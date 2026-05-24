Feature: Nykaa Negative Test Cases


  Scenario: Search invalid product

    Given user opens Nykaa website

    When user searches for "12qwe3"

    Then no results message should be shown


  Scenario: Proceed button should not work for empty cart

    Given user opens Nykaa website

    When user opens cart

    Then proceed button should be visible





