*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***
${btn_LeadInfo_ConvToOp}    xpath=//button[@id='btnConvertToOpportunity']
${btn_LeadInfo_Delete}    xpath=//div[text()='Delete Lead']

*** Keywords ***
Validate Lead Name
    [Arguments]    ${name}
    [Documentation]    Validates the Lead Name next to the field in the Lead Deatil section.
    ...    .
    Wait Until Element Is Visible    xpath=//td[@class='cell_data0' and text()='${name}']   60s    Laed ${name} did not display after 60s.
    
Click Converted to Opp Link
    [Arguments]    ${name}
    [Documentation]    Clicks the ${name} link in the Stage field for Lead that has been Converted to Opportunity.
    ...    .
    Click-Object    xpath=//a[contains(@href,'lead_view.cfm') and text()='${name}']
    
Open Company by Name
    [Arguments]    ${name}
    [Documentation]    Clicks the link to the Company Profile by the ${name}
    ...    .
    Click-Object    xpath=//td//a[text()='${name}']