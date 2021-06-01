*** Settings ***
Library    SeleniumLibrary
Library    String
Library     RequestsLibrary
Resource    ../page/LoginPage.robot
Resource    ../page/UniversalKeywords.robot
Resource    ../page/Global/GlobalVariables.robot
Resource    ../page/Administration.robot
Resource    ../page/Workflow/Workflow.robot
Resource    ../page/ContactManager.robot
Resource    ../page/Leads.robot
Resource    ../page/Leads/NewLead.robot
Resource    ../page/Leads/LeadInfo.robot
Resource    ../page/CompanyInfo.robot
Resource    ../page/OpportunitySummary.robot
Resource    ../page/Contacts.robot
Resource    ../page/ContactInfo.robot
Resource    ../page/Company.robot
Resource    ../page/AddCompany.robot

Test Teardown    Close Browser

*** Variables ***
#${URL}    http://services.org.com/
#${URL}    http://services.org.com/
${URL}    https://services-qe.orgdev.com
#${URL}    https://hr-4.orgdev.com/

** Keywords **
#  Before you use a request, you must create a session.  The bare minimum that you need to create a session is
#  an alias name, and a url.  The url should basically be your environment host.
create workflow runner session
    [Arguments]     ${alias name}
    create session  alias=${alias name}   url=${URL}

*** Test Cases ***
Workflow > Lead > Create > Set
    [Tags]    Workflow    TC-475
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Click-Object    ${btn_Workflow_NewWorkflow}
    Sleep    1
    ${name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Name}    ${name}
    Click-Object    ${btn_Workflow_New_Resource_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Resource_Lead}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Event_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Event_Create}
    Sleep    1
    Click-Object    ${btn_Workflow_New_WorkflowActions}
    Click-Object    ${btn_Workflow_New_Actions_Add}
    Sleep    1
    Click-Object    ${lbl_Workflow_New_Actions_SetAction}
    Sleep    2
    Click-Object    ${btn_Workflow_New_Actions_SetAction_Opts}
    Sleep    1
    Click-Object    ${btn_Wrofklow_New_Actions_SetAction_Opts_Set}
    Sleep    5
    Click-Object    ${btn_Workflow_New_Actions_Values_Add}
    Click-Object    ${btn_Workflow_New_Actions_Values_Field}
    New Workflow > Set > Select Action Field by Text    Client - City
    ${rand_city}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Actions_Value_Field_TextValue}    ${rand_city}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Save}
    Sleep    1
    Click-Object    ${btn_Workflow_NewConf_OK}
    Sleep    1
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Activate}
    Click-Object    ${GlobalNav_ContactManager}
    Sleep    1
    Click-Object    ${link_ContactManager_Lead}
    Click-Object    ${btn_Lead_New}
    Switch Window    NEW
    ${LeadName}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_NewLead_Name}    ${LeadName}
    Enter-Text    ${txt_NewLead_PotentialClient}    Automation
    Click-Object    ${btn_NewLead_PCSearch_1stRslt}
    Click-Object    ${btn_NewLead_Save}
    Validate Lead Name    ${LeadName}
    create workflow runner session  workflow
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    Reload Page
    Open Company by Name    Automation Company
    Validate Company City    ${rand_city}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Delete}
    Click-Object    ${btn_Workflow_Actions_Delete_Confirm_Yes}
    
