import json
import re
from celery import shared_task
from django.utils import timezone
from target.models import BaseTarget

from .models import Result, Rule, Scan


@shared_task
def add(x, y):
    return x + y


@shared_task
def scan_task(scan_id):

    print(f'Running a scan {scan_id}')
    try:
        scan = Scan.objects.get(pk=scan_id)
    except Scan.DoesNotExist:
        error = f'Scan {scan_id} does not exist'
        print(error)
        scan_task.update_state(state='FAILURE', meta={'error': error})
        return

    # Need to perform a secondary query in order to fetch the derrived class
    # This magic is handled by django-polymorphic
    target = BaseTarget.objects.get(id=scan.target.id)

    # Now that we have the derrived class, call its implementation of search()
    for rule in scan.plan.rules.all():  
        print(f'Running rule {rule}')  
        results = target.search(query=rule.query_string, max_results=100)  
  
        matches = 0  
        found_matches = []  # Create a list to store the actual regex matches  
        for text in results:  
            regex_matches = re.findall(rule.regex_test, text)  
            matches += len(regex_matches)  
            found_matches.extend(regex_matches)  # Append the regex matches to the found_matches list  
  
        # Perform the regex against the results  
        # TODO: Convert the query to an embedding if required by the target.  
  
        # Update the Result object creation to include the found_matches list as the value for the findings field  
        findings = json.dumps(found_matches)
        result = Result(count=matches, result=True, rule=rule, findings=findings)  
        result.save()  
  
        scan.results.add(result)
    
    # Persist the completion time of the scan
    scan.finished_at = timezone.now()
    scan.save()
    print(f'Saved scan results')
