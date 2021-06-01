*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Header Navigation
${lnk_ProjSumm_ProjSumm}    xpath=//td[text()='Project Summary']

#Project Summary Information Section

${btn_ProjSumm_EditAll}    xpath=//img[contains(@src, 'editall')]

*** Keywords ***
Validate Project Name
    [Arguments]    ${name}
    [Documentation]    Validates the Project Name next to the field in the Project Summary Information section.
    ...    .
    Wait Until Element Is Visible    xpath=//div[text()='${name}']    60s    Personnel ${name} did not display after 60s.