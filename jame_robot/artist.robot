*** Settings ***
Library  SeleniumLibrary
Resource  keywords.resource
Suite Setup  Connect to eventdb
Suite Teardown  Disconnect from eventdb
Test Setup  Open Chrome
Test Teardown  Close Chrome
*** Test Cases ***
User can go to artist page via artist panel
    Given There is artist A in database
    And User access to biggestfan event site
    When User select artist A from artist panel
    Then User is redirected to artist A page