Workflow > Opportunity > Create > Set
    [Tags]    Workflow    TC-487
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Click-Object    ${btn_Workflow_NewWorkflow}
    Sleep    1
    ${name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Name}    ${name}
    Click-Object    ${btn_Workflow_New_Resource_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Resource_Opp}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Event_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Event_Create}
    Sleep    1
    Click-Object    ${btn_Workflow_New_WorkflowActions}
    Click-Object    ${btn_Workflow_New_Actions_Add}
    Sleep    1
    Click-Object    ${lbl_Workflow_New_Actions_SetAction}
    Sleep    2
    Click-Object    ${btn_Workflow_New_Actions_SetAction_Opts}
    Sleep    1
    Click-Object    ${btn_Wrofklow_New_Actions_SetAction_Opts_Set}
    Sleep    5
    Click-Object    ${btn_Workflow_New_Actions_Values_Add}
    Click-Object    ${btn_Workflow_New_Actions_Values_Field}
    New Workflow > Set > Select Action Field by Text    Client - City
    ${rand_city}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Actions_Value_Field_TextValue}    ${rand_city}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Save}
    Sleep    1
    Click-Object    ${btn_Workflow_NewConf_OK}
    Sleep    1
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Activate}
    Click-Object    ${GlobalNav_ContactManager}
    Sleep    1
    Click-Object    ${link_ContactManager_Lead}
    Click-Object    ${btn_Lead_New}
    Switch Window    NEW
    ${LeadName}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    #TODO - Need to Update and fix the validation
    create workflow runner session  workflow
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    Reload Page
    Opp - Open Company by Name    Automation Company
    Validate Company City    ${rand_city}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Delete}
    Click-Object    ${btn_Workflow_Actions_Delete_Confirm_Yes}
    
Workflow > Contact > Create > Set
    [Tags]    Workflow    TC-467
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Click-Object    ${btn_Workflow_NewWorkflow}
    Sleep    1
    ${name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Name}    ${name}
    Click-Object    ${btn_Workflow_New_Resource_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Resource_Contact}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Event_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Event_Create}
    Sleep    1
    Click-Object    ${btn_Workflow_New_WorkflowActions}
    Click-Object    ${btn_Workflow_New_Actions_Add}
    Sleep    1
    Click-Object    ${lbl_Workflow_New_Actions_SetAction}
    Sleep    2
    Click-Object    ${btn_Workflow_New_Actions_SetAction_Opts}
    Sleep    1
    Click-Object    ${btn_Wrofklow_New_Actions_SetAction_Opts_Set}
    Sleep    5
    Click-Object    ${btn_Workflow_New_Actions_Values_Add}
    Click-Object    ${btn_Workflow_New_Actions_Values_Field}
    New Workflow > Set > Select Action Field by Text    Company - City
    ${rand_city}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Actions_Value_Field_TextValue}    ${rand_city}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Save}
    Sleep    1
    Click-Object    ${btn_Workflow_NewConf_OK}
    Sleep    1
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Activate}
    Click-Object    ${GlobalNav_ContactManager}
    Sleep    1
    Click-Object    ${lnk_ContactManager_Contact}
    Click-Object    ${btn_Contact_NewContact}
    Enter-Text    ${txt_ContactInfo_Company}    Automation Company
    Click-Object    ${btn_ContactInfo_CSearch_1stRslt}
    ${FName}    Generate Random String    10    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_ContactInfo_Fname}    ${FName}
    ${LName}    Generate Random String    10    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_ContactInfo_Lname}    ${LName}
    Click-Object    ${btn_ContactInfo_Save}
    create workflow runner session  workflow
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    Reload Page
    Open Contact Company by Name    Automation Company
    Validate Company City    ${rand_city}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Delete}
    Click-Object    ${btn_Workflow_Actions_Delete_Confirm_Yes}
    
