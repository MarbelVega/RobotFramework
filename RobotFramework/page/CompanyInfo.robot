*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Header Links
${lbl_CompanyInfo_CompanyInfo}    xpath=//*[text()='Company Information']


#Summary Tab
## Action Buttons
${btn_CompanyInfo_Summary_Delete}    xpath=//div[text()='Delete']

*** Keywords ***
Validate Company Name
    [Arguments]   ${expectedtxt}
    [Documentation]    Validates the expected value of the header text on the Company Information page 
    ...    DOES NOT VALIDATE THE TEXT SEEN NEXT TO COMPANY NAME FIELDS
    ...    .
    Element Should Be Visible    xpath=(//span[text()='${expectedtxt}'])[1]    Company ${expectedtxt} was not found.

Validate Company City
    [Arguments]    ${expectedtxt}
    [Documentation]    Validates the expected value of the 'City' field.
    ...    .
    Element Should Be Visible    xpath=//td//div[@class='Data' and text()='${expectedtxt}']