*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
# variables to make finding things inside a call log in API easier.
${calllogs_route}    calllogs
${calllogs_name_field}  subject
${calllogs_id_field}    id

*** Keywords ***
Simple Call Log Post Data
    [Arguments]     ${count}=1
    [Documentation]     Returns a simple call log's data, for post requests.  It's only the subject.

    ${data}=  Create List
    :For    ${i}   IN RANGE  ${count}
    \   ${inner_data}=     Simple Call Log Put Data
    \   Append To List  ${data}     ${inner_data}
    [Return]  ${data}

Simple Call Log Put Data
    [Documentation]     Returns a simple call log's data, for put requests.  It's only the subject.

    ${subject}=     random call subject

     ${data}   Create Dictionary
    ...     ${calllogs_name_field}    ${subject}
    [Return]  ${data}

Make sure we have calls
    [Documentation]     This is a setup for call logs to make sure we have
    ...                 at least 20 call logs
    Start Standard API Session      API
    ${response}=    get request     API     api/calllogs
    ${count}=    get length     ${response.json()}
    ${evaluation}=      evaluate    20 - ${count}
    ${data}=    simple call log post data      ${evaluation}
    Run keyword if  ${count} < 20
    ...     post request    API     api/calllogs   ${data}