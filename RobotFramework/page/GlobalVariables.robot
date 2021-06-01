*** Variables ***

#QA Admin Env
${QA_Admin_URL}    http://qa.org.com/administration20/admin/
${QA_Admin_UserName}    noreply
${QA_Admin_Password}    asheyY247

#QA Customer Env
${QA_URL}    https://qa.org.com/
${QA_UserName}    sprintuser
${QA_Password}    Devaccount123!
${QA_Firm_1}    1

#DevInt Admin Env
${DevInt_Admin_URL}    http://integration.org.com/administration20/admin/
${DevInt_Admin_UserName}    noreply
${DevInt_Admin_Password}    aksheyY247

#DevInt Customer Env
${DevInt_URL}    http://integration.org.com
${DevInt_UserName}    emason
${DevInt_Password}    w3lcom3
${DevInt_Firm_783}    783

#Staging Env
${Staging_URL}    https://services-staging.org.com/
${Staging_UserName}    autouser
${Staging_Password}    QC2EVKHP6zs8buE2^pBrNXtz
${Staging_Firm_1}    822
${Staging_Admin}    autouser
${Staging_Admin_Password}   1234$#@!a

#Global Navigation Menu Objects
${GlobalNav_Home}    xpath=(//*[text()='Home'])[1]
${GlobalNav_ContactManager}    xpath=//span[text()='Contact Manager']
${GlobalNav_Personnel}    xpath=//span[text()='Personnel']
${GlobalNav_Projects}    xpath=//span[text()='Projects']
${GlobalNav_Reports}    xpath=//span[text()='Reports']
${GlobalNav_Publisher}    xpath=//span[text()='Publisher 4.0']
${GlobalNav_Admin}    xpath=//span[text()='Administration']
${GlobalNav_Activities}    xpath=//span[text()='Activities']
${GlobalNav_Marketing}    xpath=//span[text()='Marketing']
${GlobalNav_Goals}    xpath=//span[text()='Goals']
${GlobalNav_Products}    xpath=//span[text()='Products']
${GlobalNav_Properties}    xpath=//span[text()='Properties']