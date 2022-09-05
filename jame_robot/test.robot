*** Settings ***
Library  SeleniumLibrary
Resource  keywords.resource
Suite Setup  Connect to eventdb
Suite Teardown  Disconnect from eventdb
Test Setup  Open Chrome
Test Teardown  Close Chrome
*** Test Cases ***
close connection
    Write  exit
    Write  pwd
    Read Until  /home/biggesfan