Workflow > Company > Create > Set
    [Tags]    Workflow    TC-462
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Click-Object    ${btn_Workflow_NewWorkflow}
    Sleep    1
    ${name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Name}    ${name}
    Click-Object    ${btn_Workflow_New_Resource_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Resource_Company}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Event_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Event_Create}
    Sleep    1
    Click-Object    ${btn_Workflow_New_WorkflowActions}
    Click-Object    ${btn_Workflow_New_Actions_Add}
    Sleep    1
    Click-Object    ${lbl_Workflow_New_Actions_SetAction}
    Sleep    2
    Click-Object    ${btn_Workflow_New_Actions_SetAction_Opts}
    Sleep    1
    Click-Object    ${btn_Wrofklow_New_Actions_SetAction_Opts_Set}
    Sleep    5
    Click-Object    ${btn_Workflow_New_Actions_Values_Add}
    Click-Object    ${btn_Workflow_New_Actions_Values_Field}
    New Workflow > Set > Select Action Field by Text    Name
    ${rand_Name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Actions_Value_Field_TextValue}    ${rand_Name}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Save}
    Sleep    1
    Click-Object    ${btn_Workflow_NewConf_OK}
    Sleep    1
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Activate}
    Click-Object    ${GlobalNav_ContactManager}
    Sleep    1
    Click-Object    ${lnk_ContactManager_Comapny}
    Click-Object    ${btn_Company_Add}
    Switch Window    NEW
    ${LeadName}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_NewLead_Name}    ${LeadName}
    Enter-Text    ${txt_NewLead_PotentialClient}    Automation
    Click-Object    ${btn_NewLead_PCSearch_1stRslt}
    Click-Object    ${btn_NewLead_Save}
    Validate Lead Name    ${LeadName}
    create workflow runner session  workflow
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    Reload Page
    Open Company by Name    Automation Company
    Validate Company City    ${rand_Name}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Delete}
    Click-Object    ${btn_Workflow_Actions_Delete_Confirm_Yes}
    
Workflow > Project > Create > Set
    [Tags]    Workflow    TC-512
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Click-Object    ${btn_Workflow_NewWorkflow}
    Sleep    1
    ${name}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Name}    ${name}
    Click-Object    ${btn_Workflow_New_Resource_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Resource_Proj}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Event_OptionsArrow}
    Click-Object    ${btn_Workflow_New_Event_Create}
    Sleep    1
    Click-Object    ${btn_Workflow_New_WorkflowActions}
    Click-Object    ${btn_Workflow_New_Actions_Add}
    Sleep    1
    Click-Object    ${lbl_Workflow_New_Actions_SetAction}
    Sleep    2
    Click-Object    ${btn_Workflow_New_Actions_SetAction_Opts}
    Sleep    1
    Click-Object    ${btn_Wrofklow_New_Actions_SetAction_Opts_Set}
    Sleep    5
    Click-Object    ${btn_Workflow_New_Actions_Values_Add}
    Click-Object    ${btn_Workflow_New_Actions_Values_Field}
    New Workflow - Select Action Field by Text
    ${rand_city}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_Workflow_New_Actions_Value_Field_TextValue}    ${rand_city}
    Sleep    1
    Click-Object    ${btn_Workflow_New_Save}
    Sleep    1
    Click-Object    ${btn_Workflow_NewConf_OK}
    Sleep    1
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Activate}
    Click-Object    ${GlobalNav_ContactManager}
    Sleep    1
    Click-Object    ${link_ContactManager_Lead}
    Click-Object    ${btn_Lead_New}
    Switch Window    NEW
    ${LeadName}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_NewLead_Name}    ${LeadName}
    Enter-Text    ${txt_NewLead_PotentialClient}    Automation
    Click-Object    ${btn_NewLead_PCSearch_1stRslt}
    Click-Object    ${btn_NewLead_Save}
    Validate Lead Name    ${LeadName}
    create workflow runner session  workflow
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    Reload Page
    Open Company by Name    Automation Company
    Validate Company City    ${rand_city}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_Workflow}    
    Open Options Menu by Workflow Name    ${name}
    Click-Object    ${btn_Workflow_Actions_Delete}
    Click-Object    ${btn_Workflow_Actions_Delete_Confirm_Yes}
    
make workflow runner session call
    #  Create your session, and give it a name that you want to differentiate what you are calling.
    #  Here, I called my session workflow.
    create workflow runner session  workflow
    #  Call get request to send a get call, and pass in both your alias, and the path after the host.
    #  Here, we are calling the workflow runner, and we are using our alias "workflow"
    #  If you want to do any processing on the response, assign it to a variable.  Here, I used response.
    ${response}=  get request   workflow  external/workflow/dowork.cfm?firmid=919
    #  This is simply an example on how to look for your firm in the response.
    #  Should be true  will actually pass or fail your script, so you might instead want to assign the value
    #  of the check into a variable and use that for processing.