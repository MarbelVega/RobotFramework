*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${btn_Personnel_Add}    xpath=//input[contains(@src, 'addpersonnel')]
${lnk_Personnel_StartsA}    xpath=//div[@class='SectionHeader']//a[text()='A']
${lnk_Personnel_StartsT}    xpath=//div[@class='SectionHeader']//a[text()='T']

*** Keywords ***
Validate Personnel Exists
    [Arguments]    ${LName}
    [Documentation]    Validates that a Personnel row exists in the table.
    ...    This Keyword simply searches for the Personnel's Last name. If the searched text is included in another company name this keyword will fail.
    ...    May Need Enhancements
    ...
    Wait Until Element Is Visible    xpath=//div//a[text()='${LName}']    30s    Personnel with Last Name ${LName} did not appear in the grid.

Validate Personnel Does Not Exist
    [Arguments]    ${LName}
    [Documentation]    Validates that a Personnel row exists in the table.
    ...    This Keyword simply searches for the Personnel's Last name. If the searched text is included in another company name this keyword will fail.
    ...    May Need Enhancements
    ...
    Element Should Not Be visible    xpath=//div//a[text()='${LName}']    Personnel with Last Name ${LName} appeared in the grid.
