from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
import re
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
import time

# Locators
JN_NW = (By.CSS_SELECTOR, "a.newUser.green")
FRST_NM = (By.ID, "forename")
SR_NM = (By.XPATH, "//input[@name='map(lastName)']")
TTL_DRPDNMN = (By.ID, "title")
D_BRTH = (By.ID, "dobDay")
M_BRTH = (By.ID, "dobMonth")
Y_BRTH = (By.ID, "dobYear")
E_ML = (By.XPATH, "//input[@name='map(email)']")
PHN_FLD = (By.CSS_SELECTOR, "input.required.telephoneNumber")
M_PHN_FLD= (By.CSS_SELECTOR, "input.required.mobileNumber")
ADDRSS_LN_ON = (By.CSS_SELECTOR, "input.full.required")
ADDRSS_LN_TW = (By.XPATH, "//input[@name='map(address2)']")
CTY = (By.XPATH, "//input[@name='map(addressCity)']")
CNTY = (By.XPATH, "//input[@name='map(stateProv)']")
PST_CD = (By.XPATH, "//input[@name='map(postCode)']")
CNTRY = (By.CSS_SELECTOR, "select#countryList.required")
USR_NM = (By.XPATH, "//input[@name='map(userName)']")
PSWRD = (By.CSS_SELECTOR, "input#\password.required.autocomplete-off")
RSND_PSWD = (By.XPATH, "//input[@name='map(passwordConfirm)']")
SCRT_QSTN = (By.ID, "securityQuestionOne")
ANSWR_T_SCRT_QSTN = (By.XPATH , "//input[@name='map(securityAnswerOne)']")
SCRT_QSTN_TW = (By.XPATH, "//select[@name='map(securityQuestionTwo)']")
ANSWR_T_SCRT_QSTN_TW = (By. XPATH, "//input[@name='map(securityAnswerTwo)']")
# ANSWR_T_SCRT_QSTN_TW = (By.XPATH, "//option[@value='Where were you born?']")
CRRNCY = (By.XPATH, "//select[@name='map(currency)']")
CHCK_BX_EIGHTNYRS = (By.XPATH, "//input[@name='map(terms)']")
DT_OF_BRTH_RQRD = (By.XPATH, "//label[@for='dob']")
SBMT_BTN = (By.CSS_SELECTOR, "input#form.promoReg.green")
LBL_AGE_HR = (By.XPATH, "(//label[@class='error'])[18]")

