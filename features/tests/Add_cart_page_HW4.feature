# Created by user at 2/20/23
Feature: Amazon add to cart test

  Scenario: User can add product to cart
    Given Open Amazon page
    When Input this text adjustable dumbbell set
    When Click on search button
    And Click on product
    And Click on cart
    When Open cart page
    Then Verify cart has 1 item(s)
