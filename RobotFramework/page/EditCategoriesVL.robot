*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${btn_EditCategoriesVL_NewCat}    xpath=//input[@value='new category']

${btn_EditCategoriesVL_Delete1stCat}    xpath=(//input[@type='submit' and @value='delete'])[1]

#New Categories
${txt_NewCategory_Name}    xpath=//input[@name='ProjectCategoryName']

${btn_NewCategory_DpdMenuYes}    xpath=//input[@name='AvailableCat' and @value='1']
${btn_NewCateogory_DpdMenuNo}    xpath=//input[@name='AvailableCat' and @value='0']

${btn_NewCategory_Add}    xpath=//input[@type='submit']

*** Keywords ***
Check if Category Exists
    [Arguments]    ${name}
    [Documentation]    Checks if a Category ${name} exists.
    ...
    Wait Until Element Is Visible    xpath=//div[contains(text(), '${name}')]    30s    Category ${name} does not exist or the page did not load properly.
    
Check if Category Does Not Exist
    [Arguments]    ${name}
    [Documentation]    Checks if a Category ${name} DOES NOT exist.
    ...
    Element Should Not Be Visible    xpath=//div[contains(text(), '${name}')]