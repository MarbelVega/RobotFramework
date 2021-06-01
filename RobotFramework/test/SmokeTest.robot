*** Settings ***
Library    OperatingSystem
Library    SeleniumLibrary
Library    String

Resource    ../../PageObjs/Global/GlobalVariables.robot
Resource    ../../../Universal/UniversalKeywords.robot
Resource    ../../PageObjs/Modules/Login/LoginPage.robot
Resource    ../../PageObjs/Modules/ContactManager/ContactManager.robot
Resource    ../../PageObjs/Modules/ContactManager/Company/Company.robot
Resource    ../../PageObjs/Modules/ContactManager/Company/AddCompany.robot
Resource    ../../PageObjs/Modules/ContactManager/Company/CompanyInfo.robot
Resource    ../../PageObjs/Modules/ContactManager/Opportunity/Opportunity.robot
Resource    ../../PageObjs/Modules/Personnel/Personnel.robot
Resource    ../../PageObjs/Modules/Personnel/AddPersonnel.robot
Resource    ../../PageObjs/Modules/Personnel/PersonnelSummary.robot
Resource    ../../PageObjs/Modules/Projects/Projects.robot
Resource    ../../PageObjs/Modules/Projects/NewProject.robot
Resource    ../../PageObjs/Modules/Projects/ProjectSummary.robot
Resource    ../../PageObjs/Modules/Projects/ProjectAdmin.robot
Resource    ../../PageObjs/Modules/Projects/EditProject.robot
Resource    ../../PageObjs/Modules/Projects/MergeProject.robot
Resource    ../../PageObjs/Modules/Reports/Reports.robot
Resource    ../../PageObjs/Modules/Reports/CreateContactReport.robot
Resource    ../../PageObjs/Modules/Reports/CreateLeadReport.robot
Resource    ../../PageObjs/Modules/Reports/ReportResults.robot
Resource    ../../PageObjs/Modules/Dashboard/Dashboard.robot
Resource    ../../PageObjs/Modules/Publisher/Publisher.robot
Resource    ../../PageObjs/Modules/Publisher/CreateResume.robot
Resource    ../../PageObjs/Modules/Publisher/DocumentView.robot
Resource    ../../PageObjs/Modules/Administration/Administration.robot
Resource    ../../PageObjs/Modules/Administration/ValueLists.robot
Resource    ../../PageObjs/Modules/Administration/EditCategoriesVL.robot
Resource    ../../PageObjs/Modules/Activities/Activities.robot
Resource    ../../PageObjs/Modules/Marketing/Marketing.robot
Resource    ../../PageObjs/Modules/Marketing/CreateCampaign.robot
Resource    ../../PageObjs/Modules/Marketing/CampaignDetails.robot
Resource    ../../PageObjs/Modules/Goals/Goals.robot


Test Teardown    Close Browser 

*** Variables ***
#${URL}    http://integration.orgdev.com
#${URL}    https://services-staging.orgdev.com/
${URL}    https://services-qe.orgdev.com
#${URL}    http://services.org.com/

*** Test Cases ***
Create Company Record
    [Documentation]    Creates a Simple Company Record using Only the Required Fields
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_ContactManager}
    Click-Object    ${lnk_ContactManager_Comapny}
    Click-Object    ${btn_Company_Add}
    ${name}    Generate Random String    15
    Enter-Text    ${txt_AddCo_Name}    ${name}
    Random String    ${txt_AddCo_Address1}    20
    Random String    ${txt_AddCo_City}    10
    Select Company Country    United States
    Select Company State    Texas
    Enter-Text    ${txt_AddCo_Phone}    5555551234
    Random String    ${txt_AddCo_Website}    20
    Click-Object    ${btn_AddCo_Save}
    Wait Until Element Is Visible    ${lbl_CompanyInfo_CompanyInfo}    60s    Company was not created correctly or page did not load within 60s
    Validate Company Name    ${name}
    Click-Object    ${btn_CompanyInfo_Summary_Delete}
    Handle Alert    Accept
    Wait Until Element Is Visible    ${tbl_Company_Table}    60s    Company page did not load after 60s
    Validate Company Does Not Exist    ${name}
	    
