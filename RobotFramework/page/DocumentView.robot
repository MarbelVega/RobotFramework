*** Settings ***
Library    SeleniumLibrary
Resource    ../../Global/GlobalKeywords.robot

*** Variables ***
${btn_DocView_Delete}    xpath=//img[contains(@src, 'delete')]

*** Keywords ***
Check Resume Name
    [Arguments]    ${name}
    [Documentation]    Checks the Resume Name field by ${name} value.
    ...
    Wait Until Element Is Visible    xpath=//td//div[text()='${name}']
    #TODO - Add Validation error text