import os
import yaml
import base64
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from tools import (
    ExtractIngredientsTool, 
    FilterIngredientsTool, 
    DietaryFilterTool,
    NutrientAnalysisTool
)
from models import RecipeSuggestionOutput, NutrientAnalysisOutput 
from io import BytesIO

load_dotenv()
WATSONX_API_KEY = os.environ.get('WATSONX_API_KEY')
WATSONX_URL = os.environ.get('WATSONX_URL')
WATSONX_PROJECT_ID = os.environ.get('WATSONX_PROJECT_ID')

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
