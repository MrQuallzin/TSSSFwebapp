Feature: Home Page

  In order to play the game
  As a user
  I want the Home Page to work

  Background:
    Given I am on the site

  Scenario: The Home Page Is Available
    When I visit the home page
    Then I should see a welcome heading
    And I should not have an error code response
