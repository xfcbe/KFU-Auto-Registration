from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
i = 0
crn = []
corses = int(input('how many courses do you have: '))
for x in range(corses):
	crn_codes= input('Enter the crn code for the course number '+ str(x+1)+': ')
	if crn_codes=="":
		pass
	else:
		crn.append(crn_codes)

username= input(Fore.RED+'Enter your student id ')

password= input(Fore.RED+'Enter your password ')

check = input(Fore.GREEN+"do you have a veryfi key? (y\n) ")

if (check == "y"):
	verify = input(Fore.GREEN+'Enter the verify code: ')
	i=i+1
else:
	pass

if __name__ == '__main__':
	url ='https://banner.kfu.edu.sa:7710/PROD_ar/twbkwbis.P_WWWLogin'
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

							# Provide the path of chromedriver present on your system.
	driver = webdriver.Chrome(executable_path="chromedriver",
							chrome_options=options)
	driver.set_window_size(1680,1050)

							# Send a get request to the url
	driver.get(url)
											#login to kfu banar
	inputElement1 = driver.find_element_by_id("UserID")
	inputElement = driver.find_element_by_name("PIN")
	inputElement1.send_keys(username)
	inputElement.send_keys(password)
	inputElement.send_keys(Keys.ENTER)
	if (i==1):
		pass
	else:
		verify = input("Enter the code you receve in your phone: ")
	inputElement2 = driver.find_element_by_name("VerC")
	inputElement2.send_keys(verify)
	inputElement2.send_keys(Keys.ENTER)
	time.sleep(1)
	button3 = driver.find_element_by_id("bmenu--P_StuMainMnu___UID1").click()
	try:

		element = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, "bmenu--P_RegMnu___UID0")))
		element.click()
		element1 = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, "contentItem11")))
		element1.click()
	except:
		driver.quit()
	select = Select(driver.find_element_by_id('term_id'))
	select.select_by_index(1)
	driver.find_element_by_id("id____UID6").click()
												#coursees registration
	for crn_number in crn:
		inputElement3 = driver.find_element_by_id("crn_id1")
		inputElement3.send_keys(crn_number)
		inputElement3.send_keys(Keys.ENTER)
		print(crn_number+" -----> "+Fore.GREEN+"Done")
										
											#confirm the registrations
	for d in range(corses):
		select = Select(driver.find_element_by_id('action_id'+ str(d+1)))		
		select.select_by_value("")
		
											#take a screenshot of a weekly schedule 
	check2 = input("do you want to check your weekly Schedule? Y/N ")

	if check2=='y':
		driver.back()
		driver.back()
		try:
			element = WebDriverWait(driver, 5).until(
			EC.element_to_be_clickable((By.ID, "contentItem110")))
			element.click()
			time.sleep(5)
			driver.save_screenshot('New-Schedule.png')
			print("Screenshot has been taken ")
			driver.quit()
		except:
			driver.quit()
	else:
		driver.quit()
