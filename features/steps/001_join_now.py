from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()


@then("Click on Join Now button")
def clck_jn_nw_btn(context):
    """
    Click on Join Now button
    """
    context.app.main_page.clck_jn_nw_btn()


@then("Select a title in the dropdown '{mr}'")
def ttl_vl_drp_dwn_mn(context, mr):
    """
    Select a title in the dropdown "Mr"
    """
    context.app.main_page.tl_vl_drp_dwn_mn(mr)


@step("Fill the First Name field '{f_t}'")
def frst_nm(context, f_t):
    """
    Fill the First Name field
    """
    context.app.main_page.frst_nm(f_t)

@step("Fill the Surnme field '{s_n}'")
def sr_nm(context, s_n):
    """
    Fill the Surnme field 'surName'
    """
    context.app.main_page.sr_nm(s_n)


@then("Click Join Now button")
def jn_btn(context):
    """
    Click Join Now button
    """
    context.app.main_page.jn_btn()


@step("Verify text '{tx_hr}' is here")
def txt_hr(context, tx_hr):
    """
    Verify text 'This field is required' is here
    """
    context.app.main_page.txt_hr(tx_hr)