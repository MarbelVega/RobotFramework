*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${btn_Products_AddProd}    xpath=//button[text()='Add Products']


*** Keywords **
Validate Product Name In Table
    [Arguments]    ${name}
    [Documentation]    Validates that a row exists in the table for product with ${name}
    ...    .
    Wait Until Element Is Visible    xpath=//div[@class='column-content']//a[text()='${name}']   