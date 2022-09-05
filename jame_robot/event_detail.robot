*** Settings ***
Library  SeleniumLibrary
Resource  keywords.resource
Suite Setup  Connect to eventdb
Suite Teardown  Disconnect from eventdb
Test Setup  Open Chrome
Test Teardown  Close Chrome
*** Test Cases ***
User can see upcoming event detail on event detail page
    Given There is upcoming event A in database
    And User access to biggestfan event site
    When User select event A on eventlist
    Then User is redirected to event A detail page
    And event detail page contains "event name", "related artist","date of event", "duration of event","price of ticket" and event A details
User can see previous event detail on event detail page
    Given There is previous event A in database
    And User access to biggestfan event site
    When User select event A on eventlist
    Then User is redirected to event A detail page
    And event detail page contains "event name", "related artist","date of event", "duration of event","price of ticket" and event A details
User can go to artist page from event detail page
    Given There is upcoming event A in database
    And There is artist A in database
    And User access to biggestfan event site
    And User select event A on eventlist
    When User selects artist A under event name
    Then User is redirected to artist A page