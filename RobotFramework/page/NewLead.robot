*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***
${lbl_NewLead_LeadDetailHeader}    xpath=//div[text()='Lead Detail']
${btn_NewLead_Save}    xpath=//div[@id='submit' and text()='Save']

${txt_NewLead_Name}    xpath=//input[@id='oppLeadName']
${txt_NewLead_PotentialClient}    xpath=//input[@type='search' and @id='companyName']
${txt_NewLead_OrgDate}    xpath=//input[@id='oppDate']
${slt_NewLead_RecSource}    xpath=//select[@id='oppLeadCreateMethodID']
${slt_NewLead_LeadSource}    xpath=//select[@id='oppLeadSourceID']
${slt_NewLead_Stage}    xpath=//select[@id='oppLeadStatus']
${slt_NewLead_Score}    xpath=//select[@id='oppLeadScoreID']
${txt_NewLead_TicklerDate}    xpath=//input[@id='oppTickDate']
${txt_NewLead_BidDate}    xpath=//input[@id='bidDate']
${txt_NewLead_EstCost}    xpath=//input[@id='EstimatedCost']
${txt_NewLead_City}    xpath=//input[@id='City']
${slt_NewLead_Country}    xpath=//select[@name='CountryID']
${slt_NewLead_State}    xpath=//select[@id='StateID']
${txt_NewLead_Email}    xpath=//input[@id='Email']
${txt_NewLead_Phone}    xpath=//input[@id='Phone']
${txt_NewLead_FName}    xpath=//input[@id='contactfirst']
${txt_NewLead_LName}    xpath=//input[@id='contactlast']
${txt_NewLead_NextAct}    xpath=//input[@id='oppLeadNextAction']

#Potential Client Company Search Results Dropdown
## This is bad Xpath. Objects with class CLFItemContainer need Automation Hooks. 
${btn_NewLead_PCSearch_1stRslt}    xpath=(//div[@class='Data']//div[@class='CLFItemContainer'])[1]

##Notes is an iFrame and requires some extra steps in order to type into it.
${frame_NewLead_Notes}    xpath=//iframe
${txt_NewLead_Notes_TypeBox}    xpath=//body[contains(@class,'cke_editable')]//p

*** Keywords ***
Select Resource Source
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Resource Source dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_RecSource}
    Click-Object    xpath=//select[@id='oppLeadCreateMethodID']//option[contains(text(),'${text}')]
    
Select Lead Source
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Lead Source dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_LeadSource}
    Click-Object    xpath=//select[@id='oppLeadSourceID']//option[contains(text(),'${text}')]
    
Select Stage
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Stage dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_Stage}
    Click-Object    xpath=//select[@id='oppLeadStatus']//option[text()='${text}']
    
Select Score
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Score dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_Score}
    Click-Object    xpath=//select[@id='oppLeadScoreID']//option[contains(text(),'${text}')]
    
Select Country
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Country dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_Country}
    Click-Object    xpath=//select[@name='CountryID']//option[text()='${text}']
    
Select State
    [Arguments]    ${text}
    [Documentation]    Selects an option from the Country dropdown by ${text}
    ...
    Click-Object    ${slt_NewLead_State}
    Click-Object    xpath=//select[@id='StateID']//option[text()='${text}']