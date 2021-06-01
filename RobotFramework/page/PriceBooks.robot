*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***



*** Keywords **
Validate PriceBooks Name In Table
    [Arguments]    ${name}
    [Documentation]    Validates that a row exists in the table for Kits with ${name}
    ...    .
    Wait Until Element Is Visible    xpath=//div[@class='column-content']//a[text()='${name}']  
    