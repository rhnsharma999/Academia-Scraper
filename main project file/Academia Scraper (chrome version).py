

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import time
import sys

#<-------------------constants here ----------------------------------------------------------->
baseurl='https://academia.srmuniv.ac.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&serviceurl=https://academia.srmuniv.ac.in/'
myproxy = "172.16.0.17:8080"
chromedriver = '/Users/rohanlokeshsharma/Downloads/chromedriver'
#<-------------------constants end here -------------------->


#<-------------------Functi ons------------------>

def printStudentInfo(names):
	print "\n"
	print " {:10s} {:10s}".format('','<------------------------Student Info------------------------>')
	print ""
	i=1
	while(i<len(names)):
		print ' {:30s} {:10s}'.format(names[i-1].text,names[i].text)
		i = i+2
	print ""
	print " {:10s} {:10s}".format('','<------------------------Student Info------------------------>')


def printAtt(info):
	print "\n"
	
	print " {:10s} {:10s}".format('','<------------------------Attendance------------------------>')
	print ""

	print ' {:45s} {:10s}'.format('Subject','Attendance Percentage')
	print ""
	i = 12
	while(i<len(info)):
		print ' {:50s} {:10s}'.format(info[i].text,info[i+9].text)
		i = i+11
	print "" 
	print " {:10s} {:10s}".format('','<------------------------Attendance------------------------>')


def getAttendance(AttendancePage):

	soup = BeautifulSoup(AttendancePage,'html.parser') #parse page

	table = soup.findAll("table",{"width":"707"}) #find the table containing attendance
	data=[]
	info = []
	for i in table:
		data = i.find_all('td') #find all the table data elements
		for j in data:
			info.append(j) #adding the elements to this list

	return info 		#return this list to the calling method

def getStudentInfo(page):
	soup = BeautifulSoup(page,'html.parser')
	names = soup.findAll("table",{"align":"left","cellspacing":"1","cellpadding":"1","border":"0"})

	naam = []
	for i in names:
		data = i.find_all('td')
		for j in data:
			naam.append(j)
	return naam

def getInfo(): #Get user Data

	ls=[]
	a=raw_input("Enter username\n")
	b=getpass.getpass("Enter password\n")
	ls.append(a)
	ls.append(b)
	
	print ""
	return ls


def setProxy(PROXY): #set proxy if needed

	#PROXY = "172.16.0.4:8080"
	webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "autodetect":False
}

def getData(credentials):
	
	try:
		browser = webdriver.Chrome(chromedriver)

		browser.get(baseurl)
		
		print "Logging In"

		
		username = browser.find_element_by_name('username')  #find the field that takes username
		username.send_keys(credentials[0])
		

		password = browser.find_element_by_name('password') #find the field that takes password
		
		password.send_keys(credentials[1])


		#form = browser.find_element_by_id('signinForm')  #find the function that submits the login form
		#form.submit() #submit the form or click the SignIn button
		but = browser.find_element_by_class_name("btn")
		
		but.click()
		time.sleep(2)
		but.click()

		#time.sleep(20)
		
		try:
			element = WebDriverWait(browser, 10).until(EC.title_contains('Academia - Academic Web Services'))
		
		except:
			if(browser.title=='academia-academic-services Login' or browser.title=='Sign In'):
				browser.quit()
				return "invaldCredentials"
			else:
				browser.quit()
				return "timeout"

		print "Logged In"
	
		browser.get('https://academia.srmuniv.ac.in/#View:My_Attendance')
		print "Crunching data"

		time.sleep(2)
		soup = browser.page_source.encode('utf-8')
		browser.quit()
		return soup
	
	except:
		print "AW SNAP, SOME ERROR OCCURED, Please try again"
		browser.quit

#<-------------------Functions end here------------------>


#<-------------------Main Program------------------>

credentials = getInfo()
#setProxy(myproxy)

page = getData(credentials)

if(page=='invaldCredentials'):
	print "Invalid Credentials"
	sys.exit(0)
elif(page=='timeout'):
	print "Timeout :-(, (running hostel wifi? i feel for u man/woman) \n Please try increasing the timeout time set in the code"
	sys.exit(0)

printStudentInfo(getStudentInfo(page))
printAtt(getAttendance(page))




#<-------------------Main Program Ends here------------------>
