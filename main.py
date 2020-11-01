import mudel
from termcolor import colored
import os
import requests

if os.name == 'nt':
    os.system('cls')
else:
    os.system("clear")


print(colored("""
   _,    _   _    ,_
  .o888P     Y8o8Y     Y888o.
 d88888      88888      88888b
d888888b_  _d88888b_  _d888888b
8888888888888888888888888888888
8888888888888888888888888888888
YJGS8P"Y888P"Y888P"Y888P"Y8888P
 Y888   '8'   Y8P   '8'   888Y
  '8o          V          o8'
    `                     `

""" , 'red'))
print(colored("------batCMS coded by ECHZED------" , 'green'))
print(colored("\n\nfor example ----> https://target.com " , 'red'))
target = str(input(colored('\nenter your target ~> ' , 'cyan')))

try:
    print(colored("\n[!] checking internet and url !" , 'yellow'))
    test_connnection = requests.get(target)
except:
    print(colored("\n[-] check your internet or url !" , 'red'))
    exit

print(colored("[+] checked" , 'green'))
if mudel.wp_detect(url=target):

    print(colored('\n[+] wordpress detected !' , 'green'))
    print(colored(f"\n[+] wordpress version : " , 'green') , colored(mudel.wp_version(target) , 'yellow'))


    theme = mudel.wp_theme(target)

    if len(theme) > 0 :

        print(colored("\n[+] theme : " , 'green') , colored(theme[0] , 'yellow'))
    
    else:
        print(colored("\n[+] theme : " , 'green') , colored("Not Found" , 'red'))

    plugins = mudel.wp_plugin(target)

    print(colored("\n[+] plugins : \n" , 'green'))

    for i in plugins:
        print(colored(f'\t| {i}' , 'yellow'))

    theme_ex = mudel.ex_search(theme)


    print(colored(f'\n[+]theme exploits :' , 'green'))
    
    if theme_ex != None and len(theme) > 0:

        for i in theme_ex:

            print(colored(f"\t| {i}" , 'yellow'))


    else:
        print(colored("\tNot Found :(" , 'red'))

    for x in plugins :

        plugin_ex = mudel.ex_search(x)
        
        print(colored(f"\n[+] {x} exploits : " , 'green'))
        if plugin_ex == None:
            print(colored("\tNot Found :(" , 'red'))


        else:
                
            for i in plugin_ex:

                print(colored(f"\t| {i}" , 'yellow'))





elif mudel.joomla_detect(target):

    print(colored("\n[+] joomla detected !" , 'green'))
    
    version = mudel.joomla_version(target)[0]

    if version == None :
        print(colored("\n[+] joomla version : " , 'green') , colored("not found ! " , 'red'))

    else: 
        print(colored("\n[+] joomla version : " , 'green') , colored( version , 'yellow'))

    template = mudel.joomla_template(target)

    print(colored("\n[+] joomla template : " , 'green') , colored(template , 'yellow'))

    template_exploit = mudel.ex_search(template)

    print(colored(f"\n[+] {template} exploits : " , 'green'))

    if template_exploit != None :
        
        for i in template_exploit:
            print(colored(f"\t| {i}" , 'yellow'))
    
    else:
        print(colored("\tNot Found :(" , 'red'))

else:    
    print(colored(f'\n[-] {target} is not wordpress or joomla !' , 'red'))
    exit



