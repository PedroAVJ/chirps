from django.contrib import admin
from django.db import models


class Plan(models.Model):
    """Model for what to do when scanning a target."""

    name = models.CharField(max_length=256)
    description = models.TextField()

    # True if this plan is a template for other plans
    is_template = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Rule(models.Model):
    """A step to execute within a plan."""

    name = models.CharField(max_length=256)
    description = models.TextField()

    # Query to run against the target
    query_string = models.TextField()

    # Embedding of the query string
    query_embedding = models.TextField(null=True, blank=True)

    # Regular expression to run against the response documents
    regex_test = models.TextField()

    # If the regex test finds results in the response documents, how severe of a problem is it?
    severity = models.IntegerField()

    # Foreign Key to the plan this rule belongs to
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='rules')

    def __str__(self):
        return self.name


admin.site.register(Plan)
admin.site.register(Rule)