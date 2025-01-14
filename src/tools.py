import json
import os
import base64
import requests
from dotenv import load_dotenv
from langchain.tools import tool
from PIL import Image
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from io import BytesIO
from typing import List
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Extracting ingredients from image...")

# Load environment variables (e.g., API keys)
WATSONX_API_KEY = os.environ.get('WATSONX_API_KEY')
WATSONX_URL = os.environ.get('WATSONX_URL')
WATSONX_PROJECT_ID = os.environ.get('WATSONX_PROJECT_ID')

credentials = Credentials(
    url=WATSONX_URL,
    api_key=WATSONX_API_KEY
)

## TODO: Define the tools for the NutriCoach crew