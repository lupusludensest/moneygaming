from behave import *


@then("Fill all fields and choose options before entering password")
def fll_evrthg_bf_pswd(context):
    """
    Fill all fields and choose options before entering password
    """
    context.app.main_page.fll_evrthg_bf_pswd()


@step('Send password {pswrd} verify it is at least {ln_ch} chars length, has {dgts} and {spcs}')
def snd_pswd(context, pswrd, ln_ch, dgts, spcs):
    """
    Send password one1Two@ verify it is at least 6 chars length, has "[0-9]" and "[_@$]"
    """
    context.app.main_page.snd_pswd(pswrd, ln_ch, dgts, spcs)

@then("Resend password {pswrd} verify it is at least {ln_ch} chars length, has {dgts} and {spcs}")
def rsnd_pswd(context, pswrd, ln_ch, dgts, spcs):
    """
    Resend password 'one1Two@' verify it is at least 6 chars length, has "[0-9]" and "[_@$]"
    """
    context.app.main_page.rsnd_pswd(pswrd, ln_ch, dgts, spcs)