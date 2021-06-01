*** Settings ***
Library    SeleniumLibrary
Resource    ../../../PageObjs/Global/GlobalVariables.robot
#Resource    ../../../PageObjs/Global/GlobalKeywords.robot
Resource    ../../../../Universal/UniversalKeywords.robot

Library     ../../../../libraries/webDriverShortcuts.py
Library     ../../../../libraries/webdriver_sync.py

*** Variables ***
${txt_Admin_Login_UserName}    xpath=//input[@id='Username']
${txt_Admin_Login_Password}    xpath=//input[@id='Password']
${btn_Admin_Login}    xpath=//input[@value='Login']

${txt_Login_UserName}    xpath=//input[@id='username']
${txt_Login_Password}    xpath=//input[@id='password']
${txt_Login_Firm}    xpath=//input[@id='firmid']
${btn_Login}    xpath=//input[@value='Login']


${Login_User}    autotest
${Login_Password}    QAAuto123#@!
${Login_Firm}    919


#Staging: autouser/QC2EVKHP6zs8buE2^pBrNXtz/822
#QA: sprintuser/Devaccount123!/1
#QE: emason/w3lcom3/822

#919 For Automation 03/30 
#Firm 919 for Staging = ccarmichael/QAAuto123#@!

*** Keywords ***
AdminLogin    
    [Arguments]    ${URL}    ${User}    ${Pass}   ${download directory}=default   ${is_headless}=False
    [Documentation]    Generic Keyword to handle logging into the application
    ...    Pass in desired URL, Username, and Password.
    
    # Set a download directory for files to go to.
    ${capabilities}=  set chrome capabilities  ${download directory}  ${is_headless}
    # Get our chromedriver's path, so we don't have to rely on manually updating it.
    ${driver_path}=  chromedriver path
    # Open the browser with the above options, then perform the login.
    Open Browser    ${URL}    chrome  desired_capabilities=${capabilities}  executable_path=${driver_path}
    Maximize Browser Window
    Input Text    ${txt_Admin_Login_UserName}    ${User}
    Input Text    ${txt_Admin_Login_Password}    ${Pass}
    Click-Object    ${btn_Admin_Login}
    
CustLogin
    [Arguments]    ${URL}    ${User}    ${Pass}    ${Firm}  ${download directory}=default  ${is_headless}=False
    [Documentation]    Generic Keyword to handle logging into the application
    ...    Pass in desired URL, Username, and Password.
    # Set a download directory for files to go to.
    ${capabilities}=  set chrome capabilities  ${download directory}  ${is_headless}
    # Get our chromedriver's path, so we don't have to rely on manually updating it.
    ${driver_path}=  chromedriver path
    # Open the browser with the above options, then perform the login.
    Open Browser    ${URL}    chrome  desired_capabilities=${capabilities}  executable_path=${driver_path}
    Maximize Browser Window
    Enter-Text    ${txt_Login_UserName}    ${User}
    Enter-Text     ${txt_Login_Password}    ${Pass}
    Enter-Text     ${txt_Login_Firm}    ${Firm}
    Click-Object    ${btn_Login}
    Wait Until Element Is Visible    ${GlobalNav_Home}   30s    Home Page Did Not Load.
    
Login-WebApp
    [Arguments]    ${URL}  ${download directory}=default  ${is_headless}=False
    [Documentation]    Login Keyword - Only need to pass in URL as User/Pass/Firm are all static across env.
    ...    
    # Set a download directory for files to go to.
    ${capabilities}=  set chrome capabilities  ${download directory}  ${is_headless}
    # Get our chromedriver's path, so we don't have to rely on manually updating it.
    ${driver_path}=  chromedriver path
    # Open the browser with the above options, then perform the login.
    Open Browser    ${URL}    chrome  desired_capabilities=${capabilities}  executable_path=${driver_path}
    Maximize Browser Window
    Enter-Text    ${txt_Login_UserName}    ${Login_User}
    Enter-Text     ${txt_Login_Password}    ${Login_Password}
    Enter-Text     ${txt_Login_Firm}    ${Login_Firm}
    Click-Object    ${btn_Login}
    Wait Until Element Is Visible    ${GlobalNav_Home}   30s    Home Page Did Not Load.