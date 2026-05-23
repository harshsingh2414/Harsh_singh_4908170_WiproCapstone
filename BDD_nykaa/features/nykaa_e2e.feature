Feature: Nykaa E2E Flow

  Scenario: User completes full product purchase flow till cart

    Given user opens Nykaa website

    When user opens login popup
    And user selects mobile or email login option
    And user clicks skip login button

    And user hovers on skin menu
    And user clicks on moisturizers category

    And user selects brand "Cetaphil"
    And user selects first moisturizer product

    And user adds product to bag
    And user opens cart from product page

    Then user clicks on proceed button