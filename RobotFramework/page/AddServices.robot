*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Services main tab
${btn_Services_Tab}    xpath=//a[contains(@href,'#services') and text()='Services'] 
${btn_Services_IndexTab}    xpath=//a[contains(@href,'#services') and text()='Services'] 

#Add Services button
${btn_Products_AddServices}    xpath=//button[text()='Add Services']

# Enter Service Name
${txt_AddServices_Name}    xpath=//input[@id='name']

#Action Buttons
${btn_AddServices_Cancel}    xpath=//a[text()='Cancel']
${btn_AddServices_Save}    xpath=//input[@value='Save']
${btn_AddServices_SaveNew}    xpath=//input[@value='Save and New']

#Details Section
${slt_AddServices_Unit}    xpath=//select[@id='unit']
${txt_AddServices_ServAbbrev}    xpath=//input[@id='abbreviation']
${txt_AddServices_UnitCost}    xpath=//input[@id='unitcost']
${txt_AddServices_Desc}    xpath=//textarea[@id='description']
${txt_AddServices_UnitPrice}    xpath=//input[@id='price']
${txt_AddServices_ServSKU}    xpath=//input[@id='skunumber']
${slt_AddServices_BillCycle}    xpath=//select[@id='billingcycle']
${txt_AddServices_ServiceCode}    xpath=//input[@id='servicecode']
${slt_AddServices_GLAcc}    xpath=//select[@id='glaccount']
${slt_AddServices_Type}    xpath=//select[@id='type']
${slt_AddServices_SLA}    xpath=//select[@id='sla']
${slt_AddServices_Family}    xpath=//select[@id='family']
${txt_AddServices_WarrantyTerm}    xpath=//input[@id='warranty']
${slt_AddServices_WarrantyUnit}    xpath=//select[@id='warrantyunit']
${txt_AddServices_Commission}    xpath=//input[@id='commission']
${slt_AddServices_Status}    xpath=//select[@id='status']
${slt_AddServices_Discounts}    xpath=//select[@id='isdiscountable']



#Firm Orgs
${btn_AddServices_AddOffice}    xpath=(//button//span[text()='Add'])[1]
${btn_AddServices_AddPractArea}    xpath=(//button//span[text()='Add'])[4]
${btn_AddServices_AddDivs}    xpath=(//button//span[text()='Add'])[2]
${btn_AddServices_AddTerrs}    xpath=(//button//span[text()='Add'])[5]
${btn_AddServices_AddStudios}    xpath=(//button//span[text()='Add'])[3]

##Firm Orgs Dropdown Menu Buttons
${btn_AddServices_FirmOrgs_Save}    xpath=//div[@class='pull-right']//button[text()='Save']

${_AddServices_}    xpath=//select[@id='']

*** Keywords ***
Select From Dropdown By Text_Services
    [Arguments]    ${loc}    ${text}
    [Documentation]    Selects an option from ${loc} dropdown by ${text}
    ...    .
    #Click-Object    ${loc}//option[text()='${text}']
    Click-Object    ${loc}//option[2]
    
Select Firm Org By Text_Services
    [Arguments]    ${loc}    ${text}    
    [Documentation]    Clicks the Add button ${loc} and then selects the option based on ${text}
    ...    .
    Click-Object    ${loc}
    Sleep    1
    Click-Object    xpath=//span[contains(text(),'${text}')]
    Click-Object    ${btn_AddProduct_FirmOrgs_Save}
    Sleep    1
