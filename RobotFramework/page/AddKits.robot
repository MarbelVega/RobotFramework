*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Kits main tab
${btn_Kits_Tab}    xpath=//a[contains(@href,'#kits') and text()='Kits'] 
${btn_Kits_IndexTab}    xpath=//a[contains(@href,'#kits') and text()='Kits'] 

#Add Kits button
${btn_Products_AddKits}    xpath=//button[text()='Add Kits']

# Enter Service Name
${txt_AddKits_Name}    xpath=//input[@id='name']

#Action Buttons
${btn_AddServices_Cancel}    xpath=//a[text()='Cancel']
${btn_AddServices_Save}    xpath=//input[@value='Save']
${btn_AddServices_SaveNew}    xpath=//input[@value='Save and New']

#Details Section
${txt_AddKits_KitAbbrev}    xpath=//input[@id='abbreviation']
${txt_AddKits_Desc}    xpath=//textarea[@id='description']
${txt_AddKits_KitsSKU}    xpath=//input[@id='skunumber']
${txt_AddKits_KitsCode}    xpath=//input[@id='kitcode']  
${slt_AddKits_Type}    xpath=//select[@id='type']
${slt_AddKits_Family}    xpath=//select[@id='family']
${txt_AddKits_Commission}    xpath=//input[@id='commission']
${txt_AddKits_KitPrice}    xpath=//input[@id='price']
${slt_AddKits_SLA}    xpath=//select[@id='sla']
${slt_AddKits_BillCycle}    xpath=//select[@id='billingcycle']
${txt_AddKits_ProductWarrantyTerm}    xpath=//input[@id='pwarranty']
${slt_AddKits_ProductWarrantyunit}    xpath=//select[@id='pwarrantyunit']
${txt_AddKits_ServiceWarrantyTerm}    xpath=//input[@id='swarranty']
${slt_AddKits_ServiceWarrantyunit}    xpath=//select[@id='swarrantyunit']
${txt_AddKits_LaborWarrantyTerm}    xpath=//input[@id='lwarranty']
${slt_AddKits_LaborWarrantyunit}    xpath=//select[@id='lwarrantyunit']
${slt_AddKits_Status}    xpath=//select[@id='status']
${slt_AddKits_Discounts}    xpath=//select[@id='isdiscountable']

#Firm Orgs
${btn_AddKits_AddOffice}    xpath=(//button//span[text()='Add'])[1]
${btn_AddKits_AddPractArea}    xpath=(//button//span[text()='Add'])[4]
${btn_AddKits_AddDivs}    xpath=(//button//span[text()='Add'])[2]
${btn_AddKits_AddTerrs}    xpath=(//button//span[text()='Add'])[5]
${btn_AddKits_AddStudios}    xpath=(//button//span[text()='Add'])[3]

##Firm Orgs Dropdown Menu Buttons
${btn_AddServices_FirmOrgs_Save}    xpath=//div[@class='pull-right']//button[text()='Save']

${_AddServices_}    xpath=//select[@id='']

*** Keywords ***
Select From Dropdown By Text_Kits
    [Arguments]    ${loc}    ${text}
    [Documentation]    Selects an option from ${loc} dropdown by ${text}
    ...    .
    Click-Object    ${loc}//option[text()='${text}']
   
    
Select Firm Org By Text_Kits
    [Arguments]    ${loc}    ${text}    
    [Documentation]    Clicks the Add button ${loc} and then selects the option based on ${text}
    ...    .
    Click-Object    ${loc}
    Sleep    1
    Click-Object    xpath=//span[contains(text(),'${text}')]
    Click-Object    ${btn_AddProduct_FirmOrgs_Save}
    Sleep    1
