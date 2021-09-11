from behave import *


@then("Fill all fields and choose options before entering password")
def fll_evrthg_bf_pswd(context):
    """
    Fill all fields and choose options before entering password
    """
    context.app.main_page.fll_evrthg_bf_pswd()


@step("Send password '{pswrd}'")
def snd_pswd(context, pswrd):
    """
    Send password 'one1Two@'
    """
    context.app.main_page.snd_pswd(pswrd)

@then("Resend password '{rsnd_pswd}'")
def rsnd_pswd(context, rsnd_pswd):
    """
    Resend password 'one1Two@'
    """
    context.app.main_page.rsnd_pswd(rsnd_pswd)


@step("Fill all fields and choose options after entering password")
def fll_evrthg_ftr_pswd(context):
    """
    Fill all fields and choose options after entering password
    """
    context.app.main_page.fll_evrthg_ftr_pswd()