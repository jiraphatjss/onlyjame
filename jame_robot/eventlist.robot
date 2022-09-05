*** Settings ***
Library  SeleniumLibrary
Resource  keywords.resource
Suite Setup  Connect to eventdb
Suite Teardown  Disconnect from eventdb
Test Setup  Open Chrome
Test Teardown  Close Chrome
*** Test Cases ***
User can see upcoming events on homepage
    Given There is upcoming event A in database
    And User access to biggestfan event site
    When User should see upcoming events A
    Then upcoming events contain "event name" and "start date"

User can see previous events on homepage
    Given There is previous event A in database
    When User access to biggestfan event site
    Then User should see previous events A
    And previous events contain "event name" and "short description"
    