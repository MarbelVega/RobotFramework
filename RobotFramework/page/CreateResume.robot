*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${txt_CreateResume_Name}    xpath=//input[@name='DocumentName']
${txt_CreateResume_Personnel}    xpath=//input[@name='PersonnelName']

${btn_CreateResume_Save}    xpath=//input[@name='addDocument']

*** Keywords ***
Select Row By Name
    [Arguments]    ${name}
    [Documentation]    Selects row from auto-complete dropdown by ${name}
    ...    .
    Click-Object    xpath=//div[@class='CLFListItem personnelStatusActive']//*[text()='${name}']