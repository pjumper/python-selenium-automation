# Created by user at 2/20/23
Feature: Amazon search test

  Scenario: Verify shopping cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify Amazon Cart is empty
