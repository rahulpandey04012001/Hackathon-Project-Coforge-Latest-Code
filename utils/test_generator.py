def generate_test_cases(parsed_data, include_negative=False):
    """
    Generate positive (and optionally negative) test cases based on the parsed user story.

    Args:
        parsed_data (dict): Parsed information from the user story.
        include_negative (bool): Whether to include negative test scenarios.

    Returns:
        list: A list of test cases with IDs, steps, and expected results.
    """
    test_cases = []

    # Generate positive scenarios
    test_cases.append({
        "ID": 1,
        "Step": "The user enters a valid password to reset.",
        "Expected": "The system should reset the password successfully."
    })

    # Generate additional positive scenarios if needed
    test_cases.append({
        "ID": 2,
        "Step": "The user clicks the reset link and provides a valid new password.",
        "Expected": "The system updates the password and confirms success."
    })

    # Generate negative scenarios if requested
    if include_negative:
        test_cases.append({
            "ID": 3,
            "Step": "The user enters an incorrect old password.",
            "Expected": "The system should display an error message indicating the incorrect password."
        })
        test_cases.append({
            "ID": 4,
            "Step": "The user leaves the password field blank.",
            "Expected": "The system should prompt the user to enter a valid password."
        })
        test_cases.append({
            "ID": 5,
            "Step": "The user provides a password that doesn't meet the minimum complexity requirements.",
            "Expected": "The system should notify the user to choose a more secure password."
        })

    return test_cases
