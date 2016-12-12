#Cookie digging tool 
#Obedience (Hacking Ninja)
#Evil Python - Active State
#Anonymous Libraries

import mechanize 
import cookielib 
def printCookies(url):  
	browser = mechanize.Browser()  
	cookie_jar = cookielib.LWPCookieJar()  
	browser.set_cookiejar(cookie_jar)  
	page = browser.open(url)  
	for cookie in cookie_jar:   
		print cookie 
	#	url = 'target' 
		printCookies(url) 