Edit Opportunity From Opportunity Grid
	#TODO - Blocked Because unselectable=on flag in the text fields keeps Selenium from entering text into Comments fields.
    [Documentation]    Edits the comments field of the first row in the Opportunity Page's grid.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_ContactManager}
    Click-Object    ${lnk_ContactManager_Opporunity}
    Wait Until Element Is Visible    ${lbl_Opportunity_HeaderTxt}    60s    Opportunities Page did not load after 60s
    Wait Until Element Is Visible    ${txt_Opportunity_Grid_1stRow_Comments}    60s    Opportunities Grid did not load after 60s
    ${randomtxt}=    Generate Random String    10
    #Breaks here; Selenium can't enter text into the Comments field because it is reading it as not editable.
    Sleep	3
    Double Click Element	${txt_Opportunity_Grid_1stRow_Comments}
    Press Keys	${txt_Opportunity_Grid_1stRow_Comments}	CTRL+a+BACKSPACE
    #Added Double click and entered Backspace two times because it's intermittently ignoring the first backspace. 
    Double Click Element	${txt_Opportunity_Grid_1stRow_Comments}
    Press Keys	${txt_Opportunity_Grid_1stRow_Comments}	CTRL+a+BACKSPACE
    Press Keys	${txt_Opportunity_Grid_1stRow_Comments}	${randomtxt}
    Press Keys	${txt_Opportunity_Grid_1stRow_Comments}	ENTER	
    Sleep	2
    Click-Object    ${btn_Opportunity_Grid_Actions_Refresh}
    Sleep	4
    ${comparetxt}=    Get Text        ${txt_Opportunity_Grid_1stRow_Comments}
    Should Be Equal As Strings    ${randomtxt}    ${comparetxt}
    
Create Personnel Record
    [Documentation]    Creates a Simple Personnel Record using Only the Required Fields
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Personnel}
    Click-Object    ${btn_Personnel_Add}
    ${fname}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    ${lname}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddPerson_FName}    ${fname}
    Enter-Text    ${txt_AddPerson_LName}    ${lname}
    Click-Object    ${btn_AddPerson_Save} 
    Wait Until Element Is visible    ${lbl_PersonnelSumm_Header}    60s    Personnel Summary page did not load after 60s
    Validate Employee Name    ${fname} ${lname}
    Click-Object    ${btn_PersonnelSumm_Delete}
    Handle Alert    Accept
    Wait Until Element Is Visible    ${btn_Personnel_Add}    60s    Personnel page did not load after 60s
    #Click-Object    ${lnk_Personnel_StartsT}
    #Sleep    5
    Validate Personnel Does Not Exist    ${lname}
    
Convert New Personnel to User
    [Documentation]    Converts a newly created Personnel to a user.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Personnel}
    Click-Object    ${btn_Personnel_Add}
    ${fname}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    ${lname}    Generate Random String    15    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddPerson_FName}    ${fname}
    Enter-Text    ${txt_AddPerson_LName}    ${lname}
    Click-Object    ${btn_AddPerson_Save} 
    Wait Until Element Is visible    ${lbl_PersonnelSumm_Header}    60s    Personnel Summary page did not load after 60s
    Validate Employee Name    ${fname} ${lname}
    Sleep	3
    Click-Object    ${btn_PersonnelSumm_MakeUser}
    Enter-Text    ${txt_PersonnelSumm_Pop_Email}    test@test.test
    Click-Object    ${btn_PersonnelSumm_Pop_Next}
    Sleep    1
    Click-Object    ${btn_PersonnelSumm_Pop_FORG}
    Click-Object    ${btn_PersonnelSumm_Pop_Convert}
    Wait Until Element Is Not Visible    ${ConvertPersonnelPopUp}    60s    Convert Personnel did not complete after 60s   
    Validate Employee Name    ${fname} ${lname}
    Sleep	3
    Element Should Not Be Visible    ${btn_PersonnelSumm_MakeUser}
    Click-Object    ${btn_PersonnelSumm_Delete}
    Handle Alert    Accept
    Wait Until Element Is Visible    ${btn_Personnel_Add}    60s    Personnel page did not load after 60s
    Click-Object    ${lnk_Personnel_StartsT}
    Sleep    5
    Validate Personnel Does Not Exist    ${lname}
    
Create Project Record
    [Documentation]    Creates a Simple Project Record using Only the Required Fields
    [Tags]    Smoke
    Login-WebApp    ${URL} 
    Click-Object    ${GlobalNav_Projects}
    Wait Until Element Is Visible    ${lbl_Projects_Header}    60s    Projects page did not load after 60s
    Click-Object    ${btn_Projects_NewProj}
    Wait Until Element Is Visible    ${lbl_NewProj_Header}    60s    New Project page did not load after 60s
    ${name}    Generate Random String    15
    Enter-Text    ${txt_NewProj_ProjDetails_ProjName}    ${name}
    Sleep    2
    Click-Object    ${btn_NewProj_CreateProj}
    Wait Until Element Is Visible    ${lnk_ProjSumm_ProjSumm}     60s    Project Summary page did not load after 60s
    Validate Project Name    ${name}
    Click-Object    ${btn_ProjSumm_EditAll}
    Click-Object    ${btn_ProjEdit_Delete}
    Handle Alert    Accept
    #TODO - Finish Confirming Project Deletion
  
