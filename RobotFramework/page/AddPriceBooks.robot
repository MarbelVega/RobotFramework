*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Price Books main tab
${btn_PB_Tab}    xpath=//a[contains(@href,'#pricebooks') and text()='Price Books'] 
${btn_PB_IndexTab}    xpath=//a[contains(@href,'#pricebooks') and text()='Price Books'] 

#Add Price Books button
${btn_Products_AddPB}    xpath=//button[text()='Add Price Books']

# Enter Price Book Name
${txt_AddPB_Name}    xpath=//input[@id='name']

#Action Buttons
${btn_AddPB_Cancel}    xpath=//a[text()='Cancel']
${btn_AddPB_Save}    xpath=//input[@value='Save']
${btn_AddPB_SaveNew}    xpath=//input[@value='Save and New']

#Details Section
${txt_AddPB_CustomerName}    xpath=//input[@id='customername']
${txt_AddPB_Desc}    xpath=//textarea[@id='description']
${txt_AddPB_Commission}    xpath=//input[@id='commissionadjustment']
${txt_AddPB_ListPriceAdjustment}    xpath=//input[@id='priceAdjustment']


*** Keywords ***
Select From Dropdown By Text_PriceBooks
    [Arguments]    ${loc}    ${text}
    [Documentation]    Selects an option from ${loc} dropdown by ${text}
    ...    .
    Click-Object    ${loc}//option[text()='${text}']
   
    

