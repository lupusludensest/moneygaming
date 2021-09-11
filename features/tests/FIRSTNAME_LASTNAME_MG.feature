# Created by rapid at 7/9/2021
Feature: # 002 Password must be at least 6 characters long with at least one number and at least one special character

  Scenario: # 002 Password must be at least 6 characters long with at least one number and at least one special character
    Given Loginpage
    Then Fill all fields and choose options before entering password
    And Send password one1Two@ verify it is at least 6 chars length, has [1234567890] and [!@#$%^&*()_]
    Then Resend password one1Two@ verify it is at least 6 chars length, has [1234567890] and [!@#$%^&*()_]