Merge Project into Newly Created Project
    [Documentation]    Create 2 Simple Project Records and Merges one into the other.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    # Create Project1
    Click-Object    ${GlobalNav_Projects}
    Wait Until Element Is Visible    ${lbl_Projects_Header}    60s    Projects page did not load after 60s
    Click-Object    ${btn_Projects_NewProj}
    Wait Until Element Is Visible    ${lbl_NewProj_Header}    60s    New Project page did not load after 60s
    Enter-Text    ${txt_NewProj_ProjDetails_ProjName}    Merge Project Two
    Sleep    2
    Click-Object    ${btn_NewProj_CreateProj}
    Wait Until Element Is Visible    ${lnk_ProjSumm_ProjSumm}     60s    Project Summary page did not load after 60s
    Validate Project Name    Merge Project Two
    # Create Project2 
    Click-Object    ${GlobalNav_Projects}
    Wait Until Element Is Visible    ${lbl_Projects_Header}    60s    Projects page did not load after 60s
    Click-Object    ${btn_Projects_NewProj}
    Wait Until Element Is Visible    ${lbl_NewProj_Header}    60s    New Project page did not load after 60s
    Enter-Text    ${txt_NewProj_ProjDetails_ProjName}    Merge Project One
    Sleep    2
    Click-Object    ${btn_NewProj_CreateProj}
    Wait Until Element Is Visible    ${lnk_ProjSumm_ProjSumm}     60s    Project Summary page did not load after 60s
    Validate Project Name    Merge Project One
    # Merge Project one into other
    Click-Object    ${GlobalNav_Projects}
    Click-Object    ${lnk_Projects_ProjAdmin}
    Click-Object    ${lnk_ProjAdmin_Merge}
    Enter-Text    ${txt_ProjMerge_ProjToMerge}    Merge Project Two
    Sleep    1
    Select Merge Option By Text    Merge Project Two
    Enter-Text    ${txt_ProjMerge_MergeInto}    Merge Project One
    Sleep    1
    Select Merge Option By Text    Merge Project One
    Click-Object    ${btn_ProjMerge_Save}
    Wait Until Element Is Visible    ${lbl_ProjMerge_SuccessMsg}    60s    Merge Success Message did not display.
    
Create a Report
    [Documentation]    Creates a Simple Report
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Reports}
    Click-Object    ${btn_Reports_Contact}
    Click-Object    ${btn_Reports_CreateCustomReport}
    Click-Object    ${btn_CreateContactReport_Fields_CompanyName}
    Click-Object    ${btn_CreateContactReport_SaveContinue1}
    Click-Object    ${btn_CreateContactReport_SaveContinue2}
    Click-Object    ${btn_CreateContactReport_SaveContinue3}
    Validate Contact Report Headers    Company Name

Create a Report and Export it
    [Documentation]    Creates a Simple Report and Exports it.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Reports}
    Click-Object    ${btn_Reports_Lead}
    Click-Object    ${btn_Reports_CreateCustomReport}
    Click-Object    ${btn_CreateLeadReport_Fields_LeadType}
    Click-Object    ${btn_CreateLeadReport_SaveContinue1}
    Click-Object    ${btn_CreateLeadReport_SaveContinue2}
    Validate Lead Report Headers    Lead Type
    Click-Object    ${btn_ReportResults_ExportToExcel}
    Wait Until Created    C:\\Users\\*\\Downloads\\report.csv
    Remove File    C:\\Users\\*\\Downloads\\report.csv
	
Create a new Dashboard
    [Documentation]    Creates a new Dashboard
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${btn_Dashboard_Settings}
    Click-Object    ${btn_DashSettings_NewTab}
    Sleep    1
    Click-Object    ${btn_Dashboard_Administration}
    Click-Object    ${btn_Dashboard_DashboardItems}
    # "The Tab Title" text field shows not visible after creation. Come back to dashboard items as workaround
    Enter-Text    ${txt_DashSettings_TabTitle}    Automation Test
    press keys    None  TAB
    Check If Dashboard Tab Exists	Automation Test    
    Delete Dashboard Tab By Name    Automation Test
    Check If Dashboard Tab Does Not Exist    Automation Test
   
