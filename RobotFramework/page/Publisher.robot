*** Settings ***
Library    SeleniumLibrary

*** Variables ***

#Action Buttons
${btn_Publisher_CreateDoc}    xpath=//button[text()='Create Document']

#Create Document Menu
${btn_Publisher_CreateDoc_Resume}    xpath=//span[@class='x-menu-item-text' and text()='Resume']

${txt_Publisher_SearchBar}    xpath=(//td[@class='x-toolbar-cell']//input[contains(@class, 'x-form-text x-form-field')])[1]

${pdoc generate button}    xpath=//button[text()='Generate Document']
${pdoc progress done}      xpath=//div[@class='x-progress-text']/div[text()='Done']
${pdoc select word temp}   xpath=//img[@src='/images/general_button_mega_selectword.gif']


${ptemp ddd}               xpath=//a[text()='Document Data Dictionary']
${ptemp ldf}               xpath=//a[text()='List Data Format']
${ptemp upload button}     xpath=//img[@src='/images/general_button_big_uploadtemplate.gif']
${ptemp upload name}       xpath=//input[@name='TemplateName']
${pbtemp choose file box}  xpath=//input[@name='ClientFileName']
${pbtemp upload save}      xpath=//input[@alt='Upload Document']

${pbdocnew name}           xpath=//input[@name='DocumentName']
${pbdocnew project}        xpath=//input[@name='ProjectName']
${pbdocnew opportunity}    xpath=//input[@name='OpportunityName']
${pbdocnew save doc}       xpath=//input[@name='addDocument']
${pbdocnew resume}         xpath=//input[@name='PersonnelName']

${pdoc plist open search}  xpath=//img[@src='/images/general_button_big_search.gif']/..
${pdoc plist input name}   xpath=//input[@name='ProjectName']
${pdoc plist search}       xpath=//input[@name='AddButton'][1]
${pdoc plist save}         xpath=//input[@name='selectProjects'][1]

${pdocnew download word}   xpath=//div[contains(text(), 'Download')]/a[text()= 'docx']
${pdocnew download idml}   xpath=//div[contains(text(), 'Download')]/a[text()= 'idml']

*** Keywords ***
Check If Document Exists
    [Arguments]    ${name}
    [Documentation]    Checks if a Document exists by document ${name}
    ...
    Wait Until Element Is Visible    xpath=//a[text()='${name}']    60s    Document ${name} did not display.
    
Check If Document Does Not Exist
      [Arguments]    ${name}
    [Documentation]    Checks if a Document does not exist by document ${name}
    ...
    Element Should Not Be Visible    xpath=//a[text()='${name}']    Document ${name} exists on the page.

Upload a template document
    [Documentation]    Abstraction of uploading the template documents.  Performs the steps, takes a file / name as parameters.
    [Arguments]     ${file to upload}  ${template name}
    Click-Object  ${ptemp upload button}
    Wait Until Keyword Succeeds  5 times  30s  Select Window   NEW
    input text  ${ptemp upload name}  ${template name}
    choose file  ${pbtemp choose file box}  ${file to upload}
    Click-Object  ${pbtemp upload save}
    ${windows}=  Get Window Handles
    select window  ${windows[1]}  # go back to original window
    sleep  5  # no matter what, it's going to refresh and break the dom.  so we're going to wait.  Until I can figure this one out.
    [Return]    Test name that should be random    

Upload a simple project profile template
    [Documentation]    Uploads the simplest project profile template
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleprojectprofiletemplate.docx
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple project profile IDML template
    [Documentation]    Uploads the simplest project profile idml template
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleprojectprofiletemplate.idml
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple project list IDML template
    [Documentation]    Uploads the simplest project list IDML template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}   C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleprojectlisttemplate.idml
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple opportunity profile IDML template
    [Documentation]    Uploads the simplest opportunity profile IDML template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleopportunityprofiletemplate.idml
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple resume IDML template
    [Documentation]    Uploads the simplest resume IDML template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleresumetemplate.idml
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple project list template
    [Documentation]    Uploads the simplest project list template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}   C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleprojectlisttemplate.docx
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple opportunity profile template
    [Documentation]    Uploads the simplest opportunity profile template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleopportunityprofiletemplate.docx
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Upload a simple resume template
    [Documentation]    Uploads the simplest resume template
    ${tname}=   Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    set test variable  ${file}  C:/Users/autouser/Documents/robotframework/org/Publisher Templates/simpleresumetemplate.docx
    Upload a template document  ${file}  ${tname}
    [Return]    ${tname}

