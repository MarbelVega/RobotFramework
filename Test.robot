# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html

*** Settings ***
Library    SeleniumLibrary

Suite Setup    Log    I'm inside test suite setup 
Suite Teardown     Log    I'm inside test suite teardown
Test Setup    Log    I'm inside test setup 
Test Teardown     Log    I'm inside test teardown

Default Tags    SANITY

*** Test Cases ***

MyFirstTest
     [Tags]    SMOKE     # overrides default tags
    Log    This test was executed by {username} on {os}..    #env variables
    Log    Test name is ${SUITE NAME} and result is ${PREV_TEST_STATUS}  # built in variables
    
    
FirstSeleniumCase
    Remove Tags    SANITY
    Open Browser    https://google.com    chrome
    Set Browser Implicit Wait    5
    Input Text    name=q    Milan
    Press Keys    None      ENTER
    #Click Button    name=btnK          
    Close Browser





    

    
SampleLoginCase
    [Documentation]    This is sample login test
    Open Browser      ${URL}    chrome
    Set Browser Implicit Wait    5
    LOGINACTION
    Click Element    id=welcome  
    Click Element    link=Logout 
    Title Should Be    &{LOGIN_DATA}[title]           
    Close Browser

    

*** Variables ***
${URL}     https://opensource-demo.orangehrmlive.com/  # SCALAR
@{CREDENTIALS}     Admin    admin123  # LIST
&{LOGIN_DATA}    title=OrangeHRM      # KEY_VALUE PAIRS 

*** Keywords ***
# Club built-in keyword actions. Enable reuse of same steps in multiple test cases
LOGINACTION
    Input Text    id=txtUsername    @{CREDENTIALS}[0]
    Input Password    id=txtPassword    @{CREDENTIALS}[1]
    Click Button    name=Submit 
