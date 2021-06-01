*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${txt_Contact_Srch}    xpath=(//table[@class='x-table-layout']//input[@type='text'])[1]
${btn_Contact_NewContact}    xpath=//button[text()='New Contact']

#Search Results
${btn_Contact_FrstRslt}    xpath=(//div[contains(@class, 'x-grid3-col-contactid')])[1]


#Search Results Menu List Options
#${btn_Contact_ContactDetails}    xpath=(//span[contains(text(), 'Contact details')])[3]
#${btn_Contact_ContactDetails}    xpath=(//img[@src='/images/icons/16/Contact.png'])[4]
${btn_Contact_ContactDetails}    xpath=//span[text()='Contact details: Automation Testing']

*** Keywords ***
Wait For Contact to Load in Search
    [Arguments]    ${criteria}
    [Documentation]    Waits for Lead Search Results to Load by waiting for the Lead Name element to exist with ${criteria} as text
    ...
    Wait Until Element Is Visible    xpath=//div[contains(text(), '${criteria}')]    30    Expected Lead Result did not load.