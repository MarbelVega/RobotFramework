*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
${lbl_ReportResults_FirstGroupingHeader}    xpath=//*[@id="PrimaryGroupRow1"]/td/strong

${btn_ReportResults_ExportToExcel}    xpath=//img[@alt='Export results to Excel']
${btn_ReportResults_ExportToExcelCartesian}    xpath=//img[@alt='Export results to Excel (Cartesian)']
${btn_ReportResults_Print}    xpath=(//img[contains(@src,'print.gif')])[1]
${btn_ReportResults_PrintIECustom}    xpath=(//img[contains(@src,'print.gif')])[2]
${btn_ReportResults_SaveReport}    xpath=//img[@alt='Save this Report']

*** Keywords ***
Validate Report Title
    [Arguments]    ${title}
    [Documentation]    Checks Report Title field for ${title} text.
    ...    .
    Wait Until Element Is Visible    //div[@class='ReportsHelpFont' and contains(text(),'${title}')]//strong[text()='Report Title:']    60    Report Title: ${title} did not display.
    
Validate Report Header Rows
    [Arguments]    ${text}
    [Documentation]    Validates that the expected Report headers exist by checking ${text}
 
    Wait Until Element Is Visible    xpath=//td//div[contains(text(), '${text}')]    60s    Results Page did not load or Expected Header did not exist.
    
Validate Report Group by header
    [Documentation]    Validates first grouping ID.
    ...    Work in Progress. Only Validates first grouping ID.
    Wait Until Element Is Visible    xpath=//*[@id="PrimaryGroupRow1"]/td/strong  60s    Report was not created or page did not load within 60s

Export to Excel As A
    [Arguments]    ${name}
    [Documentation]    Makes a Selection from the Export to Excel As A.. dropdown based on name in the dropdown list (Ex: Flat File)
    ...    .
    Click-Object    xpath=//option[text()='${name}']