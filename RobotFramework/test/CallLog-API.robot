*** Settings ***
Library    RequestsLibrary
Library    Collections
Resource   ../../PageObjs/Global/GlobalKeywords.robot
Resource   ../../PageObjs/Global/GlobalVariables.robot
Resource   ../../PageObjs/Routes/calllogs/CallLog.robot

Test Setup      Make sure we have calls

*** Test Cases ***
The Call Log Endpoint Allows A User to Read It
    [Documentation]     A GET call to the calllogs endpoint should return records
    [Tags]  API     Call Logs   Activities   Smoke   GET
    Start Standard API Session  API
    ${response}=    get request     API     api/calllogs
    Expect The Field In the Response  ${calllogs_name_field}  ${response}

The Call Log Endpoint Allows A User to Read a Single Call Log
    [Documentation]     A GET call to the call logs endpoint with a valid id should return a record
    [Tags]  API     Call Logs   Activities   Smoke   GET  By ID
    Start Standard API Session  API
    ${record_id}=   Get the top ID from the route  calllogs  API  ${calllogs_id_field}
    ${response}=    get request     API     api/calllogs/${record_id}
    Expect There To Be Only One Returned Record not in an array  ${record_id}     ${response}

The Call Log Endpoint Allows A User to Make A Call Log
    [Documentation]     A POST call to the calllogs endpoint with valid data should create a record
    [Tags]  API  Call Logs   Activities   Smoke   POST
    Start Standard API Session  API
    ${data}=    Simple Call Log Post Data   
    ${response}=    post request    API     api/calllogs   ${data}
    # We actually want to read from the get after for this test
    ${response}=    get request     API     api/calllogs
    Expect Simple Post Data Is In The Response  ${data}  ${response}     ${calllogs_name_field}

The Call Log Endpoint Allows A User to Delete A Call Log
    [Documentation]     A DELETE call to the calllogs endpoint with valid id should delete the call log
    [Tags]  API  Call Logs   Activities   Smoke   DELETE
    Start Standard API Session  API
    ${record_id}=   Get the top ID from the route  calllogs  API  ${calllogs_id_field}
    ${response}=    delete request  API     api/calllogs/${record_id}
    ${response}=    get request     API     api/calllogs
    Expect the ID to not be in the response     ${record_id}   ${response}

The Call Log Endpoint Allows A User to Update a Call Log
    [Documentation]     A PUT call to the calllogs endpoint with a valid id and valid data should update a calllog
    [Tags]  API   Call Logs   Activities   Smoke   PUT
    Start Standard API Session  API
    ${record_id}=   Get the top ID from the route  calllogs  API  ${calllogs_id_field}
    ${data}=    Simple Call Log Put Data
    ${response}=    put request     API     api/calllogs/${record_id}   ${data}
    ${response}=    get request     API     api/calllogs
    Expect Simple Put Data Is In The Response  ${data}  ${response}  ${calllogs_name_field}

The call log endpoint will allow a user to receive a specific size return
    [Documentation]     A GET call to calllogs specifying a size will return size records.
    [Tags]  API     Call Logs   Regression      GET     Sizing
    Start Standard API Session  API
    # We are doing 3 sizes for this test to confirm it
    ${size_first}=     set variable     13
    ${size_second}=    set variable      5
    ${size_third}=     set variable      8

    ${response_first}=   get request     API     api/calllogs?size=${size_first}
    ${response_second}=  get request     API     api/calllogs?size=${size_second}
    ${response_third}=   get request     API     api/calllogs?size=${size_third}

    Expect the size of the response to match    ${response_first}       ${size_first}
    Expect the size of the response to match    ${response_second}      ${size_second}
    Expect the size of the response to match    ${response_third}       ${size_third}

The call log endpoint will allow a user to page through to receive multiple pages
    [Documentation]     A GET call to calllogs specifying paging will return sequential records.
    [Tags]      API     Call Logs   Regression      GET     Paging
    Start Standard API Session  API
    ${page_start}=     set variable    8

    ${response_first}=   get request     API     api/calllogs
    ${response_second}=  get request     API     api/calllogs?from=${page_start}

    Expect the responses to have been paged     
    ...     ${response_first}   
    ...     ${response_second}  
    ...     ${page_start}