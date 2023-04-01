# Created by user at 2/20/23
Feature: Amazon search test

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders Link
    Then Verify Sign In page is opened


  Scenario: Verify shopping cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify Amazon Cart is empty


