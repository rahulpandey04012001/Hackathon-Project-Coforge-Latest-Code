Feature: As a user, I want to reset my password so that I can access my account.

  Scenario: Scenario 1: Test Case 1
    Given Click on the "Reset Password" link and enter a new password.
    Then Password is successfully reset and the user can access the account with the new password.

  Scenario: Scenario 2: Test Case 2
    Given Try to reset the password with invalid input (e.g., blank password field).
    Then System displays appropriate error message prompting for valid input.

  Scenario: Scenario 3: Test Case 3
    Given Reset the password with a weak password (e.g., less than 8 characters).
    Then System prompts the user to enter a password that meets security requirements.

  Scenario: Scenario 4: Test Case 4
    Given Reset the password and check for a confirmation message.
    Then User receives a confirmation message indicating successful password reset.

