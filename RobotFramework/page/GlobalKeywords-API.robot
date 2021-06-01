*** Settings ***
Library     RequestsLibrary
Library     Collections

# Here we add custom libraries we've written ourselves.
# Custom libraries are path relative to this file.
Library     ../../../libraries/fakeData.py

*** Keywords ***

# Keywords to make it easier to override environment

Pick API Environment
    [Arguments]  ${environment}='QA'
    [Documentation]     Makes for easier choosing of an environment and user
    ...                 so that command line arguments don't reach a mile long
    
    # TODO:  Add support for a firm / user check!!
    Run keyword if  "qa" in "${environment.lower()}"    
    ...     Run keywords
    ...     Set Suite Variable  ${username}     ${QA_UserName}      AND
    ...     Set Suite Variable  ${password}     ${QA_Password}      AND
    ...     Set Suite Variable  ${URL}          ${QA_URL}           AND
    ...     Set Suite Variable  ${firmid}       ${QA_Firm_5}        AND
    ...     Set Suite Variable  ${apikey}       ${QA_Default_API_Key}
    ...     ELSE IF     "local" in "${environment.lower()}"
    ...     Run keywords
    ...     Set Suite Variable  ${username}  ${Local_UserName}      AND
    ...     Set Suite Variable  ${password}  ${Local_Password}      AND
    ...     Set Suite Variable  ${URL}       ${Local_URL}           AND
    ...     Set Suite Variable  ${firmid}    ${Local_Firm_1}        AND
    ...     Set Suite Variable  ${apikey}    ${Local_Default_API_Key}
    ...     ELSE IF     "dev" in "${environment.lower()}"    
    ...     Run keywords
    ...     Set Suite Variable  ${username}  ${DevInt_UserName}     AND
    ...     Set Suite Variable  ${password}  ${DevInt_Password}     AND
    ...     Set Suite Variable  ${URL}       ${DevInt_URL}          AND
    ...     Set Suite Variable  ${firmid}    ${DevInt_Firm_822}     AND
    ...     Set Suite Variable  ${apikey}    ${DevInt_Default_API_Key}
    ...     ELSE IF  "staging" in "${environment.lower()}"    
    ...     Run keywords
    ...     Set Suite Variable  ${username}  ${Staging_UserName}     AND
    ...     Set Suite Variable  ${password}  ${Staging_Password}     AND
    ...     Set Suite Variable  ${URL}       ${Staging_URL}          AND
    ...     Set Suite Variable  ${firmid}    ${Staging_Firm_822}     AND
    ...     Set Suite Variable  ${apikey}    ${Staging_Default_API_Key}
    ...     ELSE IF  "uat" in "${environment.lower()}"    
    ...     Run keywords
    ...     Set Suite Variable  ${username}  ${UAT_UserName}     AND
    ...     Set Suite Variable  ${password}  ${UAT_Password}     AND
    ...     Set Suite Variable  ${URL}       ${UAT_URL}          AND
    ...     Set Suite Variable  ${firmid}    ${UAT_Firm_822}     AND
    ...     Set Suite Variable  ${apikey}    ${UAT_Default_API_Key}
    ...     ELSE IF  "${environment.lower()}" in ["production", "prod"]
    ...     Run keywords
    ...     Set Suite Variable  ${username}  ${Production_UserName}     AND
    ...     Set Suite Variable  ${password}  ${Production_Password}     AND
    ...     Set Suite Variable  ${URL}       ${Production_URL}          AND
    ...     Set Suite Variable  ${firmid}    ${Production_Firm_822}     AND
    ...     Set Suite Variable  ${apikey}    ${Production_Default_API_Key}

    # Always needs to be set
    Set Suite Variable  &{headers}  Content-Type=application/json   
    ...                             Authorization=Basic    
    ...                             x-API-firm-id=${firmid}
    ...                             x-API-api-key=${apikey}


# Keywords that make life easier when writing API tests

Convert Username And Password
    [Arguments]      ${user}='test'     ${pass}='test'
    [Documentation]     Sets up the username and password to be base 64 encoded
    ...                 for setting up an api call 
    ${work}=    Evaluate    (${user}, ${pass},)
    [return]    ${work}

Start Standard API Session
    [Arguments]     ${session_name}
    [Documentation]     This keyword will simplify the starting up of a requests session
    ...                 This is a standard session, that assumes it will be having a
    ...                 username and password and firmid sent every time.
    Pick API Environment  ${env_over}
    ${user_pass}=   Convert Username And Password  "${username}"  "${password}"    # quoted here so you don't have to on the variables
    create session  alias=${session_name}   url=${URL}  headers=${headers}  auth=${user_pass}

Start Custom API Session
    [Arguments]     ${session_name}  ${user}="${username}"  ${pass}="${password}"
    ...             ${firm}=${firmid}  ${api-key}=${apikey}
    [Documentation]     This keyword will allow you to override certain variables in order
    ...                 to test certain aspects of the api, such as authentication.

    # TODO:  Allow tokenization and all that jazz.
    Pick API Environment  ${env_over}
    ${user_pass}=   Convert Username And Password  ${user}  ${pass}
    Set To Dictionary   ${headers}  x-API-firm-id   ${firm}
    Set To Dictionary   ${headers}  x-API-api-key   ${api-key}
    create session  alias=${session_name}   url=${URL}  headers=${headers}  auth=${user_pass}

