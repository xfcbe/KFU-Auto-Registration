from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import colorama
from colorama import Fore

i = 0
crn = []
corses = int(input('how many courses do you have: '))
for x in range(corses):
	crn_codes= input('enter the crn code for the course number '+ str(x+1)+': ')
	crn.append(crn_codes)

username= input(Fore.RED+'enter your student id ')
password= input(Fore.RED+'enter your password ')
check = input(Fore.GREEN+"do you have a veryfi key? (y\n) ")
if (check == "y"):
	verify = input(Fore.GREEN+'enter the verify code: ')
	i=i+1
else:
	pass

#def calc_min():
 #   return secndes*60

if __name__ == '__main__':
	url ='https://banner.kfu.edu.sa:7710/PROD_ar/bwskfreg.P_AltPin'
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
		verify = input("Enter the code you receve in your phone: ")
	inputElement2 = driver.find_element_by_name("VerC")
	inputElement2.send_keys(verify)
	inputElement2.send_keys(Keys.ENTER)

	inputElement3 = driver.find_element_by_id("bmenu--P_StuMainMnu___UID1").click()
	login_form = driver.find_element_by_xpath("/html/body/div[@id='content']/div[@id='bodyContainer']/div[@id='pagebody']/div[@id='contentHolder']/div[@id='contentBelt']/div[@id='bmenu--P_RegMnu___UID0']").click()
	#inputElement4 = driver.find_element_by_id("bmenu--P_RegMnu___UID0").click()
	inputElement5 = driver.find_element_by_id("contentItem11").click()
	
	#after this we have to find the path for the page of regstration thin we make a for loop to move in the 
	#crn array and regstir the crn cosdes thin we well be finshed (:).
	print("------------Done------------")