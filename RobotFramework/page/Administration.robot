*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Top Navigation Menu
${lnk_Admin_ValueLists}    xpath=//td[text()='Value Lists']
${lnk_Admin_FirmSetup}    xpath=//td[text()='Firm Setup']
${lnk_Admin_Workflow}    xpath=//td[text()='Work Flow 2.0']