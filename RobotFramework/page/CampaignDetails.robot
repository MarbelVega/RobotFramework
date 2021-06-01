*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${btn_CampaignDetails_RsltsDrop}    xpath=//button[@data-toggle='dropdown']
${btn_CampaignDetails_RsltsDrop_Delete}    xpath=//li//a[text()='Delete']

#Delete Confirmation
${btn_CampaignDetails_DelConf_Delete}    xpath=//button[text()='Delete']

*** Keywords ***
Check Campaign Name
    [Arguments]    ${name}
    [Documentation]    Checks the Campaign ${name}
    ...    .
    Wait Until Element Is Visible    xpath=//td[text()='${name}']    60s    ${name} Campaign did not get created or Details page did not load