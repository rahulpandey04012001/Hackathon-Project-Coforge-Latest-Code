def generate_gherkin_feature_file(user_story, gpt_cases):
    """
    Generate a Gherkin feature file content for a given user story and its test cases.

    Args:
        user_story (str): The user story for which to generate the feature file.
        gpt_cases (list): List of test case dictionaries, each containing 'Steps' and 'Expected'.

    Returns:
        str: Path to the generated feature file.
    """
    # Construct the feature file content
    feature_content = f"Feature: {user_story}\n\n"

    for idx, case in enumerate(gpt_cases, 1):
        scenario_title = f"Scenario {idx}: Test Case {idx}"
        feature_content += f"{scenario_title}\n"

        steps = case.get('Steps', [])
        if steps:
            # Use the first step as the "Given"
            feature_content += f"  Given {steps[0]}\n"

            # Use remaining steps as "When"
            for step in steps[1:]:
                feature_content += f"  When {step}\n"
        else:
            # If no steps, fall back to a placeholder
            feature_content += f"  Given No step defined.\n"

        # Add the expected outcome as the "Then"
        feature_content += f"  Then {case.get('Expected', 'No expected result defined')}\n\n"

    # Save the feature content to a file
    feature_filename = "generated_feature.feature"
    with open(feature_filename, "w") as file:
        file.write(feature_content)

    return feature_filename
