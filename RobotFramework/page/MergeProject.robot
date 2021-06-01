*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${lbl_ProjMerge_SuccessMsg}    xpath=//*[text()='Succesfully Updated.']

${txt_ProjMerge_ProjToMerge}    xpath=//input[@id='ProjectName']
${txt_ProjMerge_MergeInto}    xpath=//input[@id='Project_MergName']
${btn_ProjMerge_Save}    xpath=//input[@name='AddButton']

*** Keyword ***
Select Merge Option By Text
    [Arguments]    ${text}
    [Documentation]    Selects row from Auto Complete dropdown by ${text}
    ...
    #Wait Until Element Is Visible    xpath=(//div[contains(@data-row, '${text}') and @class='CLFItemContainer'])[1]    60s    No Options Display in Predict Text Dropdown
    Wait Until Element Is Visible    xpath=//div[@class='CLFListItem']//*[text()='${text}']
	Click-Object    xpath=//div[@class='CLFListItem']//*[text()='${text}']