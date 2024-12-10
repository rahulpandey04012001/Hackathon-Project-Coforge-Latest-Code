Feature: As an admin, I want to be able to deactivate user accounts.

Scenario 1: Test Case 1
  Given Admin selects a specific user account to deactivate.
  When Admin clicks on the "Deactivate" button.
  Then The user account is successfully deactivated and user should no longer have access to the system.

Scenario 2: Test Case 2
  Given Admin attempts to deactivate a user account.
  When Admin confirms the deactivation action.
  Then The user account is successfully deactivated.

Scenario 3: Test Case 3
  Given Admin tries to deactivate a user account that is already deactivated.
  Then An error message is displayed indicating that the user account is already deactivated and the deactivation action cannot be performed.

