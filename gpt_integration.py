import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_test_cases_with_gpt3(user_story, max_cases, include_negative=False):
    """
    Generate detailed test cases using GPT-3.5 based on the provided user story.

    Args:
        user_story (str): The user story for which to generate test cases.
        max_cases (int): Maximum number of test cases to generate.
        include_negative (bool): Whether to include negative test scenarios.

    Returns:
        list: A list of generated test cases.
    """
    try:
        # Define the prompt for the LLM
        scenario_type = "positive and negative" if include_negative else "positive"
        prompt = f"""
        Analyze the following user story and generate {scenario_type} test cases:

        User Story: {user_story}

        Provide the test cases in this format:
        1. Test Case Title
        - Step: [Action to be performed]
        - Expected Result: [Expected outcome]
        Limit the response to a maximum of {max_cases} test cases.
        """

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a test case generation assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # Extract and split the response content into individual test cases
        response_text = response['choices'][0]['message']['content']
        test_cases = response_text.split('\n\n')  # Splitting by double newline to get individual test cases

        # Restrict the number of test cases based on max_cases value
        limited_test_cases = test_cases[:max_cases]

        return limited_test_cases

    except openai.error.OpenAIError as e:
        return [f"Error generating test cases: {e}"]
