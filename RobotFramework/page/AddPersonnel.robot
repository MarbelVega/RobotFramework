*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${slt_AddPerson_Prefix}    xpath=//select[@name='Prefix']
${txt_AddPerson_FName}    xpath=//input[@name='FirstName']
${txt_AddPerson_MName}    xpath=//input[@name='MI']
${txt_AddPerson_LName}    xpath=//input[@name='LastName']
${txt_AddPerson_Suffix}    xpath=//input[@name='Suffix']
${txt_AddPerson_Title}    xpath=//input[@name='Title']

#Personnel Details
${txt_AddPerson_FormalName}    xpath=//input[@name='FormalName']
${txt_AddPerson_Nickname}    xpath=//input[@name='NickName']
${txt_AddPerson_ProfDesg1}    xpath=//input[@name='ProfDesignation1']
${txt_AddPerson_ProfDesg2}    xpath=//input[@name='ProfDesignation2']
${txt_AddPerson_Acro}    xpath=//input[@name='Acronym']
${txt_AddPerson_EmpUnion}    xpath=//input[@name='Level']
${txt_AddPerson_ParaName}    xpath=//input[@name='OtherInfo']
${btn_AddPerson_TechStaff_Yes}    xpath=//input[@name='TechStaff' and @value='1']
${btn_AddPerson_TechStaff_No}    xpath=//input[@name='TechStaff' and @value='0']
${slt_AddPerson_DiscCode254}    xpath=//select[@name='DisciplineCodeId']
${slt_AddPerson_DiscCode330}    xpath=//select[@name='Discipline_330CodeID']
${txt_AddPerson_Bio}    xpath=//textarea[@name='bio']
${txt_AddPerson_SummaryNotes}    xpath=//textarea[@name='summaryNotes']

#Employment History
${txt_AddPerson_YrsStartInd}    xpath=//input[@name='User_Year']
${txt_AddPerson_StartDate}    xpath=//input[@name='User_StartDate']
${txt_AddPerson_SepDate}    xpath=//input[@name='User_EndDate']
${txt_AddPerson_PrevStartDate}    xpath=//input[@name='datePreviousStart']
${txt_AddPerson_PrevSepDate}    xpath=//input[@name='datePreviousSeparation']
${txt_AddPerson_AddTimeWFirm}    xpath=//input[@name='additionalTimeWithFirm']
${txt_AddPerson_YrsWOther}    xpath=//input[@name='yearsWithOtherFirms']

#Office Contact Info
${txt_AddPerson_OfficeEmail}    xpath=//input[@name='OfficeEmail']
${txt_AddPerson_OfficePhone}    xpath=//input[@name='OfficePhone']
${txt_AddPerson_OfficeExt}    xpath=//input[@name='OfficeExt']
${txt_AddPerson_Officefax}    xpath=//input[@name='OfficeFax']
${txt_AddPerson_Location}    xpath=//input[@name='OfficeLocation']
${txt_AddPerson_OfficeCell}    xpath=//input[@name='CellPhone']
${txt_AddPerson_AIM}    xpath=//input[@name='OfficePager']
${slt_AddPerson_SF330DefaultOffice}    xpath=//select[@name='SF330_OfficeID']

${btn_AddPerson_Save}    xpath=//input[@id='submit']

*** Keywords ***
Select Prefix
    [Arguments]    ${text}
    [Documentation]     Selects Option in Prefix Dropdown by ${text}
    ...
    Click-Object    ${slt_AddPerson_Prefix}
    Click-Object    xpath=//select[@name='Prefix']//option[@value='${text}']
    
Select 254 Disc Code
    [Arguments]    ${text}
    [Documentation]    Selects Option in 254 Discipline Code Dropdown by ${text}
    ...
    Click-Object    ${slt_AddPerson_DiscCode254}
    Click-Object    ${slt_AddPerson_DiscCode254}//option[text()='${text}']
    
Select 330 Disc Code
    [Arguments]    ${text}
    [Documentation]    Selects Option in 254 Discipline Code Dropdown by ${text}
    ...
    Click-Object    ${slt_AddPerson_DiscCode330}
    Click-Object    xpath=(//select[@name='Discipline_330CodeID']//option[contains(text(),'${text}')])[1]
    
Select SF330 Office
    [Arguments]    ${text}
    [Documentation]    Selects Option in SF330 Default Office Dropdown by ${text}
    ...
    Click-Object    ${slt_AddPerson_SF330DefaultOffice}
    Click-Object    xpath=(//select[@name='SF330_OfficeID']//option[contains(text(),'${text}')])[1]
    