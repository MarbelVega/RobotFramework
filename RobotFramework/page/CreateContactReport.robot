*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Step 1
#Available Fields Contact
${btn_CreateContactReport_Fields_CompanyName}    xpath=//input[@id='Company']
${chkbx_CreateContactReport_Fields_BizState}    xpath=//input[@id='BusinessState' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgDiv}    xpath=//input[@id='CompanyDivisionName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgOffDiv}    xpath=//input[@id='CompanyOffDivDesc' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgOff}    xpath=//input[@id='CompanyOfficeName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgPrac}    xpath=//input[@id='CompanyPracticeAreaName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgStudio}    xpath=//input[@id='CompanyStudioName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_CoFirmOrgTerr}    xpath=//input[@id='CompanyTerritoryName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgDiv}    xpath=//input[@id='ContactDivision' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgOffDiv}    xpath=//input[@id='OffDivDesc' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgOff}    xpath=//input[@id='ContactOffice' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgPrac}    xpath=//input[@id='ContactPracticeArea' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgStudio}    xpath=//input[@id='ContactStudio' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FirmOrgTerr}    xpath=//input[@id='ContactTerritory' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_FName}    xpath=//input[@id='FirstName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_HomeState}    xpath=//input[@id='HomeState' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_LName}    xpath=//input[@id='LastName' and @type='Checkbox']
${chkbx_CreateContactReport_Fields_Status}    xpath=//input[@id='Status' and @type='Checkbox']

${chkbx_CreateContactReport_LimRelativeDate}    xpath=//input[@id='dateActionType_RelativeDate']

${chkbx_CreateContactReport_Fields_}    xpath=//input[@id='' and @type='Checkbox']

${btn_CreateContactReport_SaveContinue1}    xpath=//input[@name='ChooseFields']

##Step 2
${btn_CreateContactReport_SaveContinue2}    xpath=//input[@name='SelectCriteria']

##Step 3
${btn_CreateContactReport_SaveContinue3}    xpath=//input[@name='ChooseFields']

*** Keywords ***
Validate Contact Report Headers
    [Arguments]    ${text}
    [Documentation]    Validates that the expected Report headers exist by checking ${text}
    ...
    Wait Until Element Is Visible    xpath=//td//div[contains(text(), '${text}')]    60s    Report was not created or page did not load within 60s
    
Contact Select Where Filter By Name
    [Arguments]    ${index}    ${name}
    [Documentation]    Selects an option from WhereField${index} dropdown using ${name}
    ...    .
    #Click-Object    xpath=//select[@id='WhereField${index}']
    Click-Object    xpath=//select[@id='WhereField${index}']//option[text()='${name}']
    
Contact Select Operator By Text
    [Arguments]    ${index}    ${text}
    [Documentation]    Selects an option from WhereOperator${index} dropdown using ${text}
    ...    .
    #Click-Object    xpath=//select[@id='WhereOperator${index}']
    Click-Object    xpath=//select[@id='WhereOperator${index}']//option[text()='${text}']
    
Contact Enter-Text in Where Criteria by Index
    [Arguments]    ${index}    ${text}
    [Documentation]    Enters Text into Where by Criteria Field by ${index}
    Enter-Text    xpath=//input[@id='WhereValue${index}']    ${text}
    
Contact Select Relative Limit Date Period By Text
    [Arguments]    ${text}
    [Documentation]    Selects an option from Relative Date Period dropdown by Text (Ex: Day(s) )
    ...    .
    Click-Object    xpath=//select[@id='relDatePeriod']//option[text()='${text}']
    
#Step 2 Keywords    
Contact Select Sort Order Option By Name
    [Arguments]    ${index}    ${name}
    [Documentation]    Selects Sort Order Option from Dropdown by ${name} text under the ${index} field.
    ...    .
    Click-Object    xpath=//select[@id='OrderByField${index}']//option[contains(text(),'${name}')]
    
Contact Select Primary Grouping Option By Name
    [Arguments]    ${name}
    [Documentation]    Selects an option from Primary Grouping dropdown by ${name}
    ...    .
    Click-Object    xpath=//select[@id='primaryGroup']//option[contains(text(),'${name}')]