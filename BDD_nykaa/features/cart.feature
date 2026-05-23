Feature: Cart functionality

  Scenario: User proceeds from cart

    Given user opens cart page
    When user clicks proceed button
    Then checkout page should appear