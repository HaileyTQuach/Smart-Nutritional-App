import gradio as gr
from src.crew import NutriCoachRecipeCrew, NutriCoachAnalysisCrew

def analyze_food(image, dietary_restrictions, workflow_type):
    """
    Wrapper function for the Gradio interface.
    
    :param image: Uploaded image (PIL format)
    :param dietary_restrictions: Dietary restriction as a string (e.g., "vegan")
    :param workflow_type: Workflow type ("recipe" or "analysis")
    :return: Result from the NutriCoach workflow.
    """
    image.save("uploaded_image.jpg")  # Save the uploaded image temporarily
    image_path = "uploaded_image.jpg"

    inputs = {
        'uploaded_image': image_path,
        'dietary_restrictions': dietary_restrictions,
        'workflow_type': workflow_type
    }
    
    # Initialize the appropriate crew instance based on workflow type
    if workflow_type == "recipe":
        crew_instance = NutriCoachRecipeCrew(
            image_data=image_path,
            dietary_restrictions=dietary_restrictions
        )
    elif workflow_type == "analysis":
        crew_instance = NutriCoachAnalysisCrew(
            image_data=image_path
        )
    else:
        return "Invalid workflow type. Choose 'recipe' or 'analysis'."

    # Run the crew workflow and get the result
    crew_obj = crew_instance.crew()
    final_output = crew_obj.kickoff(inputs=inputs)
    
    return final_output

# Define the Gradio interface
interface = gr.Interface(
    fn=analyze_food,
    inputs=[
        gr.Image(type="pil"),                           # Image input (PIL format)
        gr.Textbox(label="Dietary Restrictions (optional)", placeholder="e.g., vegan"),  # Text input
        gr.Radio(["recipe", "analysis"], label="Workflow Type")  # Radio buttons for workflow selection
    ],
    outputs=gr.Textbox(label="Result"),                 # Textbox output for result
    title="AI NutriCoach",
    description="Upload an image of food and select a workflow type (recipe or analysis) to get nutritional insights or recipe ideas.",
    theme="default"
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()
