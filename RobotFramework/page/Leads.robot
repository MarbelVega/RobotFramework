*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${btn_Lead_New}    xpath=//button[@type='button' and text()='New Lead']
${txt_Lead_Srch}    xpath=(//td[@class='x-toolbar-cell']//input[@type='text'])[1]

#Search Results
${btn_Lead_FrstRslt}    xpath=(//div[contains(@class, 'x-grid3-col-id')])[1]
${lbl_Lead_NoResults}    xpath=//div[text()='There are not any leads that match your criteria. Please try again.']


#Search Results Menu List Options
${btn_Lead_LeadDetails}    xpath=//span[text()='Lead details']

*** Keywords ***
Wait For Lead to Load in Search
    [Arguments]    ${name}
    [Documentation]    Waits for Lead Search Results to Load by waiting for the Lead Name element to exist with ${name} as text
    ...
    Wait Until Element Is Visible    xpath=//div[text()='${name}']    30    Expected Lead Result did not load.
    
Wait For Search to Load and Validate No Results Found
    [Arguments]    ${name}
    [Documentation]    Waits for Lead Search Results to Load by waiting 15 seconds and checking to see if ${name} element exists.
    ...
    Sleep    15
    Page Should Not Contain Element    xpath=//div[text()='${name}']    ${name} loaded so Lead was not Deleted.