Edit the Settings on a Widget
    [Documentation]    Edits the settings on a widget element on the dashboard.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${lbl_Dashboard_FirstTab}
    ${widgetName}=    Get Text    ${lbl_Dashboard_FirstWidgetName}
    Check for Widget Title    ${widgetName}
    ${WidgNameLength}=    Get Length    ${widgetName}
    Click-Object    ${btn_Dashboard_FirstWidgetSettings}
    ${randomtxt}=    Generate Random String    15
    Click-Object    ${txt_WidgetSettings_Title}
    Clear Text    ${txt_WidgetSettings_Title}    ${WidgNameLength}
    Enter-Text    ${txt_WidgetSettings_Title}    ${randomtxt}
    Click-Object    ${btn_WidgetSettings_Save}
    Check for Widget Title    ${randomtxt}
    Click-Object    ${btn_Dashboard_FirstWidgetSettings}
    Click-Object    ${txt_WidgetSettings_Title}
    Clear Text    ${txt_WidgetSettings_Title}    15
    Enter-Text    ${txt_WidgetSettings_Title}    ${widgetName}
    Click-Object    ${btn_WidgetSettings_Save}
    Check for Widget Title    ${widgetName}
    
Generate a Document in Publisher
    [Documentation]    Generates a Document in Publisher
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Publisher}
    Click-Object    ${btn_Publisher_CreateDoc}
    Click-Object    ${btn_Publisher_CreateDoc_Resume}
    Switch Window    new
    ${name}    Generate Random String    15
    Enter-Text    ${txt_CreateResume_Name}    ${name}
    Enter-Text    ${txt_CreateResume_Personnel}    Automation
    Select Row By Name    Automation Tester
    Click-Object    ${btn_CreateResume_Save}
    Check Resume Name    ${name}
    Click-Object    ${btn_DocView_Delete}
    Handle Alert    Accept
    Enter-Text    ${txt_Publisher_SearchBar}     ${name}
    Sleep    1
    Check If Document Does Not Exist    ${name}

Create a Call Log
    [Documentation]    Creates a new call log
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Activities}
    Click-Object    ${btn_Activities_NewCall}
    Enter-Text    ${txt_Acts_NewLog_Attendee}    test
    Click-Object    ${lbl_Acts_NewLog_FirstListOption}
    Random String    ${txt_Acts_NewLog_Subject}    15
    #Enter-Text    ${txt_Acts_NewLog_Subject}    Automation Testing
    Click-Object    ${btn_Acts_NewLog_Save&Close}
    Wait Until Element Is Not Visible    ${btn_Acts_NewLog_Save&Close}    60s    New Call Log box took longer than 60s to go away, or save action failed.    
    Sleep    1
    Click-Object    ${btn_Activities_FirstOptionDropdown}
    Click-Object    ${btn_Activities_DeleteCall}
    Click-Object    ${btn_Activities_DeleteConfYes}
	
Add a Value to an existing Value List
    [Documentation]    Edits a Value List to Add a value.
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Admin}
    Click-Object    ${lnk_Admin_ValueLists}
    Click-Object    ${lnk_ValueLists_PrimaryCategories}
    Click-Object    ${btn_EditCategoriesVL_NewCat}
    ${randomtxt}=    Generate Random String    10
    Enter-Text    ${txt_NewCategory_Name}    1Automation Test ${randomtxt}
    Click-Object    ${btn_NewCategory_DpdMenuYes}
    Click-Object    ${btn_NewCategory_Add}
    Check if Category Exists    1Automation Test ${randomtxt}
    Click-Object    ${btn_EditCategoriesVL_Delete1stCat}
    Handle Alert    Accept
    
Create a Marketing Campaign
    [Documentation]    Creates a Marketing Campaign
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Marketing}
    Click-Object    ${btn_Marketing_CreateCampaign}
    Enter-Text    ${txt_CreateCampaign_Name}    Automation Campaign
    Click-Object    ${btn_CreateCampaign_Save}
    Check Campaign Name    Automation Campaign
    Click-Object    ${btn_CampaignDetails_RsltsDrop}
    Click-Object    ${btn_CampaignDetails_RsltsDrop_Delete}
    Click-Object    ${btn_CampaignDetails_DelConf_Delete}
 	   
Create a New Sales Goal
    #TODO - Fields in the New Sales Goal window need Automation Hooks.
    [Documentation]    Creates a New Sales Goal
    [Tags]    Smoke
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Goals}
    Click-Object    ${btn_Goals_NewGoal}
    Click-Object	${txt_NewGoal_Type_SalesGoal} 
    Click-Object    ${ddn_NewGoal_Type_SalesGoal}	
    sleep	1
    Click-Object    ${chkbx_NewGoal_Company}
    Sleep    2
    Enter-Text    ${txt_NewGoal_Comapny}    org
    Click-Object    ${lbl_NewGoal_Comapny_FirstRslt}
    Enter-Text    ${txt_NewGoal_DfltMonthlyGoal}    200
    Click-Object    ${btn_NewGoal_CreateGoal}