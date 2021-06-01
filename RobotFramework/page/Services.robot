*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***



*** Keywords **
Validate Service Name In Table
    [Arguments]    ${name}
    [Documentation]    Validates that a row exists in the table for service with ${name}
    ...    .
    Wait Until Element Is Visible    xpath=//div[@class='column-content']//a[text()='${name}']  
    
