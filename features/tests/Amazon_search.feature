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

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias videogames
    When Input text Legend of Zelda
    When Click on search button
    Then Verify videogames department is selected


