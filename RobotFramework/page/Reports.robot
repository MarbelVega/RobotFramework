*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Nav Menu
${btn_Reports_Contact}    xpath=//td[@class='coolButton']//a[text()='Contact']
${btn_Reports_Lead}    xpath=//td[@class='coolButton']//a[text()='Lead']
${btn_Reports_Opps}    xpath=//td[contains(@class,'coolButton')]//a[text()='Opportunity']
${btn_Reports_Proj}    xpath=//td[@class='coolButton']//a[text()='Project']
${btn_Reports_Co}    xpath=//td[@class='coolButton']//a[text()='Company']
${btn_Reports_Person}    xpath=//td[@class='coolButton']//a[text()='Personnel']

${btn_Reports_CreateCustomReport}    xpath=//img[@id='Create_Custom_Report_Button']
${btn_Reports_Customize}    xpath=//img[contains(@src,'customize') and @align='absmiddle']
${btn_Reports_Delete1st}    xpath=(//img[@alt='Delete this Report'])[1]

#Nav When Viewing Report
${lnk_Reports_Print}        xpath=//a[contains(., 'Print') and not(contains(., 'IE custom'))]
${lnk_Reports_Export_Excel}     xpath=//a[contains(., 'Export To Excel') and not(contains(., 'Cartesian'))]
${lnk_Reports_Export_Excel_Cartesian}     xpath=//a[contains(., 'Export To Excel') and (contains(., 'Cartesian'))]

*** Keywords ***
Open Report By Name
    [Arguments]    ${title}
    [Documentation]    Opens a report from the grid using the ${title}
    ...    .
    Click-Object    xpath=//a[@class='ReportsLinkSmall' and text()='${title}']
    
Verify Report Doesn't Exist
    [Arguments]    ${title}
    [Documentation]    Verifies that a certain report ${title} does not show up in the grid.
    ...    .
    Page Should Not Contain Element    xpath=//a[@class='ReportsLinkSmall' and text()='${title}']    Report ${title} exists and should not.
    
Open Random Report
    [Arguments]    ${count}
    [Documentation]    Opens a random report using an index value. Index is generated as '[#]' in range 1-${count} (ex: ${index}=[4])        
    ...    .
    ${index} =    Evaluate    random.sample(range(1, ${count}), 1)    random
    Click-Object    xpath=(//img[contains(@src,'customize') and @align='absmiddle'])${index}

Open Print View From Report
    [Documentation]     Opens the print view while you are on a report that has one.
    run keyword and ignore error  click-object    ${lnk_Reports_Print}

Export Excel From Report
    [Documentation]     Downloads/Exports an excel file if the report has it
    # Need to handle the dropdown selector
    run keyword and ignore error  click-object    ${lnk_Reports_Export_Excel}

Export Excel Cartesian From Report
    [Documentation]     Downloads/Exports an excel cartesian file if the report has it
    # Need to handle the dropdown selector
    run keyword and ignore error  click-object    ${lnk_Reports_Export_Excel_Cartesian}

Does report have a print view
    [Documentation]     Will return true if there is a print view
    ${count}=  Get element count  ${lnk_Reports_Print}
    [return]    Evaluate  ${count}>0

Does report have an export to excel link
    [Documentation]     Will return true if there is the export to excel link on the print view
    # Need to handle the dropdown selector
    ${count}=  Get element count  ${lnk_Reports_Export_Excel}
    [return]    Evaluate  ${count}>0

Does report have an export to excel cartesian link
    [Documentation]     Will return true if there is the export to excel cartesian link on the print view
    # Need to handle the dropdown selector
    ${count}=  Get element count  ${lnk_Reports_Export_Excel_Cartesian}
    [return]    Evaluate  ${count}>0
