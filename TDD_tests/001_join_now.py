from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

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
CRRNCY = (By.XPATH, "//select[@name='map(currency)']")
CHCK_BX_EIGHTNYRS = (By.XPATH, "//input[@name='map(terms)']")
DT_OF_BRTH_RQRD = (By.XPATH, "//label[@for='dob']")
SBMT_BTN = (By.CSS_SELECTOR, "input#form.promoReg.green")
LBL_AGE_HR = (By.XPATH, "(//label[@class='error'])[18]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://moneygaming.qa.gameaccount.com/' )

# 2. Click on Join Now button
wait.until(EC.element_to_be_clickable(JN_NW)).click()

# 3. Select a title value from the dropdown
wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).click()
wait.until(EC.presence_of_element_located(TTL_DRPDNMN)).send_keys('Mr')

# 4. Fill the First Name field
wait.until(EC.presence_of_element_located(FRST_NM)).clear()
wait.until(EC.presence_of_element_located(FRST_NM)).send_keys('firstName')

# 5. Fill the Surname field
wait.until(EC.presence_of_element_located(SR_NM)).clear()
wait.until(EC.presence_of_element_located(SR_NM)).send_keys('surName')

# 5. Click checkbox 18 years is a minimum CHCK_BX_EIGHTNYRS
wait.until(EC.presence_of_element_located(CHCK_BX_EIGHTNYRS)).click()

# 7. Click Join Now button
wait.until(EC.presence_of_element_located(SBMT_BTN)).click()

# 8. Verify text "This field is required" is here
expected_text = "This field is required"
actual_text = wait.until(EC.visibility_of_element_located(DT_OF_BRTH_RQRD)).text
print(f'Actual text: "{actual_text}"')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

driver.close()

# Sleep to see what we have
sleep(4)

# Driver quit
driver.quit()


