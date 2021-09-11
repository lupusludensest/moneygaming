# Created by rapid at 9/10/2021
Feature: # Verify text "This field is required" is here

  Scenario: # Verify text "This field is required" is here
    Given Loginpage
    Then Click on Join Now button
    Then Select a title in the dropdown 'Mr'
    And Fill the First Name field 'firstName'
    And Fill the Surnme field 'surName'
    Then Click Join Now button
    And Verify text 'This field is required' is here