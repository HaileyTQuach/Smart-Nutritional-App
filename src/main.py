import os
import sys
import base64
import json
from dotenv import load_dotenv
from crew import NutriCoachAnalysisCrew, NutriCoachRecipeCrew

# Load environment variables (e.g., API keys)
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def run(image_path: str, dietary_restrictions: str, workflow_type: str):
    ## TODO: Implement the run function
    pass

if __name__ == "__main__":
    print("Hello world!")

    ## TODO: Implement the main function