from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
				#python -m PyInstaller myscript.py
i = 0
crn = []
corses = int(input('how many courses do you have: '))
for x in range(corses):
	crn_codes= input(f'Enter the crn code for the course number [{str(x+1)}] :')
	if crn_codes=="":
		pass
	else:
		crn.append(crn_codes)

username= input(Fore.RED+'Enter your student ID ')
password= input(Fore.RED+'Enter your PASSWORD ')
check = input(Fore.GREEN+"do you have a veryfi key? (Y/N) ")
if (check == "y"):
	verify = input(Fore.GREEN+'Enter the verify code: ')
	i+=1
else:
	pass

url ='https://banner.kfu.edu.sa:7710/PROD_ar/twbkwbis.P_WWWLogin'
options = webdriver.ChromeOptions()
# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path="chromedriver",
						chrome_options=options)

	# Send a get request to the url
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID,"UserID").send_keys(username)
inputElement = driver.find_element(By.NAME,"PIN")
inputElement.send_keys(password)
inputElement.send_keys(Keys.ENTER)
if (i==1):
	pass
else:
	verify = input("Enter the code that's you receved in your phone: ")
inputElement2 = driver.find_element(By.NAME,"VerC")
inputElement2.send_keys(verify)
inputElement2.send_keys(Keys.ENTER)
time.sleep(1)
button3 = driver.find_element(By.ID,"bmenu--P_StuMainMnu___UID1").click()
try:
	element = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.ID, "bmenu--P_RegMnu___UID0")))
	element.click()
	element1 = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.ID, "contentItem11")))
	element1.click()
except:
	driver.quit()
while True:
	try:
		select = Select(driver.find_element(By.ID,'term_id'))
		select.select_by_index(1)
		driver.find_element(By.ID,"id____UID6").click()
		for crn_number in crn:
			if crn_number==5:
				driver.find_element(By.ID,"id____UID4").click()
			else:
				pass
			inputElement3 = driver.find_element(By.ID,f"crn_id{crn_number+1}")
			inputElement3.send_keys(crn_number)
			crn_number+=1
			print(crn_number+" -----> "+Fore.GREEN+"Done")
		driver.find_element(By.ID,"id____UID4").click()
		break
	except:
		time.sleep(2)
		driver.refresh()
for d in range(corses):
	select = Select(driver.find_element(By.ID,'action_id'+str(d+1)))
	select.select_by_value("RC")
if corses != 0:
	driver.find_element(By.ID,"id____UID4").click()
else:
	pass
check2 = input("do you want to check your weekly Schedule? Y/N ")

if check2=='y':
	driver.back()
	driver.back()
	try:
		element = WebDriverWait(driver, 5).until(
		EC.element_to_be_clickable((By.ID, "contentItem110")))
		element.click()
		time.sleep(5)
		n = random.randint(0,100)
		driver.save_screenshot(f'New-Schedule{n}.png')
		driver.quit()
	except:
		driver.quit()
else:
	driver.quit()