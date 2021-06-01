*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Headers
${lbl_Opportunity_HeaderTxt}    xpath=//span[contains(text(), 'Opportunities')]

#Grid
##First Row Elements
${btn_Opportunity_Grid_1stRow_MenuButton}    xpath=(//img[@src='/images/arrow_default.gif']/parent::div)[1]
${txt_Opportunity_Grid_1stRow_Comments}    xpath=(//div[@class='x-grid3-cell-inner x-grid3-col-TXCOMMENTS x-unselectable'])[1]

##Grid Actions
${btn_Opportunity_Grid_Actions_Refresh}    xpath=//button[@id='ext-gen90']

##Grid Menu Actions
${btn_Opp_GridMenu_OppDetails}    xpath=//span[text()='Opportunity Details']

*** Keywords ***
Validate Opportunity Name
    [Arguments]    ${name}
    [Documentation]    Validates the Opportunity Name next to the field in the Opportunity Summary Information section.
    ...    .
    Wait Until Element Is Visible    xpath=//div[@class='DataBold' and text()='${name}']    60s    Personnel ${name} did not display after 60s.