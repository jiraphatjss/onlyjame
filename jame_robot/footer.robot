*** Settings ***
Library  SeleniumLibrary
Resource  keywords.resource
Suite Setup  Connect to eventdb
Suite Teardown  Disconnect from eventdb
Test Setup  Open Chrome
Test Teardown  Close Chrome
*** Test Cases ***
User can see "contact us" detail on contact us page
    Given User access to biggestfan event site
    When User selects "Contact Us" at footer
    Then User should be able to redirect to <ContactUs> page 
User can see "terms & conditions" detail on terms & conditions page
    Given User access to biggestfan event site
    When User selects "Terms and Conditions" at footer
    Then User should be able to redirect to <Terms-and-conditions> page 
User can see "data protection & privacy policy" detail on data protection & privacy policy page
    Given User access to biggestfan event site
    When User selects "Data Protection & Privacy Policy" at footer
    Then User should be able to redirect to <Data-Protection-and-Privacy-Policy> page
User can see "refund policy" detail on refund policy page
    Given User access to biggestfan event site
    When User selects "Refund Policy" at footer
    Then User should be able to redirect to <Refund-Policy> page