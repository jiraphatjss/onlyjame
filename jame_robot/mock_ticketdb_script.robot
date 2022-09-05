*** Settings ***
Library   SSHLibrary
Library   DatabaseLibrary
Library   OperatingSystem

Suite Setup  setup connection to database
#Suite Teardown  close connection

*** Variables ***
${DBname}  artist-service_artist-db_1
${DBUser}  postgres
${DBpass}  example-password
${DBHost}  events.dev.biggestfan.net
${DBPort}  5432
${stdout}  read command output  

*** Keywords ***
setup connection to database
    Open connection  events.dev.biggestfan.net
    Log in with public key  biggestfan  /home/karn/.ssh/id_rsa
    write  docker exec -it ticket-service_ticket-db_1 psql -U postgres ticket_service
    
*** Test Cases ***
insert 
    sleep  2s
    write  insert into event (slug,layout_venue_slug,layout_slug,name,image,banner,description,short_description) values ('ink-waruntorn','impact-arena','convention-center','Ink On Earth','https://i.pinimg.com/originals/cc/c7/67/ccc767704907e6f8a9af117fd6685449.png','https://adaymagazine.com/wp-content/uploads/2021/05/Type-F_Ink_%E0%B8%89%E0%B8%B1%E0%B8%99%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B4%E0%B8%94%E0%B8%96%E0%B8%B6%E0%B8%87%E0%B9%80%E0%B8%98%E0%B8%AD%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B9%84%E0%B8%AB%E0%B8%99-04.jpg','ink concert','Ink On Earth') ;
    sleep  2s
    write  insert into event_period (event_slug,slug,time_period) values ('ink-waruntorn','round-1','["2021-12-21 11:00:00.638843+00","2022-01-01 14:00:0.638843+00"]') ;
    sleep  2s
    write  insert into ticket_definition (event_slug,slug,name,sale_period,quantity,price_default_currency,price_accept_currencies,price_currencies,type) values ('ink-waruntorn','night','Night','["2021-12-21 00:00:00.638843+00","2022-01-01 05:00:00.638843+00"]',500,'THB','["THB","USD"]','{"THB":{"amount":"1200"},"USD":{"amount":"40"}}','one-ticket') ;
    sleep  2s
    write  insert into ticket_definition_event_period values ('ink-waruntorn','night','ink-waruntorn','round-1') ;
    sleep  2s
    write  insert into ticket_definition_slot_type values ('ink-waruntorn','night','impact-arena','convention-center','dance-section','dance-slot',1) ;