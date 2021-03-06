# Code of Kibo [Virtual Assistant]
# Let's Begin

# Libraries required

import platform
import webbrowser
import random
import os

# rolldie() body
def rolldie():
    print(random.randint(1, 6))

# flipcoin() body
def flipcoin():
    val = (random.randint(0,1))
    if val == 1:
        print("Heads!")
    else:
        print("Tails!")

# openApp() body
def openApp():
    app = raw_input('Enter app name : ')
    os.system('open {}:').format(app)

# shutdown() body
def shutdown():
    ch = platform.system()
    if ch == 'Windows':
        os.system('shutdown /s /t 1')
    elif ch == 'Linux':
        os.system('sudo shutdown now')
    else:
        os.system('sudo shutdown -h now')

# sleep() body
def sleep():
    ch = platform.system()
    print ('Good Bye,'+name)
    if ch == 'Windows':
        os.system('Rundll32.exe powrprof.dll,SetSuspendState')
    elif ch =='Linux':
        os.system('systemctl suspend')
    else:
        os.system('pmset sleepnow')

# openURL() body
def openURL():
    URL = input('Enter URL : ')
    webbrowser.open(URL)

# sysinfo() body
def sysinfo():
    info = """
    Machine: {}\n
    Version: {}\n
    Platform: {}\n
    Name: {}\n
    Family: {}\n
    Processor: {}\n
""".format(
        platform.machine(),
        platform.version(),
        platform.platform(),
        platform.node(),
        platform.system(),
        platform.processor(),
    )
    print (info) 

# Initialize everything and load all the commands

def createDictionary():
    dict = {

        '#rolldie' : rolldie ,
        '#flipcoin' : flipcoin ,
        '#openApp' : openApp ,
        '#shutdown' : shutdown,
        '#sleep' : sleep,
        '#openURL' : openURL,
        '#sysinfo' : sysinfo,

        }    
    return dict  

cmds_list = createDictionary()

cmds_keys = ["#rolldie","#flipcoin","#openApp","#shutdown","#sleep","#openURL","#sysinfo"]

print ('''
             ############################
             #              Kibo v1.2                            #
             #         Developed by Kaname           #
             ############################
                                                        ''')

print ('Hey! This is Kibo (^_^)')
name = input('What\'s your name?\n->')
print ('\nHello '+name+', nice to meet you!'+',let\'s get started!')

# Main function

def main():
    while True:
        command = input('->')

        if command.isdigit():
            print ('Oops! I didn\'t got that try again')

        elif command.isalpha():
            print ('Did you added \'#\' at the beginning?')

        elif command == '#exit':
            quit()

        elif command == '#help':
            print ('\nFollowing are commands I support : ')
            for var in cmds_keys:
                print ("- "+var)
                                   
        else:
            try:
                if command in cmds_keys:
                    cmds_list[command]()
                    print('\n')
                    main()
                
                else:
                    raise IOError()

            except IOError:
                print ('Invalid command! Try again or enter \'#help\' for all commands list')
       
main()
