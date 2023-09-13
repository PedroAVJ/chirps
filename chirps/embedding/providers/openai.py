"""OpenAI implementation for embedding provider."""
import logging
from typing import Any

import openai
from django.contrib.auth.models import User

from .base import BaseEmbeddingProvider, EmbeddingError

logger = logging.getLogger(__name__)


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    """OpenAI implementation for embedding providers."""

    def embed(self, user: User, model: str, text: str) -> Any:
        """Use OpenAI to generate embeddings for the specified text."""
        # If the OpenAI API key is not set, raise an error
        if user.profile.openai_api_key in [None, '']:
            logger.error('User OpenAI key not set', extra={'user_id': user.id})
            raise EmbeddingError('OpenAI API key not set')

        # Initialize the OpenAI API key from the user's profile
        openai.api_key = user.profile.openai_api_key

        logger.debug('Generating embedding for text', extra={'text': text})

        # Generate the embedding
        try:
            response = openai.Embedding.create(model=model, input=text)
        except openai.error.InvalidRequestError as err:
            raise EmbeddingError(f'Embedding failure: {str(err)}') from err

        logger.debug(
            'Embedding complete',
            extra={
                'prompt_tokens': response['usage']['prompt_tokens'],
                'total_tokens': response['usage']['total_tokens'],
            },
        )
        return response['data'][0]['embedding']
