*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Step 1
#Available Fields Lead
${btn_CreateLeadReport_Fields_LeadType}    xpath=//input[@id='leadTypeName']
${chkbx_CreateLeadReport_Fields_City}    xpath=//input[@id='city' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgDiv}    xpath=//input[@id='DivisionName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgOffDiv}    xpath=//input[@id='OffDivDesc' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgOff}    xpath=//input[@id='OfficeName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgPrac}    xpath=//input[@id='PracticeAreaName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgStudio}    xpath=//input[@id='StudioName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_FirmOrgTerr}    xpath=//input[@id='TerritoryName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_LeadName}    xpath=//input[@id='oppLeadName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_LeadStage}    xpath=//input[@id='oppLeadStageName' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_LeadStatus}    xpath=//input[@id='oppLeadStatus' and @type='Checkbox']
${chkbx_CreateLeadReport_Fields_OppTickDate}    xpath=//input[@id='oppTickDate' and @type='Checkbox']



${chkbx_CreateLeadReport_Fields_}    xpath=//input[@id='' and @type='Checkbox']

${chkbx_CreateLeadReport_RelativeDate}    xpath=//input[@id='dateActionType_RelativeDate']

${btn_CreateLeadReport_SaveContinue1}    xpath=//input[@name='ChooseFields']

##Step 2
${btn_CreateLeadReport_SaveContinue2}    xpath=//input[@name='ChooseFields']

*** Keywords ***
Validate Lead Report Headers
    [Arguments]    ${text}
    [Documentation]    Validates that the expected Report headers exist by checking ${text}
    ...
    Wait Until Element Is Visible    xpath=//td//div[contains(text(), '${text}')]    60s    Report was not created or page did not load within 60s
    
Lead Select Where Filter By Name
    [Arguments]    ${index}    ${name}
    [Documentation]    Selects an option from WhereField${index} dropdown using ${name}
    ...    .
    #Click-Object    xpath=//select[@id='WhereField${index}']
    Click-Object    xpath=//select[@id='WhereField${index}']//option[text()='${name}']
    
Lead Select Operator By Text
    [Arguments]    ${index}    ${text}
    [Documentation]    Selects an option from WhereOperator${index} dropdown using ${text}
    ...    .
    #Click-Object    xpath=//select[@id='WhereOperator${index}']
    Click-Object    xpath=//select[@id='WhereOperator${index}']//option[text()='${text}']
    
Lead Enter-Text in Where Criteria by Index
    [Arguments]    ${index}    ${text}
    [Documentation]    Enters Text into Where by Criteria Field by ${index}
    Enter-Text    xpath=//input[@id='WhereValue${index}']    ${text}
    
Lead Select Relative Limit Date Period By Text
    [Arguments]    ${text}
    [Documentation]    Selects an option from Relative Date Period dropdown by Text (Ex: Day(s) )
    ...    .
    Click-Object    xpath=//select[@id='relDatePeriod']//option[text()='${text}']
    
#Step 2 Keywords    
Lead Select Sort Order Option By Name
    [Arguments]    ${index}    ${name}
    [Documentation]    Selects Sort Order Option from Dropdown by ${name} text under the ${index} field.
    ...    .
    Click-Object    xpath=//select[@id='OrderByField${index}']//option[contains(text(),'${name}')]
    
Lead Select Primary Grouping Option By Name
    [Arguments]    ${name}
    [Documentation]    Selects an option from Primary Grouping dropdown by ${name}
    ...    .
    Click-Object    xpath=//select[@id='primaryGroup']//option[contains(text(),'${name}')]