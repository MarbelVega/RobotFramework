*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***
${btn_OppSum_AddOpp}    xpath=//a[@class='button pending AddOppBtn']
${btn_OppSum_AddOpp_CosDflt}    xpath=//li[text()='Default']

*** Keywords ***
Validate Lead Conversion
    [Arguments]    ${name}
    [Documentation]    Uses Lead ${name} to validate that text showing conversion was successul displays.
    ...    .
    #Wait Until Element Is Visible    xpath=//div[@id='topButtonsSection' and contains(text(),'Converted from a Lead')]    30    Lead Conversion Text did not display.
    Wait Until Element Is Visible    xpath=//div[@id='topButtonsSection']//a[text()='${name}']    30    Lead Conversion Text did not display.
    
Opp - Open Company by Name
    [Arguments]    ${name}
    [Documentation]    Uses Company ${name} to open the link to the company page.
    ...    .
    Click-Object    xpath=//td//a[text()='${name}']
    
Validate Owner Text
    [Arguments]    ${text}
    [Documentation]    Uses ${text} to Validate the value in the Owner field.
    ...    .
    Wait Until Element Is Visible    xpath=//*[text()='${text}']