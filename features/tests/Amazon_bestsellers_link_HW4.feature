# Created by user at 2/20/23
Feature: Amazon bestsellers link test

  Scenario: Bestseller has correct amount of links
    Given Open Amazon page_1
    Then Verify bestseller has 5 links
