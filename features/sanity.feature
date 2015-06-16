Feature: Sanity check

    This is an example of a feature file. You can either use a blurb here for
    documentation, or the standard "In order to/As a/I want" format recommended
    by many.

    Background:
        Given behave is behaving

    Scenario: Simple Addition
        When I add 2 and 2
        Then I should have 4

    Scenario: True is True, not False
        When I check the value of True
        Then it should be True
        And  it should not be False

