*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Click-Object
    [Arguments]    ${obj}
    [Documentation]    Waits for object to be visible in the browser, and then clicks that object.
    ...    .
    Wait Until Element Is Visible    ${obj}    20    Element ${obj} did not display.
    Click Element    ${obj}

Enter-Text
    [Arguments]    ${obj}    ${txt}
    [Documentation]    Waits for object to be visible in the browser, and then enters text into object.
    ...    .
    Wait Until Element Is Visible    ${obj}    20    Element ${obj} did not display.
    Input Text    ${obj}    ${txt}   
    
Clear Text
    [Arguments]    ${loc}    ${num}
    [Documentation]    Presses the Backspace key ${num} number of times on ${loc} element.
    ...    .
    :FOR    ${index}    IN RANGE    ${num}
    \    Press Keys    ${loc}    \ue003

Random String
    [Arguments]    ${locator}    ${length}   
    [Documentation]    Generates are random string of ${length} characters and enters it into ${locator}. 
    ...    Contains Upper and Lower case letters as well as numbers.
    ...    .
    ${string}    Generate Random String    ${length}    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${locator}    ${string}
    
Random Numbers
    [Arguments]    ${locator}    ${length}   
    [Documentation]    Generates are random string of ${length} characters and enters it into ${locator}. 
    ...    Contains Upper and Lower case letters as well as numbers.
    ...    .
    ${string}    Generate Random String    ${length}    [NUMBERS]
    Enter-Text    ${locator}    ${string}

Close current window and use last opened window
    [Documentation]     This will close the window or tab you are on, and
    ...                 switch you back to the previously opened window.
    Close Window
    ${windows}=         Get Window Handles
    ${window_count}=    Get Length  ${windows}
    ${last_window}=     Evaluate  ${window_count} - 1
    Select Window       ${windows}[${last_window}]