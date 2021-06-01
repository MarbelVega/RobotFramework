*** Settings ***
Library    SeleniumLibrary
Library    String
Resource    ../../../../Universal/UniversalKeywords.robot
Resource    ../../../PageObjs/Modules/Login/LoginPage.robot
Resource    ../../../PageObjs/Global/GlobalVariables.robot
Resource    ../../../PageObjs/Modules/Products/Products.robot
Resource    ../../../PageObjs/Modules/Products/AddProduct.robot
Resource    ../../../PageObjs/Modules/Products/AddServices.robot
Resource    ../../../PageObjs/Modules/Products/Services.robot
Resource    ../../../PageObjs/Modules/Products/AddLabor.robot
Resource    ../../../PageObjs/Modules/Products/Labor.robot
Resource    ../../../PageObjs/Modules/Products/Kits.robot
Resource    ../../../PageObjs/Modules/Products/AddKits.robot
Resource    ../../../PageObjs/Modules/Products/PriceBooks.robot
Resource    ../../../PageObjs/Modules/Products/AddPriceBooks.robot
#Test Teardown    Close Browser

*** Variables ***
#${URL}    http://integration.orgdev.com
#${URL}    https://services-staging.orgdev.com/
${URL}    https://services-qe.orgdev.com
#${URL}    http://services.org.com/

*** Test Cases ***
Add Product With All Possible Fields
    [Documentation]    Create a new Product on the Product Page and add data in all possible fields.
    [Tags]    Products    Smart Tables
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Products}
    Click-Object    ${btn_Products_AddProd}
    ${name}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddProduct_Name}    ${name}
    Enter-Text    ${txt_AddProduct_Manufacturer}    Automation
    Click-Object    ${btn_AddPRoduct_ManufacturerFirstRow}
    #Press Keys    none    \ue004
    Select From Dropdown By Text    ${slt_AddProduct_Unit}    Select
    Random String    ${txt_AddProduct_ProdAbbrev}    5
    Random Numbers    ${txt_AddProduct_UnitCost}    5
    Random String    ${txt_AddProduct_Desc}    50
    Random Numbers    ${txt_AddProduct_UnitPrice}    5
    Random String    ${txt_AddProduct_ProdSKU}    10
    Select From Dropdown By Text    ${slt_AddProduct_BillCycle}    Select
    Random String    ${txt_AddProduct_ProdCode}    10
    Select From Dropdown By Text    ${slt_AddProduct_GLAcc}    Select
    Select From Dropdown By Text    ${slt_AddProduct_Type}    Select
    Select From Dropdown By Text    ${slt_AddProduct_SLA}    Select
    Select From Dropdown By Text    ${slt_AddProduct_Family}    Select
    Enter-Text    ${txt_AddProduct_WarrantyTerm}    2
    Select From Dropdown By Text    ${slt_AddProduct_WarrantyUnit}    Year(s)
    Enter-Text    ${txt_AddProduct_Commission}    10
    Select From Dropdown By Text    ${slt_AddProduct_Status}    Select
    Select From Dropdown By Text    ${slt_AddProduct_Discounts}    Not Allowed
    Select Frame    ${iframe_AddProducts_ProdDetailsFrame}
    Random String    ${txt_AddProduct_ProdDetails}    100
    Unselect Frame
    Select Firm Org By Text    ${btn_AddProduct_AddOffice}    Office1
    Select Firm Org By Text    ${btn_AddProduct_AddPractArea}    PA Two
    #Select Firm Org By Text    ${btn_AddProduct_AddDivs}    Text
    #Select Firm Org By Text    ${btn_AddProduct_AddTerrs}    Text
    Select Firm Org By Text    ${btn_AddProduct_AddStudios}    Studio Two
    Sleep    5
    Click-Object    ${btn_AddProduct_Save}
    Click-Object   ${btn_AddProduct_ProductTab}
    Sleep    3
    Validate Product Name In Table    ${name}
    
Add Service With All Possible Fields
    [Documentation]    Create a new Service on the Product Page and add data in all possible fields.
    [Tags]    Products    Smart Tables
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Products}
    Click-Object    ${btn_Services_Tab}
    Sleep    2
    #Wait Until Element Is Visible    ${btn_Products_AddServices}    60s    page did not load within 60s
    Click-Object    ${btn_Products_AddServices} 
    ${name}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddServices_Name}    ${name}
    Random String    ${txt_AddServices_ServAbbrev}    5
    Select From Dropdown By Text_Services    ${slt_AddServices_Unit}    Unit 1
    #Random String    ${txt_AddServices_ProdAbbrev}    5
    Random Numbers    ${txt_AddServices_UnitCost}    5
    Random String    ${txt_AddServices_Desc}    50
    Random Numbers    ${txt_AddServices_UnitPrice}    5
    Random String    ${txt_AddServices_ServSKU}    10
    Select From Dropdown By Text_Services    ${slt_AddServices_BillCycle}    BL 1
    Random String    ${txt_AddServices_ServiceCode}    10
    Select From Dropdown By Text_Services    ${slt_AddServices_GLAcc}    G/L Account 1
    Select From Dropdown By Text_Services    ${slt_AddServices_Type}    Type 1
    Select From Dropdown By Text_Services   ${slt_AddServices_SLA}    SLA 1
    Select From Dropdown By Text_Services    ${slt_AddServices_Family}    Family 1
    Enter-Text    ${txt_AddServices_WarrantyTerm}    2
    Select From Dropdown By Text_Services    ${slt_AddServices_WarrantyUnit}    Year(s)
    Enter-Text    ${txt_AddProduct_Commission}    10
    Select From Dropdown By Text_Services    ${slt_AddServices_Status}    Status 1
    Select From Dropdown By Text_Services    ${slt_AddServices_Discounts}    Not Allowed
    Select Firm Org By Text_Services    ${btn_AddServices_AddOffice}    Office1
    Select Firm Org By Text_Services    ${btn_AddServices_AddPractArea}    PA Two
    #Select Firm Org By Text    ${btn_AddProduct_AddDivs}    Text
    #Select Firm Org By Text    ${btn_AddProduct_AddTerrs}    Text
    Select Firm Org By Text_Services    ${btn_AddServices_AddStudios}    Studio Two
    Click-Object    ${btn_AddServices_Save}
    Click-Object    ${btn_Services_Tab} 
    Validate Service Name In Table    ${name}
    
    
