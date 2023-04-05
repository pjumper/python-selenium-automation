# Created by user at 2/20/23
Feature: Amazon add to cart test

  Scenario: User can add product to cart
    Given Open Amazon page
    When Input text adjustable dumbbell set
    When Click search button
    And Click product
    And Click on cart button
    When Open cart
    Then Verify cart have 1 item(s)