class MainPage(Page):

    # 001_join_now
    # Click on Join Now button
    def clck_jn_nw_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(JN_NW)).click()
    # End of the above code

    # Select a title in the dropdown "Mr"
    def tl_vl_drp_dwn_mn(self, mr):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).click()
        wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).send_keys(mr)
    # End of the above code

    # Fill the First Name field
    def frst_nm(self, f_t):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(FRST_NM)).clear()
        wait.until(EC.presence_of_element_located(FRST_NM)).send_keys(f_t)
    # End of the above code

    # Fill the First Name field
    def sr_nm(self, s_n):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(SR_NM)).clear()
        wait.until(EC.presence_of_element_located(SR_NM)).send_keys(s_n)
    # End of the above code

    # Click Join Now button
    def jn_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(SBMT_BTN)).click()
    # End of the above code

    # Verify text 'This field is required' is here
    def txt_hr(self,tx_hr):
        wait = WebDriverWait(self.driver, 10)
        expected_text = tx_hr
        actual_text = wait.until(EC.visibility_of_element_located(DT_OF_BRTH_RQRD)).text
        print(f'Actual text: "{actual_text}"')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
    # End of the above code

    # 002_password_accptnc_crtra
    # Fill all fields and choose options before entering password
    def fll_evrthg_bf_pswd(self):
        wait = WebDriverWait(self.driver, 10)
        # Click on Join Now button
        wait.until(EC.element_to_be_clickable(JN_NW)).click()

        # Select a title value from the dropdown
        wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).click()
        wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).send_keys('Mr')

        # Fill the First Name field
        wait.until(EC.presence_of_element_located(FRST_NM)).clear()
        wait.until(EC.presence_of_element_located(FRST_NM)).send_keys('firstName')

        # Fill the Surname field
        wait.until(EC.presence_of_element_located(SR_NM)).clear()
        wait.until(EC.presence_of_element_located(SR_NM)).send_keys('surName')

        # Select a day of birth
        wait.until(EC.presence_of_element_located(D_BRTH)).click()
        wait.until(EC.presence_of_element_located(D_BRTH)).send_keys(8)

        # Select a month of birth
        wait.until(EC.presence_of_element_located(M_BRTH)).click()
        wait.until(EC.presence_of_element_located(M_BRTH)).send_keys('August')

        # Select a year of birth
        wait.until(EC.presence_of_element_located(Y_BRTH)).click()
        wait.until(EC.presence_of_element_located(Y_BRTH)).send_keys(1918)

        # Send email
        password = str(randint(1000000000, 9999999999))
        name = 'name' + "_" + str(password)
        last_name = name + "_" + str(password)
        email = (name + '@sample.com')
        print(f'\nName: {name}, \nlast name: {last_name},\nemail: {email} \nand password: {password}')
        wait.until(EC.presence_of_element_located(E_ML)).click()
        wait.until(EC.presence_of_element_located(E_ML)).send_keys(email)

        # Send phone
        wait.until(EC.presence_of_element_located(PHN_FLD)).clear()
        wait.until(EC.presence_of_element_located(PHN_FLD)).send_keys(password)

        # Send mobile phone
        wait.until(EC.presence_of_element_located(M_PHN_FLD)).clear()
        wait.until(EC.presence_of_element_located(M_PHN_FLD)).send_keys(password[::-1])

        # Send address line one
        wait.until(EC.presence_of_element_located(ADDRSS_LN_ON)).clear()
        wait.until(EC.presence_of_element_located(ADDRSS_LN_ON)).send_keys('1450 Pennsylvania Avenue NW')

        # Send address line two
        wait.until(EC.presence_of_element_located(ADDRSS_LN_TW)).clear()
        wait.until(EC.presence_of_element_located(ADDRSS_LN_TW)).send_keys('Washington, DC 20230')

        # Send city
        wait.until(EC.presence_of_element_located(CTY)).clear()
        wait.until(EC.presence_of_element_located(CTY)).send_keys('Washington')

        # Send county
        wait.until(EC.presence_of_element_located(CNTY)).clear()
        wait.until(EC.presence_of_element_located(CNTY)).send_keys('Fudzy')

        # Send post code
        wait.until(EC.presence_of_element_located(PST_CD)).clear()
        wait.until(EC.presence_of_element_located(PST_CD)).send_keys(20230)

        # Select a country
        wait.until(EC.presence_of_element_located(CNTRY)).click()
        wait.until(EC.presence_of_element_located(CNTRY)).send_keys('TOGO')

        # Send user name
        wait.until(EC.presence_of_element_located(USR_NM)).clear()
        wait.until(EC.presence_of_element_located(USR_NM)).send_keys('firstName')
    # End of the above code

    # Send password 'one1Two@'
    def snd_pswd(self, pswrd, ln_ch, dgts, spcs):
        d_ln_ch = int(ln_ch)
        wait = WebDriverWait(self.driver, 10)
        flag = 0
        while True:
            if (len(pswrd) <= d_ln_ch):
                flag = -1
                break
            elif not re.search("[a-z]", pswrd):
                flag = -1
                break
            elif not re.search("[A-Z]", pswrd):
                flag = -1
                break
            elif not re.search(dgts, pswrd):
                flag = -1
                break
            elif not re.search(spcs, pswrd):
                flag = -1
                break
            elif re.search("\s", pswrd):
                flag = -1
                break
            else:
                flag = 0
                print("Valid Password")
                break

        if flag == -1:
            print(f'Not a Valid Password": {pswrd}, {len(pswrd)}')
        wait.until(EC.presence_of_element_located(PSWRD)).clear()
        wait.until(EC.presence_of_element_located(PSWRD)).send_keys(pswrd)
   # End of the above code

   # Resend password 'one1Two@'
    def rsnd_pswd(self, pswrd, ln_ch, dgts, spcs):
        d_ln_ch = int(ln_ch)
        wait = WebDriverWait(self.driver, 10)
        flag = 0
        while True:
            if (len(pswrd) <= d_ln_ch):
                flag = -1
                break
            elif not re.search("[a-z]", pswrd):
                flag = -1
                break
            elif not re.search("[A-Z]", pswrd):
                flag = -1
                break
            elif not re.search(dgts, pswrd):
                flag = -1
                break
            elif not re.search(spcs, pswrd):
                flag = -1
                break
            elif re.search("\s", pswrd):
                flag = -1
                break
            else:
                flag = 0
                print("Valid Password")
                break

        if flag == -1:
            print(f'Not a Valid Password": {pswrd}, {len(pswrd)}')
        wait.until(EC.presence_of_element_located(RSND_PSWD)).clear()
        wait.until(EC.presence_of_element_located(RSND_PSWD)).send_keys(pswrd)
    # End of the above code










