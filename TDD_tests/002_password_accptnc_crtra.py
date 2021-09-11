from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from random import randint

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

# 6. Select a day of birth
wait.until(EC.presence_of_element_located(D_BRTH)).click()
wait.until(EC.presence_of_element_located(D_BRTH)).send_keys(8)

# 7. Select a month of birth
wait.until(EC.presence_of_element_located(M_BRTH)).click()
wait.until(EC.presence_of_element_located(M_BRTH)).send_keys('August')

# 8. Select a year of birth
wait.until(EC.presence_of_element_located(Y_BRTH)).click()
wait.until(EC.presence_of_element_located(Y_BRTH)).send_keys(1918)

# 9. Send email
password = str(randint(1000000000, 9999999999))
name = 'name' + "_" + str(password)
last_name = name + "_" + str(password)
email = (name + '@sample.com')
print(f'\nName: {name}, \nlast name: {last_name},\nemail: {email} \nand password: {password}')
wait.until(EC.presence_of_element_located(E_ML)).click()
wait.until(EC.presence_of_element_located(E_ML)).send_keys(email)

# 10. Send phone
wait.until(EC.presence_of_element_located(PHN_FLD)).clear()
wait.until(EC.presence_of_element_located(PHN_FLD)).send_keys(password)

# 11. Send mobile phone
wait.until(EC.presence_of_element_located(M_PHN_FLD)).clear()
wait.until(EC.presence_of_element_located(M_PHN_FLD)).send_keys(password[::-1])

# 12. Send address line one
wait.until(EC.presence_of_element_located(ADDRSS_LN_ON)).clear()
wait.until(EC.presence_of_element_located(ADDRSS_LN_ON)).send_keys('1450 Pennsylvania Avenue NW')

# 13. Send address line two
wait.until(EC.presence_of_element_located(ADDRSS_LN_TW)).clear()
wait.until(EC.presence_of_element_located(ADDRSS_LN_TW)).send_keys('Washington, DC 20230')

# 14. Send city
wait.until(EC.presence_of_element_located(CTY)).clear()
wait.until(EC.presence_of_element_located(CTY)).send_keys('Washington')

# 15. Send county
wait.until(EC.presence_of_element_located(CNTY)).clear()
wait.until(EC.presence_of_element_located(CNTY)).send_keys('Fudzy')

# 16. Send post code
wait.until(EC.presence_of_element_located(PST_CD)).clear()
wait.until(EC.presence_of_element_located(PST_CD)).send_keys(20230)

# 17. Select a country
wait.until(EC.presence_of_element_located(CNTRY)).click()
wait.until(EC.presence_of_element_located(CNTRY)).send_keys('TOGO')

# 18. Send user name
wait.until(EC.presence_of_element_located(USR_NM)).clear()
wait.until(EC.presence_of_element_located(USR_NM)).send_keys('firstName')

# 19. Send password
psswrd_cntrl = 'one1Two@'
flag = 0
while True:
    if (len(psswrd_cntrl) < 7):
        flag = -1
        break
    elif not re.search("[a-z]", psswrd_cntrl):
        flag = -1
        break
    elif not re.search("[A-Z]", psswrd_cntrl):
        flag = -1
        break
    elif not re.search("[0-9]", psswrd_cntrl):
        flag = -1
        break
    elif not re.search("[_@$]", psswrd_cntrl):
        flag = -1
        break
    elif re.search("\s", psswrd_cntrl):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print(f'Not a Valid Password", {psswrd_cntrl}, {len(psswrd_cntrl)}')
wait.until(EC.presence_of_element_located(PSWRD)).clear()
wait.until(EC.presence_of_element_located(PSWRD)).send_keys(psswrd_cntrl)

# 20. Resend password
wait.until(EC.presence_of_element_located(RSND_PSWD)).clear()
wait.until(EC.presence_of_element_located(RSND_PSWD)).send_keys(psswrd_cntrl)
print(psswrd_cntrl, len(psswrd_cntrl))

# 21. Select sequrity question
wait.until(EC.presence_of_element_located(SCRT_QSTN)).click()
wait.until(EC.presence_of_element_located(SCRT_QSTN)).send_keys('What was your childhood nickname?')

# 22. Send answer to security question
wait.until(EC.presence_of_element_located(ANSWR_T_SCRT_QSTN)).clear()
wait.until(EC.presence_of_element_located(ANSWR_T_SCRT_QSTN)).send_keys('Qui pro')

# 23. Select security question two
wait.until(EC.presence_of_element_located(SCRT_QSTN_TW)).click()
wait.until(EC.presence_of_element_located(SCRT_QSTN_TW)).send_keys('Where were you born?')

# 24. Send answer to security question two
wait.until(EC.presence_of_element_located(RSND_PSWD)).clear()
wait.until(EC.presence_of_element_located(RSND_PSWD)).send_keys('Qui pro')

# 25. Send answer to security question two
wait.until(EC.presence_of_element_located(ANSWR_T_SCRT_QSTN_TW)).clear()
wait.until(EC.presence_of_element_located(ANSWR_T_SCRT_QSTN_TW)).send_keys('No one else')

# 26. Select currency
wait.until(EC.presence_of_element_located(CRRNCY)).click()
wait.until(EC.presence_of_element_located(CRRNCY)).send_keys('Pounds Sterling')

# 27. Click checkbox >18 years
wait.until(EC.presence_of_element_located(CHCK_BX_EIGHTNYRS)).click()

# 28. Click Join Now button
wait.until(EC.presence_of_element_located(SBMT_BTN)).click()

# driver.close()

# Sleep to see what we have
# sleep(4)

# # Driver quit
# driver.quit()
