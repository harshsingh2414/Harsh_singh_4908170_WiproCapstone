Feature: Product functionality

  Scenario: User adds product to cart

    Given user opens product page
    When user adds product to bag
    Then product should be added successfully