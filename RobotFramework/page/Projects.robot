*** Settings ***
Library    SeleniumLibrary    
Library    String

*** Variables ***
#Headers
${lbl_Projects_Header}    xpath=//span[text()='Projects']
${lnk_Projects_ProjAdmin}    xpath=//*[text()='[Project Administration]']
${btn_Projects_NewProj}    xpath=//td[text()='New Project']

*** Keywords ***
#$x("(//div[contains(@class,'createDate') and contains(text(),'.')])[1]")
#Filters to Find Date Mask
Creation Date Compare
    [Arguments]    ${char}    ${regex}
    [Documentation]    Used to Compare the Date Mask for Date Localization validation. Grabs the first Create Date value from the grid using ${char} as the delimiter (Ex: /)
    ...    Then uses ${regex} to compare the DateMask string to the expected DateMask format (Ex: \\d{2}.\\d{2}.\\d{4} = ##.##.#### and is compared against the string).
    ...    .
    Wait Until Element Is Visible    xpath=(//div[contains(@class,'col-createDate') and contains(text(),'${char}')])[1]   30s    Project Search never finished or no Projects exist in Firm.
    ${DateMask}    Get Text    xpath=(//div[contains(@class,'col-createDate') and contains(text(),'${char}')])[1]
    Should Match Regexp    ${DateMask}    ${regex}