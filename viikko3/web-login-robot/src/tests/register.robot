*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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

Login After Successful Registration
    Set Username  kaija
    Set Password  kaija123
    Set Password Confirmation  kaija123
    Submit Credentials
    Register Should Succeed
    Switch To Login Page
    Set Username  kaija
    Set Password  kaija123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kaija
    Set Password  kaija123
    Set Password Confirmation  123
    Submit Credentials
    Register Should Fail With Message  Password confirmation doesn't match
    Switch To Login Page
    Set Username  kaija
    Set Password  kaija123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Submit Credentials
    Submit Register Credentials

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Switch To Login Page
    Go To Login Page
    Login Page Should Be Open
