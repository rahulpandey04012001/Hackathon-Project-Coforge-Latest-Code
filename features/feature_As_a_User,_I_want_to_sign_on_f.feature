Feature: As a User, I want to sign on facebook

  Scenario: Scenario 1: Test Case 1
    Given Enter valid credentials and click on the "Sign In" button.
    Then User successfully signs in to Facebook.

  Scenario: Scenario 2: Test Case 2
    Given Enter invalid credentials and click on the "Sign In" button.
    Then User should not be able to sign in and an error message should be displayed.

