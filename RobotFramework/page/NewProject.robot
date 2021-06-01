*** Variables ***
${lbl_NewProj_Header}    xpath=//td//b[text()='Project Summary Information']

#Project Details Section
${txt_NewProj_ProjDetails_ProjName}    xpath=//input[@name='ProjectName']

#Bottom Buttons
${btn_NewProj_CreateProj}    xpath=//input[@type='submit']