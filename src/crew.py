import os
import yaml
import base64
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tools import (
    ExtractIngredientsTool, 
    FilterIngredientsTool, 
    DietaryFilterTool,
    NutrientAnalysisTool
)
from ibm_watsonx_ai import Credentials, APIClient
from src.models import RecipeSuggestionOutput, NutrientAnalysisOutput 

credentials = Credentials(
                   url = "https://us-south.ml.cloud.ibm.com",
                   # api_key = "<YOUR_API_KEY>" # Normally you'd put an API key here, but we've got you covered here
                  )
client = APIClient(credentials)
project_id = "skills-network"

# Get the absolute path to the config directory
CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")

@CrewBase
class BaseNutriCoachCrew:
    ## TODO: Define the agents and tasks for the NutriCoach crew


@CrewBase
class NutriCoachRecipeCrew(BaseNutriCoachCrew):

    ##TODO: Define the agents and tasks for the NutriCoachRecipeCrew


@CrewBase
class NutriCoachAnalysisCrew(BaseNutriCoachCrew):

    ## TODO: Define the agents and tasks for the NutriCoachAnalysisCrew
