# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html


*** Settings ***
Library    SeleniumLibrary
Library     String

Suite Setup    Log    I'm inside test suite setup 
Suite Teardown     Log    I'm inside test suite teardown
Test Setup    Log    I'm inside test setup 
Test Teardown     Log    I'm inside test teardown

Default Tags    SANITY

Library    webdrivermgr.py

*** Test Cases ***

MyFirstTest
     [Tags]    SMOKE     # overrides default tags
    Log    This test was executed by {username} on {os}..    #env variables
    Log    Test name is ${SUITE NAME} and result is ${PREV_TEST_STATUS}  # built in variables
    
    
FirstSeleniumCase
    Remove Tags    SANITY
    Open Browser    https://google.com    headlesschrome
    Set Browser Implicit Wait    5
    Input Text    name=q    Milan
    Press Keys    None      ENTER
    #Click Button    name=btnK
    Close Browser


Amit
     ${v1}    Set Variable    0.01
     Should be true     ${v1} > 0   
    FOR    ${i}    IN RANGE    50 
        ${ret} =	Evaluate	random.randint(1, 2)
        log to Console     ${ret}
    END
#
#
#
#SampleLoginCase
#    [Documentation]    This is sample login test
#    Open Browser      ${URL}    chrome
#    Set Browser Implicit Wait    5
#    LOGINACTION
#    Click Element    id=welcome
#    Click Element    link=Logout
#    Title Should Be    &{LOGIN_DATA}[title]
#    Close Browser

#Independant Login Case
#    ${driver}=      chromedriver path
#    log    ${driver}
#    Open Browser      https://google.com    chrome  executable_path=${driver}
#    ${work}=    Evaluate    (""user"", ""pass"",)
#    log    ${work}
#    INDEPENDANT KEYWORDS

    

*** Variables ***
${URL}     https://opensource-demo.orangehrmlive.com/  # SCALAR
@{CREDENTIALS}     Admin    admin123  # LIST
${LOGIN_DATA}    title=OrangeHRM      # KEY_VALUE PAIRS
${host}

*** Keywords ***
# Club built-in keyword actions. Enable reuse of same steps in multiple test cases
LOGINACTION
    Input Text    id=txtUsername    @{CREDENTIALS}[0]
    Input Password    id=txtPassword    @{CREDENTIALS}[1]
    Click Button    name=Submit 

INDEPENDANT KEYWORDS
    ${host}=    get location
    log    ${host}
    ${cookie}=     get cookie
    log     ${cookie.name}      ${cookie.domain}
    go to   ${host}/maps

Verify Evaluate
    ${1}    Set Variable    Hello
    ${2}    Set Variable    HERE
    ${3}    Set Variable    ${1}-${2}
    ${4}    Evaluate    "${1}" + " world"
    ${5}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Log To Console  ${3}
    
    Log To Console  ${5}
    ${username} =	Get Value From User	Input user name	default
    ${password} =	Get Value From User	Input password	hidden=yes
    Log To Console  ${username}    ""


*** Test Cases ***
Regexp Test 
    ${name}     Set Variable    Administration
    ${escaped} 	Regexp Escape	${name}
    Log To Console      ${escaped}