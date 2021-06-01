*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***

#Grid Elements
${tbl_Company_Table}    xpath=//table
${btn_Company_Add}    xpath=//img[contains(@src, 'addcompany')]

#Starts With Letting Filters:
${btn_Company_StartsA}    xpath=//a[@title='Quick Alpha Search' and text()='A']

*** Keywords ***
Validate Company Exists
    [Arguments]    ${companyname}
    [Documentation]    Validates that a company exists in the table.
    ...    This Keyword simply searches for the company name. If the searched text is included in another company name this keyword will fail.
    ...    May Need Enhancements
    ...
    Wait Until Element Is Visible    xpath=//a[contains(text(), '${companyname}')]    30s    Company ${companyname} did not appear in the grid.
    
Validate Company Does Not Exist
        [Arguments]    ${companyname}
    [Documentation]    Validates that a company doesn't exist in the table.
    ...    This Keyword simply searches for the company name. If the searched text is included in another company name this keyword will fail.
    ...    May Need Enhancements
    ...
    Element Should Not Be Visible    xpath=//a[contains(text(), '${companyname}')]    Company ${companyname} appeared in the grid but should not.

Open Company
    [Arguments]    ${companyname}
    [Documentation]    Opens the Company Record by Name
    Click-Object    xpath=//a[@class='LinkSmall' and text()='${companyname}']