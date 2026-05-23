Feature: Nykaa Positive Test Cases


  Scenario: Add same product to cart successfully

    Given user opens Nykaa website

    When user hovers on skin menu
    And user clicks on moisturizers category

    And user selects first moisturizer product

    And user adds product to bag
    And user adds product to bag

    And user opens cart from product page

    Then cart should contain items


  Scenario: Remove product from cart successfully

    Given user opens Nykaa website

    When user hovers on skin menu
    And user clicks on moisturizers category

    And user selects first moisturizer product

    And user adds product to bag
    And user opens cart from product page

    When user deletes product from cart

    Then product should be removed from cart


  Scenario: Search valid product successfully

    Given user opens Nykaa website

    When user searches for "lipstick"

    Then search results should be displayed


  Scenario: Cart should retain products after refresh

    Given user opens Nykaa website

    When user hovers on skin menu
    And user clicks on moisturizers category

    And user selects first moisturizer product

    And user adds product to bag
    And user opens cart from product page

    When user refreshes cart page

    Then cart should contain items