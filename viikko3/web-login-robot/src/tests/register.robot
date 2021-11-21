*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kaija
    Set Password  kaija123
    Set Password Confirmation  kaija123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kaija123
    Set Password Confirmation  kaija123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kaija
    Set Password  123
    Set Password Confirmation  123
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kaija
    Set Password  kaija123
    Set Password Confirmation  123
    Submit Credentials
    Register Should Fail With Message  Password confirmation doesn't match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

