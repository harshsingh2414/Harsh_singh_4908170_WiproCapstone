Feature: Login functionality

  Scenario: User opens login popup and skips login

    Given user opens Nykaa website
    When user opens login popup
    And user chooses mobile email option
    Then user clicks skip login