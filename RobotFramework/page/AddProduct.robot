*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${txt_AddProduct_Name}    xpath=//input[@id='name']

#Index Tab
${btn_AddProduct_ProductTab}    xpath=//a[contains(@href,'/products/index.cfm') and text()='Products'] 
#Action Buttons
${btn_AddProduct_Cancel}    xpath=//a[text()='Cancel']
${btn_AddProduct_Save}    xpath=(//input[@value='Save'])[2]
${btn_AddProduct_SaveNew}    xpath=//input[@value='Save and New']

#Details Section
${txt_AddProduct_Manufacturer}    xpath=//input[@id='manufacturer']

${btn_AddPRoduct_ManufacturerFirstRow}    xpath=//div[@class='tt-menu tt-open']//div

${slt_AddProduct_Unit}    xpath=//select[@id='unit']
${txt_AddProduct_ProdAbbrev}    xpath=//input[@id='abbreviation']
${txt_AddProduct_UnitCost}    xpath=//input[@id='unitcost']
${txt_AddProduct_Desc}    xpath=//textarea[@id='description']
${txt_AddProduct_UnitPrice}    xpath=//input[@id='price']
${txt_AddProduct_ProdSKU}    xpath=//input[@id='skunumber']
${slt_AddProduct_BillCycle}    xpath=//select[@id='billingcycle']
${txt_AddProduct_ProdCode}    xpath=//input[@id='productcode']
${slt_AddProduct_GLAcc}    xpath=//select[@id='glaccount']
${slt_AddProduct_Type}    xpath=//select[@id='type']
${slt_AddProduct_SLA}    xpath=//select[@id='sla']
${slt_AddProduct_Family}    xpath=//select[@id='family']
${txt_AddProduct_WarrantyTerm}    xpath=//input[@id='warranty']
${slt_AddProduct_WarrantyUnit}    xpath=//select[@id='warrantyunit']
${txt_AddProduct_Commission}    xpath=//input[@id='commission']
${slt_AddProduct_Status}    xpath=//select[@id='status']
${slt_AddProduct_Discounts}    xpath=//select[@id='isdiscountable']

#Product Details
${iframe_AddProducts_ProdDetailsFrame}    xpath=//iframe[@id='details_ifr']
${txt_AddProduct_ProdDetails}    xpath=//body[@id='tinymce']//p

#Firm Orgs
${btn_AddProduct_AddOffice}    xpath=(//button//span[text()='Add'])[1]
${btn_AddProduct_AddPractArea}    xpath=(//button//span[text()='Add'])[4]
${btn_AddProduct_AddDivs}    xpath=(//button//span[text()='Add'])[2]
${btn_AddProduct_AddTerrs}    xpath=(//button//span[text()='Add'])[5]
${btn_AddProduct_AddStudios}    xpath=(//button//span[text()='Add'])[3]

##Firm Orgs Dropdown Menu Buttons
${btn_AddProduct_FirmOrgs_Save}    xpath=//div[@class='pull-right']//button[text()='Save']

${_AddProduct_}    xpath=//select[@id='']

*** Keywords ***
Select From Dropdown By Text
    [Arguments]    ${loc}    ${text}
    [Documentation]    Selects an option from ${loc} dropdown by ${text}
    ...    org.
    Click-Object    ${loc}//option[text()='${text}']
    
Select Firm Org By Text
    [Arguments]    ${loc}    ${text}    
    [Documentation]    Clicks the Add button ${loc} and then selects the option based on ${text}
    ...    org.
    Click-Object    ${loc}
    Sleep    1
    Click-Object    xpath=//span[contains(text(),'${text}')]
    Click-Object    ${btn_AddProduct_FirmOrgs_Save}
    Sleep    1