Create new generic project profile document 
    [Documentation]   Creates a new project profile doc using the template name
    [Arguments]   ${template}  ${HOST}
    go to   ${HOST}/publisher30/document_create.cfm?documentType=Project%20Profile
    ${document name}=  Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]
    Wait Until Element Is Visible  ${pbdocnew name}
    input text  ${pbdocnew name}  ${document name}
    input text  ${pbdocnew project}  test project  # there's a delay with these.  animation and all.
    sleep  1
    Click-Object  xpath=//div[@class='CLFListItem']/b[text()='test project']  # Note to self, this is a standard thing, standardize it global
    sleep  1  # these things take a minute to select.  If you move away, it sometimes clears it.
    Click-Object  ${pbdocnew save doc}
    select a word template  ${template}
    [return]  ${document name}

Create new generic project list document 
    [Documentation]   Creates a new project list doc using the template name
    [Arguments]   ${template}  ${HOST}
    go to   ${HOST}/publisher30/document_create.cfm?documentType=Project%20List
    ${document name}=  Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]  
    Wait Until Element Is Visible  ${pbdocnew name}
    input text  ${pbdocnew name}  ${document name}
    Click-Object  ${pbdocnew save doc}
    select a word template  ${template}
    [return]  ${document name}

Create new generic opportunity profile document 
    [Documentation]   Creates a new project profile doc using the template name
    [Arguments]   ${template}  ${HOST}
    go to   ${HOST}/publisher30/document_create.cfm?documentType=Opportunity%20Profile
    ${document name}=  Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]  
    Wait Until Element Is Visible  ${pbdocnew name}
    input text  ${pbdocnew name}  ${document name}
    input text  ${pbdocnew opportunity}  test opportunity  # there's a delay with these.  animation and all.
    sleep  1
    Click-Object  xpath=//div[@class='CLFListItem']/b[text()='Test Opportunity']  # Note to self, this is a standard thing, standardize it global
    sleep  1  # these things take a minute to select.  If you move away, it sometimes clears it.
    Click-Object  ${pbdocnew save doc}
    select a word template  ${template}
    [return]  ${document name}

Create new generic resume document 
    [Documentation]   Creates a new resume doc using the template name
    [Arguments]   ${template}  ${HOST}
    go to   ${HOST}/publisher30/document_create.cfm?documentType=resume
    ${document name}=  Generate Random String    25    [LETTERS][NUMBERS][UPPER][LOWER]  
    Wait Until Element Is Visible  ${pbdocnew name}
    input text  ${pbdocnew name}  ${document name}
    input text  ${pbdocnew resume}  test human  # there's a delay with these.  animation and all.
    sleep  2
    Click-Object  xpath=//div[contains(@class, 'CLFListItem')]/b[text()='test human']  # Note to self, this is a standard thing, standardize it global
    sleep  1  # these things take a minute to select.  If you move away, it sometimes clears it.
    Click-Object  ${pbdocnew save doc}
    select a word template  ${template}
    [return]  ${document name}

Select a word template
    [Documentation]  Selects a word template when on a publisher document
    [Arguments]  ${template}
    Click-Object  ${pdoc select word temp}
    Wait Until Keyword Succeeds  5 times  30s  Select Window   NEW
    ${available templates}=  get webelements  xpath=//div[text()='${template}']/../../td[1]/div/input
    Click-Object  ${available templates[0]}
    click-object  xpath=//input[@name='Action']
    handle alert  action=ACCEPT
    ${windows}=  Get Window Handles
    select window  ${windows[1]}
    sleep  5

select projects for the project list
    [Documentation]  Selects a project for the project list criteria
    Click-Object  ${pdoc plist open search}
    Wait Until Keyword Succeeds  5 times  30s  Select Window  NEW
    input text  ${pdoc plist input name}  test project
    Click-Object  ${pdoc plist search}
    Click-Object  xpath=//a[text()='test project']/../../../td/input[@name='selectedProject']
    click-object  ${pdoc plist save}
    ${windows}=  Get Window Handles
    select window  ${windows[1]}
    sleep  5  # for the obligatory refresh wait.

Download the generic publisher word document and verify template variables were replaced
    [Documentation]  downloads the word document, and verifies the template has been updated
    [Arguments]  ${template}  ${document type}
    Click-Object  ${pdocnew download word}
    sleep  5  # wait for it to download.
    ${doc text}=  get text from downloaded docx  c:/users/autouser/downloads/  ${template}
    ${res}=  verify no variables in list  ${doc text}
    ${other res}=  verify template variables replaced  ${doc text}  ${document type}
    should be true  ${res}==True
    should be true  ${other res}==True

Download the generic publisher idml document and verify template variables were replaced
    [Documentation]  downloads the idml document, and verifies the template has been updated
    [Arguments]  ${template}  ${document type}
    Click-Object  ${pdocnew download idml}
    sleep  10  # wait for it to download.
    ${doc text}=  get content from idml template  c:/users/autouser/downloads/  ${template}.idml
    ${res}=  verify no variables in list  ${doc text}
    ${other res}=  verify template variables replaced  ${doc text}  ${document type}
    should be true  ${res}==True
    should be true  ${other res}==True
