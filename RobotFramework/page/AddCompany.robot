*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***
${txt_AddCo_Name}    xpath=//input[@id='NewCompanyName']

#Address Section
${txt_AddCo_Address1}    xpath=//input[@name='Address1']
${txt_AddCo_City}    xpath=//input[@name='City']
${slt_AddCo_Country}    xpath=//select[@id='Country']
${slt_AddCo_State}    xpath=//select[@id='stateOptions']
${txt_AddCo_Phone}    xpath=//input[@name='OfficePhone']
${txt_AddCo_Website}    xpath=//input[@name='OfficeURL']

${btn_AddCo_Save}    xpath=//input[@id='submit']

*** Keywords ***
Select Company State
    [Arguments]    ${name}
    [Documentation]    Selects a State from the dropdown by ${name}
    ...    .
    Click-Object    ${slt_AddCo_State}//option[text()='${name}']
    
Select Company Country
    [Arguments]    ${name}
    [Documentation]    Selects a Country from the dropdown by ${name}
    ...    .
    Click-Object    ${slt_AddCo_Country}//option[contains(text(),'${name}')]