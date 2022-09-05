*** Settings ***
Library  SeleniumLibrary
Library  SSHLibrary
Library  DatabaseLibrary
Variables  variables.py

*** Keywords ***
Connect to eventdb
    Open Connection  events.dev.biggestfan.net  port=51412
    Login With Public Key  biggestfan  /home/jame/.ssh/id_ed25519
    write  docker exec -it ticket-service_ticket-db_1 psql -U postgres ticket_service
Disconnect from eventdb
    Write  exit
    Write  pwd
    Read Until  /home/biggestfan
    close connection
Open Chrome
    Open Browser  https://www.google.com/  Chrome
    Maximize Browser Window
Close Chrome
    Close All Browsers
There is upcoming event A in database
    Write  select * from event where slug = ${upcoming_event_A} ;
    ${read}=  Read Until  ${upcoming_event_A}
    Should Contain  ${read}  ${upcoming_event_A}
There is previous event A in database
    Write  select * from event where slug = ${previous_event_A} ;
    ${read}=  Read Until  ${previous_event_A}
    Should Contain  ${read}  ${previous_event_A}
There is artist A in database
    Write  select * from artist where id = ${artist_A_id} ;
    ${read}=  Read Until  ${artist_A_name}
    Write  select * from event_artist where artist_id = ${artist_A_id} ;
    ${read}=  Read Until  ${upcoming_event_A}
    Should Contain  ${read}  ${upcoming_event_A}

User access to biggestfan event site
    Go to  ${eventdev}
User should see upcoming events A
    wait until element is visible  css:[data-robot=upcoming-event-music-festival]
User select event A on eventlist
    wait until element is visible  css:[data-robot=upcoming-event-music-festival]
    click element  css:[data-robot=upcoming-event-music-festival]
upcoming events contain "event name" and "start date"
    wait until element is visible  css:[data-robot=upcoming-event-name-music-festival]
    wait until element is visible  css:[data-robot=upcoming-event-time-music-festival]
User should see previous events A
    wait until element is visible  css:[data-robot=previous-event-stamp-live-in-concert]
previous events contain "event name" and "short description"
    wait until element is visible  css:[data-robot=previous-event-name-stamp-live-in-concert]
    wait until element is visible  css:[data-robot=previous-event-desc-stamp-live-in-concert]
User is redirected to event A detail page
    wait until location contains  event-details/${upcoming_event_A}/
event detail page contains "event name", "related artist","date of event", "duration of event","price of ticket" and event A details
    wait until element is visible  css:[data-robot=event-name]
    wait until element is visible  css:[data-robot=event-name]
    wait until element is visible  css:[data-robot=event-name]
    wait until element is visible  css:[data-robot=event-name]
User select artist A from artist panel
    wait until element is visible  css:[data-robot=artist_Ink Waruntorn]
User selects artist A under event name
    wait until element is enabled  css:[data-robot=link-artist-${artist_A_slug}]
    click element  css:[data-robot=link-artist-${artist_A_slug}]
User is redirected to artist A page
    wait until location contains  ${artist_A_slug}
    wait until element is visible  id:artist-name
User selects "Contact Us" at footer
    wait until element is enabled  css:[data-robot=contact-us]
    execute javascript  window.scrollTo(0, document.body.scrollHeight)
    sleep  2s
    click element  css:[data-robot=contact-us]
User selects "Terms and Conditions" at footer
    wait until element is enabled  css:[data-robot=term-and-conditions]
    execute javascript  window.scrollTo(0, document.body.scrollHeight)
    sleep  2s
    click element  css:[data-robot=term-and-conditions]
User selects "Data Protection & Privacy Policy" at footer
    wait until element is enabled  css:[data-robot=data-privacy]
    execute javascript  window.scrollTo(0, document.body.scrollHeight)
    sleep  2s
    click element  css:[data-robot=data-privacy]
User selects "Refund Policy" at footer
    wait until element is enabled  css:[data-robot=refund-policy]
    execute javascript  window.scrollTo(0, document.body.scrollHeight)
    sleep  2s
    click element  css:[data-robot=refund-policy]
User should be able to redirect to <ContactUs> page
    wait until location contains  contact-us/?menu=contact-us
    Wait Until Element Is Visible  css:[data-robot=contact-header]
User should be able to redirect to <Terms-and-conditions> page 
    wait until location contains  contact-us/?menu=terms-and-conditions
    Wait Until Element Is Visible  css:[data-robot=terms-header]
User should be able to redirect to <Data-Protection-and-Privacy-Policy> page
    wait until location contains  contact-us/?menu=data-protection
    Wait Until Element Is Visible  css:[data-robot=data-header]
User should be able to redirect to <Refund-Policy> page
    wait until location contains  contact-us/?menu=refund
    Wait Until Element Is Visible  css:[data-robot=refund-header]
    

