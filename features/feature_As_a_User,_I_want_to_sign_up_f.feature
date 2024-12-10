Feature: As a User, I want to sign up facebook.

  Scenario: Scenario 1: Test Case 1
    Given Enter valid email, password, and required information in the sign-up form.
    Then User account is successfully created on Facebook.

  Scenario: Scenario 2: Test Case 2
    Given Enter a weak password (e.g., less than 8 characters) during sign up.
    Then System should display an error message indicating password strength requirements.

  Scenario: Scenario 3: Test Case 3
    Given Enter an invalid email format (e.g., without '@' symbol) in the email field.
    Then System should display an error message indicating invalid email format.

  Scenario: Scenario 4: Test Case 4
    Given Attempt to sign up without accepting the terms and conditions.
    Then System should prevent user from signing up and prompt the user to accept the terms and conditions.

