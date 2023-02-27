# Created by user at 2/20/23
Feature: Amazon bestsellers link test

  Scenario: Verify bestseller has correct amount of links
    Given Open Amazon page
    Then Verify bestseller has 5 links
