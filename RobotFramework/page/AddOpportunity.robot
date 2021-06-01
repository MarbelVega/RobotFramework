*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Opportunity Metrics
##LABELS
${lbl_AddOpp_EstCost}    xpath=//div[text()='ESTIMATED COST:']
${lbl_AddOpp_TotalEstFee}    xpath=

*** Keywords ***
Validate Required Opp Fields
    [Arguments]    ${loc}
    [Documentation]    Validates that the expected field (${loc}) is a required field.
    Wait Until Element Is Visible    ${loc}/parent::td[contains(concat(' ', @class, ' '), 'DataLabelCellRequired')]    30    Expected Element was not set as a Required FIeld or Page did not load.
    
Validate Opp Fields Not Required
    [Arguments]    ${loc}
    [Documentation]    Validates that the expected field (${loc}) is a required field.
    Page Should Not Contain Element    ${loc}/parent::td[contains(concat(' ', @class, ' '), 'DataLabelCellRequired')]    30    Expected Element was not set as a Required FIeld or Page did not load.