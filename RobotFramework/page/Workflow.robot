*** Settings ***
Library    SeleniumLibrary
Resource    ../../../../../Universal/UniversalKeywords.robot

*** Variables ***
#Workflows Tab
${btn_Workflows_NewWorkflow}    xpath=//button[text()='New Workflow']
${btn_Workflow_NewWorkflow}    xpath=//button[text()='New Workflow']

#Workflows Grid
${btn_Workflow_FirstDraft}    xpath=//img[contains(@src, 'pause.png')]

#Workflow Actions
${btn_Workflow_Actions_Activate}    xpath=//span[@class='x-menu-item-text' and text()='Activate']
${btn_Workflow_Actions_Delete}    xpath=//span[@class='x-menu-item-text' and text()='Delete']

## Delete Confirmation
${btn_Workflow_Actions_Delete_Confirm_Yes}    xpath=//button[text()='Yes']

#New Workflow Window
${txt_Workflow_New_Name}    xpath=//input[@name='name']
${txt_Workflow_New_Group}    xpath=//input[@name='group']

##Workflow Group Dropdown
${btn_Workflow_New_Group_OptionsArrow}    xpath=//input[@data-qa='drpWorkflowGroup'
#xpath=(//div[@class='x-form-item ' and @tabindex='-1']//img)[1]
${btn_Workflow_New_Group_Lead}    xpath=//div[@class='x-combo-list-item' and text()='Leads']

##Resource Dropdown
${btn_Workflow_New_Resource_OptionsArrow}    xpath=//input[@data-qa='drpResource']    
#xpath=(//div[@class='x-form-item ' and @tabindex='-1']//img)[3]
${btn_Workflow_New_Resource_Lead}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Lead']
${btn_Workflow_New_Resource_Opp}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Opportunity']
${btn_Workflow_New_Resource_Company}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Company']
${btn_Workflow_New_Resource_Contact}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Contact']
${btn_Workflow_New_Resource_Proj}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Project']


##Event Dropdown
${btn_Workflow_New_Event_OptionsArrow}    xpath=//input[@data-qa='drpEvent']    
#xpath=(//div[@class='x-form-item ' and @tabindex='-1']//img)[4]
${btn_Workflow_New_Event_Create}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Create']

##Bottom Tabs
${btn_Workflow_New_WorkflowActions}    xpath=//span[text()='Workflow Actions']

#Workflow Actions
${btn_Workflow_New_Actions_Add}    xpath=//button[text()='Add Action']


##Set Action
${lbl_Workflow_New_Actions_SetAction}    xpath=//div[text()='Set Action']
${btn_Workflow_New_Actions_SetAction_Opts}        xpath=//input[@data-qa='drpActionList']
#xpath=(//div[contains(@class,'x-form-field-wrap')]//img)[6]

${btn_Wrofklow_New_Actions_SetAction_Opts_Set}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Set']

##Set Values
${btn_Workflow_New_Actions_Values_Add}    xpath=//button[text()='Add value']
${btn_Workflow_New_Actions_Values_Field}    xpath=//input[@data-qa='drpFieldToSet']
#xpath=(//div[contains(@class,'x-form-field-wrap')]//img)[8]

${btn_Workflow_New_Actions_Values_Field_ClientCity}    xpath=//div[contains(@class, 'x-combo-list-item') and text()='Client - City']

${txt_Workflow_New_Actions_Value_Field_TextValue}    xpath=//input[@type='text' and contains(@class,'x-box-item')]
${txt_Workflow_New_Actions_Value_Field_TextValue2}    xpath=//input[@type='text' and contains(@class,'x-form-text x-form-field')]

#Bottom Buttons
${btn_Workflow_New_Save}    xpath=//button[text()='Save']
${btn_Workflow_New_Cancel}    xpath=//button[text()='Cancel']

#Create Confirmation Pop-Up
${btn_Workflow_NewConf_OK}    xpath=//button[text()='OK']

*** Keywords ***
Open Options Menu by Workflow Name
    [Arguments]    ${name}
    [Documentation]    Opens the Workflow Options Menu using the ${name} of the created workflow. (Note: Spaces are denoted with %20, so "Work Flow" becomes "Work%20Flow")
    ...    
    Click-Object    xpath=//span[@data-qa="${name}"]
    
New Workflow > Set > Select Action Field by Text
    [Arguments]    ${text}
    [Documentation]    Select a field from the 'Action fields' dropdown by ${text} when creating a new workflow.
    ...    
    Click-Object    xpath=//div[contains(@class, 'x-combo-list-item') and text()='${text}']
    
New Workflow > Set > Select Value by Text
    [Arguments]    ${text}
    [Documentation]    Select a value from the 'Values' dropdown by ${text} when creating a new workflow
    ...    
    
    Click-Object    xpath=//div[@class='x-combo-list-item' and text()='${text}']