Add Labor With All Possible Fields
    [Documentation]    Create a new Labor on the Product Page and add data in all possible fields.
    [Tags]    Products    Smart Tables
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Products}
    Click-Object    ${btn_Labor_Tab}
    Sleep    3
    Click-Object    ${btn_Products_NewLabor} 
    ${name}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddUnion_Name}    ${name}
    Select Details_Drop Down By Text_Labor    ${btn_AddLabor_unionLocation}    Union Location1    
    #Sleep    1  
    #Select Details_Drop Down By Text_Labor    ${btn_AddLabor_LabourTypes}     Type1 
    #Select Details_Drop Down By Text_Labor    ${btn_AddLabor_TimesTypes}    TimeType1
    Click-Object    ${btn_Labor_IndexTab}
    Validate Labor Name In Table    ${name}
    
Add kids With All Possible Fields
    [Documentation]    Create a new Kids on the Product Page and add data in all possible fields.
    [Tags]    Products    Smart Tables
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Products}
    Sleep    2
    Click-Object    ${btn_Kits_Tab}
    Sleep    2
    #Wait Until Element Is Visible    ${btn_Products_AddServices}    60s    page did not load within 60s
    Click-Object    ${btn_Products_AddKits} 
    
    ${name}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddKits_Name}    ${name}
    Random String    ${txt_AddKits_KitAbbrev}    5
    Random String    ${txt_AddKits_Desc}    50
    Random String    ${txt_AddKits_KitsSKU}    10
    Random String    ${txt_AddKits_KitsCode}    10
    Select From Dropdown By Text_Kits    ${slt_AddKits_Type}    Select
    Select From Dropdown By Text_Kits    ${slt_AddKits_Family}    Select
    Enter-Text    ${txt_AddKits_Commission}    10
    Random Numbers    ${txt_AddKits_KitPrice}    5
    Select From Dropdown By Text_Kits    ${slt_AddKits_BillCycle}    Select
    Select From Dropdown By Text_Kits   ${slt_AddKits_SLA}    Select
    Enter-Text    ${txt_AddKits_ProductWarrantyTerm}    2
    Select From Dropdown By Text_Kits    ${slt_AddKits_ProductWarrantyunit}    Year(s)
    Enter-Text    ${txt_AddKits_ServiceWarrantyTerm}    2
    Select From Dropdown By Text_Kits    ${slt_AddKits_ServiceWarrantyunit}    Year(s)
    Enter-Text    ${txt_AddKits_LaborWarrantyTerm}    2
    Select From Dropdown By Text_Kits    ${slt_AddKits_LaborWarrantyunit}    Year(s)
    Select From Dropdown By Text_Kits    ${slt_AddKits_Status}    Select
    Select From Dropdown By Text_Kits    ${slt_AddKits_Discounts}    Not Allowed


    Select Firm Org By Text_Services    ${btn_AddServices_AddOffice}    Office1
    Select Firm Org By Text_Services    ${btn_AddServices_AddPractArea}    PA Two
    #Select Firm Org By Text    ${btn_AddProduct_AddDivs}    Text
    #Select Firm Org By Text    ${btn_AddProduct_AddTerrs}    Text
    Select Firm Org By Text_Services    ${btn_AddServices_AddStudios}    Studio Two
    Click-Object    ${btn_AddServices_Save}
    Click-Object    ${btn_Kits_Tab} 
    Validate Service Name In Table    ${name}
      
      
Add Price Books With All Possible Fields
    [Documentation]    Create a new PriceBooks on the Product Page and add data in all possible fields.
    [Tags]    Products    Smart Tables
    Login-WebApp    ${URL}
    Click-Object    ${GlobalNav_Products}
    Sleep    2
    Click-Object    ${btn_PB_Tab}
    Sleep    2
    Click-Object    ${btn_Products_AddPB} 
    ${name}    Generate Random String    20    [LETTERS][NUMBERS][UPPER][LOWER]
    Enter-Text    ${txt_AddPB_Name}    ${name}
    Random String    ${txt_AddPB_Desc}    50
    Random String    ${txt_AddPB_Commission}   10
    Random String    ${txt_AddPB_ListPriceAdjustment}     5
    Click-Object    ${btn_AddPB_Save}
    Click-Object    ${btn_PB_Tab} 
    Validate PriceBooks Name In Table    ${name}
   

