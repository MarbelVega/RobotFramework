*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${txt_CreateCampaign_Name}    xpath=//input[@id='name']
${slt_CreateCampaign_Status}    xpath=//select[@id='campaignstatusid']
${btn_CreateCampaign_Save}    xpath=//input[@type='submit']