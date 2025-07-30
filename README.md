---
title: AI_NourishBot
app_file: app.py
sdk: gradio
sdk_version: 5.12.0
---
# AI NourishBot (aka AI Dietary Crew)

AI NourishBot is an AI-powered nutrition assistant that leverages advanced vision models and natural language processing to detect ingredients from food images, filter ingredients based on dietary restrictions, estimate calories, provide detailed nutrient analysis, and generate recipe suggestions. This project demonstrates the use of CrewAI, WatsonX, and other AI tools to deliver insightful and personalized nutritional feedback.

## Features

- **Ingredient Detection**  
  Detects ingredients from user-uploaded images using a vision AI model.

- **Dietary Filtering**  
  Filters detected ingredients based on user-defined dietary restrictions (e.g., vegan, gluten-free).

- **Calorie Estimation**  
  Estimates total calories from the detected ingredients.

- **Nutrient Analysis**  
  Provides a detailed breakdown of key nutrients such as protein, carbohydrates, fats, vitamins, and minerals.

- **Health Evaluation**  
  Summarizes the overall healthiness of the meal and provides a health evaluation.

- **Recipe Suggestion**  
  Generates recipe ideas based on the filtered ingredients and dietary restrictions.

## How It Works

The project is built using the CrewAI framework, which organizes agents and tasks into workflows for two primary use cases:

1. **Recipe Workflow**  
   Detects ingredients, filters them based on dietary restrictions, and suggests recipes.

2. **Analysis Workflow**  
   Directly estimates calories, performs nutrient analysis, and provides a health evaluation summary from a food image.

## Installation

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HaileyTQuach/Smart-Nutritional-App.git
   cd Smart-Nutritional-App
   ```
2. **Create and activate a virtual environment**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install the required dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
4. **Create a .env file in the root directory with the following keys**:
   ```bash
    WATSONX_API_KEY=your_watsonx_api_key
    WATSONX_URL=your_watsonx_url
    WATSONX_PROJECT_ID=your_watsonx_project_id
   ```
## Usage
### Run the Application

You can run the application using the following commands:

1. For recipe suggestions

```bash
python main.py <image_path> <dietary_restrictions> recipe
```

Example:

```bash
python main.py food.jpg vegan recipe
```

2. For food analysis

```bash
python main.py <image_path> analysis
```

Example:

```bash
python main.py food.jpg analysis
```

3. For training (future functionality - TODO)

```bash
python main.py train <n_iterations> <output_filename> <image_path> <dietary_restrictions> <workflow_type>
```

## File Structure

```
Smart-Nutritional-App-Crew/
│
├── config/
│   ├── agents.yaml               # Configuration for agents
│   └── tasks.yaml                # Configuration for tasks
│
├── src/
│   ├── crew.py                   # Crew definitions (agents, tasks, workflows)
│   ├── tools.py                  # Tool definitions for ingredient detection, filtering, etc.
│   └── main.py                   # Main script for running the application
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue.

## License

### License
This project is licensed under the **Hailey Thao Quach's Non-Commercial License**. See the `LICENSE` file for details.


## Contact

For any questions or support, please contact [Hailey Thao Quach](mailto:hailey@haileyq.com).
