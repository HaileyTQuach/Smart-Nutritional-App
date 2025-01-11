import os
import sys
import base64
from dotenv import load_dotenv
from crew import NutriCoachAnalysisCrew, NutriCoachRecipeCrew

# Load environment variables (e.g., API keys)
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def run(image_path: str, dietary_restrictions: str, workflow_type: str):
    print("## Welcome to the AI NutriCoach Crew")
    print('------------------------------------')

    # encoded_image = encode_image_to_base64(image_path)
    workflow_type = workflow_type.lower()

    inputs = {
        'uploaded_image': image_path,
        'dietary_restrictions': dietary_restrictions,
        'workflow_type': workflow_type
    }

    if workflow_type == 'analysis':
        crew_instance = NutriCoachAnalysisCrew(
            image_data=image_path,
        )
    elif workflow_type == 'recipe':
        crew_instance = NutriCoachRecipeCrew(
            image_data=image_path,
            dietary_restrictions=dietary_restrictions
        )
    else:
        raise ValueError("Invalid workflow type. Choose 'recipe' or 'analysis'.")

    crew_obj = crew_instance.crew()
    final_outputs = crew_obj.kickoff(inputs=inputs)
    
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print(final_outputs)

def train(n_iterations: int, output_filename: str, image_path: str, dietary_restrictions: str, workflow_type: str):
    """
    Placeholder for training functionality.
    Adapt this function based on how you want to handle training 
    with the separate crew structures if needed.
    """
    print("Training functionality is not implemented in this example.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Example usage: python main.py image.jpg analysis
        image_path = sys.argv[1]
        workflow_type = sys.argv[2].lower()
        run(image_path, dietary_restrictions=None, workflow_type=workflow_type)

    elif len(sys.argv) == 4:
        # Example usage: python main.py image.jpg vegan recipe
        image_path = sys.argv[1]
        dietary_restrictions = sys.argv[2]
        workflow_type = sys.argv[3].lower()
        run(image_path, dietary_restrictions, workflow_type)

    elif sys.argv[1] == "train" and len(sys.argv) == 7:
        # Example usage: python main.py train 10 output.txt image.jpg vegan analysis
        _, _, n_iter_str, output_filename, image_path, dietary_restrictions, workflow_type = sys.argv
        n_iterations = int(n_iter_str)
        train(n_iterations, output_filename, image_path, dietary_restrictions, workflow_type)

    else:
        print("Usage: python main.py <image_path> <dietary_restrictions> <workflow_type: recipe|analysis>")
        print("Or for analysis only: python main.py <image_path> analysis")
        print("Or for training: python main.py train <n_iterations> <output_filename> <image_path> <dietary_restrictions> <workflow_type>")
