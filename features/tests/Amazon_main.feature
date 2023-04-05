# Created by user at 4/2/23
Feature: Amazon search features

  Scenario: User can see language option
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario: User can see new arrivals
    Given Open Amazon Fashion page
    When Hover over new arrival
    Then Verify user sees new arrival products


