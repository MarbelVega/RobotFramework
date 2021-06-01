*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***



*** Keywords **
Validate Labor Name In Table
    [Arguments]    ${name}
    [Documentation]    Validates that a row exists in the table for Labor with ${name}
    ...    .
    Wait Until Element Is Visible    xpath=//div[@class='column-content']//a[text()='${name}']  
    