Get the top ID from the route
    [Arguments]     ${route}    ${API_session}      ${id_field}
    [Documentation]     Gets the first ID from the route.  This is a common thing to do.
    ${response}=    get request     ${API_session}     api/${route}
    ${record_id}=   Get From Dictionary  ${response.json()[0]}     ${id_field}   
    [Return]    ${record_id}

Get the name from the response
    [Arguments]     ${response}     ${field_name}
    [Documentation]     Returns the project name from the response.  This is useful for search smoke tests.
    ${record_name}=     Run Keyword if  "${response.json().__class__.__name__}" == "list"
    ...  Get From Dictionary     ${response.json()[0]}   ${field_name}
    ...  ELSE IF  "${response.json().__class__.__name__}" == "dict"
    ...  Get From Dictionary     ${response.json()}   ${field_name}
    [Return]    ${record_name}

Get a random name from the response
    [Arguments]     ${response}     ${name_field}
    [Documentation]     This one gets a random name from the response, and returns the name.
    ${record}=      Evaluate    random.choice(${response.json()})   random
    ${record_name}=     Get from Dictionary     ${record}   ${name_field}
    [return]    ${record_name}

# Assertions that are used in multiple tests

Verify Route Has Schema
    [Arguments]     ${response}
    [Documentation]     Verifies that what we are looking at is indeed schema
    Should Be True    "PropertyName" in """${response.text}"""

Verify Route Is In Parent's Schema
    [Arguments]     ${response}     ${route}
    [Documentation]     Verifies that the route we are looking for is in the parent's schema
    Should Be True      "${route}" in """${response.text.lower()}"""

Expect The Status Code To Be 200
    [Arguments]     ${code}="Not Passed In"
    [Documentation]     Verifies that the included status code is 200
    Should Be Equal As Strings      ${code}     200

Expect The Status Code To Be 401
    [Arguments]     ${code}="Not Passed In"
    [Documentation]     Verifies that the included status code is 401
    Should Be Equal As Strings      ${code}     401

Expect Action Not Supported
    [Arguments]     ${response}
    [Documentation]     Verifies that an action, such as get, put, post, etc, is not supported.
    Should Be True      "The requested resource does not support" in """${response.text}"""

# Yes, there is two, and its really for readability in the test.  Will need to learn if these
#   can be aliased or something.
Expect The Field In the Response
    [Arguments]     ${field}    ${response}
    [Documentation]     Verifies that the field is included in the response
    Should Be True      "${field}" in """${response.text}"""

Expect item is in the response
    [Arguments]     ${item}     ${response}
    [Documentation]     Verifies that an item is in the response
    Should Be True      "${item}" in """${response.text}"""

Expect Simple Post Data Is In The Response
    [Arguments]     ${data}     ${response}     ${field_name}
    [Documentation]     Checks the response, and makes sure the simple data is returned
    ${unwound_dictionary}=  Get From List  ${data}  0
    ${unwound_data}=    Get From Dictionary     ${unwound_dictionary}   ${field_name}
    Should Be True      "${unwound_data}" in """${response.text}"""

Expect Simple Put Data Is In The Response
    [Arguments]     ${data}     ${response}     ${field_name}
    [Documentation]     Checks the response, and makes sure the simple data is returned
    ${unwound_data}=    Get From Dictionary     ${data}   ${field_name}
    Should Be True      "${unwound_data}" in """${response.text}"""

Expect the ID to not be in the response
    [Arguments]     ${id}       ${response}
    [Documentation]     Makes sure a record ID is not in the response
    Should Be True      "${id}" not in """${response.text}"""

Expect the ID to be in the response
    [Arguments]     ${id}       ${response}
    [Documentation]     Makes sure a record ID is in the response
    Should Be True      "${id}" in """${response.text}"""

Expect There To Be Only One Returned Record not in an array
    [Arguments]     ${id}    ${response}
    [Documentation]     Makes sure the response only contains one record
    ...                 This is specific to calling an ID, so it should not be a list
    Should Be True  ("${response.json().__class__.__name__}" == "dict") == ("${id}" in """${response.json()}""")

Expect the size of the response to match
    [Arguments]     ${response}     ${size}
    [Documentation]     Makes sure the response from API is the size we expect.
    Should Be True     len(${response.json()}) == ${size}

Expect the responses to have been paged
    [Arguments]     
    ...     ${first_response}   
    ...     ${second_response}  
    ...     ${page_start}      
    [Documentation]     Makes sure that the three responses are paged
    Should Be True      ${first_response.json()}[${page_start}] == ${second_response.json()}[0]

Expect the responses to have been paged when the returns are backwards
    [Arguments]     
    ...     ${first_response}   
    ...     ${second_response}  
    ...     ${page_start}      
    [Documentation]     Makes sure that the three responses are paged -- Some endpoints are sorted backwards
    Should Be True      ${first_response.json()}[0] == ${second_response.json()}[${page_start}]
