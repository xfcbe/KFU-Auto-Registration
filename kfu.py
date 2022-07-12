from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore

i = 0
crn = []
corses = int(input('how many courses do you have: '))
for x in range(corses):
	crn_codes= input('Enter CRN code for the course number '+ str(x+1)+': ')
	crn.append(crn_codes)

username= input(Fore.RED+'Enter your student ID ')
password= input(Fore.RED+'Enter your password ')
check = input(Fore.GREEN+"do you have a verify key? (y\n) ")
if (check == "y"):
	verify = input(Fore.GREEN+'Enter the verification code: ')
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
	inputElement1 = driver.find_element_by_id("UserID")
	inputElement = driver.find_element_by_name("PIN")
	inputElement1.send_keys(username)
	inputElement.send_keys(password)
	inputElement.send_keys(Keys.ENTER)
	if (i==1):
		pass
	else:
		verify = input("Enter the code you have received on your phone: ")
	inputElement2 = driver.find_element_by_name("VerC")
	inputElement2.send_keys(verify)
	inputElement2.send_keys(Keys.ENTER)

	button3 = driver.find_element_by_id("bmenu--P_StuMainMnu___UID1").click()
	button4 = driver.find_element_by_id("bmenu--P_RegMnu___UID0").click()
	button5 = driver.find_element_by_id("contentItem11").click()
	
	for crn_number in crn:
		inputElement3 = driver.find_element_by_id("")
		inputElement3.send_keys(crn_number)
		inputElement3.send_keys(Keys.ENTER)
		print(crn_number+" -----> "+Fore.GREEN+"Done")
		
	if check2=='y':
		button6 = driver.find_element_by_id("").click()
		button7 = driver.find_element_by_id("").click()
		time.sleep(3)
		driver.save_screenshot('New-Schedule.png')
		driver.quit()
	else:
		driver.quit()
