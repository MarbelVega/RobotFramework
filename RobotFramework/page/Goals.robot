*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${btn_Goals_NewGoal}    xpath=//button[text()='New Goal']

#New Goal Popup
#${ddn_NewGoal_Type}    xpath=//input[@name='goaltypes']/parent::div
#//div[@class=' x-form-text x-form-field x-form-empty-field x-trigger-noedit']
${txt_NewGoal_Type_SalesGoal}    xpath=//input[@name='goaltypes']/following::input[1]
${ddn_NewGoal_Type_SalesGoal}    xpath=//div[@class='x-combo-list-item x-combo-selected'][1]

${txt_NewGoal_DfltMonthlyGoal}    xpath=//input[@name='defaultMonthlyValue']
${chkbx_NewGoal_Company}    xpath=//input[@name='company_enabled']
${txt_NewGoal_Comapny}    xpath=//input[@name='companyId']/following::input[1]
${lbl_NewGoal_Comapny_FirstRslt}    xpath=//div[@class='x-layer x-combo-list '][contains(@style,'visibility: visible')]
${btn_NewGoal_CreateGoal}    xpath=//button[text()='Create Goal(s)']