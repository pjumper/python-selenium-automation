# Created by user at 2/20/23
Feature: Amazon bestsellers link test

  Scenario: Bestseller has correct amount of links
    Given Open Amazon bestseller page
    Then Verify bestseller has 5 links
