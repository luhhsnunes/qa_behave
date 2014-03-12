Feature: Perform Search

Scenario: Perform a basic search on Google

Given I am on Google landing page
When I attempt to search for some information
And I click on Search button
Then I see the results from my search
