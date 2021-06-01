*** Settings ***
Library    SeleniumLibrary

*** Variables ***
#Header
${lbl_PersonnelSumm_Header}    xpath=//div[text()='Personnel Information']

#Actions
${btn_PersonnelSumm_Delete}    xpath=//div[contains(text(), 'Delete')]
${btn_PersonnelSumm_MakeUser}    xpath=//div[contains(text(), 'Make User')]

#Convert Personnel To A User Pop-Up
${ConvertPersonnelPopUp}    xpath=(//div[@class='modal-content'])[1]

##Email Request
${txt_PersonnelSumm_Pop_Email}    xpath=//input[@id='ofcEmail']
${btn_PersonnelSumm_Pop_Next}    xpath=//button[@id='next-button']

##Group Request
${btn_PersonnelSumm_Pop_ReadOnlyGroup}    xpath=(//div[@id='groupList']//input[@type='radio'])[1]
${btn_PersonnelSumm_Pop_FORG}    xpath=(//div[@id='groupList']//input[@type='radio'])[1]
${btn_PersonnelSumm_Pop_RegUsers}    xpath=(//div[@id='groupList']//input[@type='radio'])[2]
${btn_PersonnelSumm_Pop_ConvertSend}    xpath=//button[@id='convert-user-and-send']
${btn_PersonnelSumm_Pop_Convert}    xpath=//button[@id='create-user']


*** Keywords ***
Validate Employee Name
    [Arguments]    ${name}
    [Documentation]    Validates the Employee Name next to the field in the Employee Information section.
    ...    .
    Wait Until Element Is Visible    xpath=//div[text()=' ${name} ']    60s    Personnel ${name} did not display after 60s.