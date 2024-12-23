import os
import ctypes
import time

text = ' ██████╗████████╗ █████╗     ██╗   ██╗    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗\n██╔════╝╚══██╔══╝██╔══██╗    ██║   ██║    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝\n██║  ███╗  ██║   ███████║    ██║   ██║    ███████╗██║     ██████╔╝██║██████╔╝   ██║   \n██║   ██║  ██║   ██╔══██║    ╚██╗ ██╔╝    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   \n╚██████╔╝  ██║   ██║  ██║     ╚████╔╝     ███████║╚██████╗██║  ██║██║██║        ██║   \n ╚═════╝   ╚═╝   ╚═╝  ╚═╝      ╚═══╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   '

os.system("color 4")

def opt_menu():
	opt = input('chose your option => ')
	os.system('cls')

	if opt=='1':
		os.system('netsh advfirewall firewall add rule name="Block GTA" dir=out action=block remoteip="192.81.241.171"')
		print('CLOUD SAVING IS DISABLED!\n')
		input("Press Enter to continue...")
		os.system('cls')
		text_menu()
	elif opt=='2':
		os.system('netsh advfirewall firewall delete rule name="Block GTA"')
		print('CLOUD SAVING IS ENABLED!\n')
		input("Press Enter to continue...")
		os.system('cls')
		text_menu()
	elif opt=='7':
		os.system("taskkill /IM GTA5.exe /F")
		os.system("taskkill /IM Launcher.exe /F")
		print('GTA 5 IS CLOSED!\n')
		input("Press Enter to continue...")
		os.system('cls')
		text_menu()
	elif opt=='8':
		print('SHUTTING OFF...')
		time.sleep(1)
		os.system("color 7")
		os.system('cls')
		exit()
	elif opt=='9':
		os.system("start www.github.com/DrRedBear/GTAO-Py-Script/blob/main/FAQ.md")
		os.system("cls")
		text_menu()
	elif opt=='0':
		os.system("start www.github.com/DrRedBear/GTAO-Py-Script?tab=readme-ov-file")
		os.system("cls")
		text_menu()
	else:
		print('UNKNOWN OPTION, TRY AGAIN!')
		time.sleep(1)
		os.system('cls')
		text_menu()


def text_menu():
	print(text)
	print('\n!!!!! MENU UPTIONS !!!!!\n')
	print('\n(1) => block cloud saving \n(2) => unblock cloud saving \n(7) => kill gta 5 process \n\n(8) => exit \n\n(9) => help/FAQ \n(0) => open my github repository \n')
	opt_menu()


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def checkAdmin():
	if isAdmin():
		text_menu()
	else:
		print("You must run this app as administrator, otherwise it won't work!!")
		input("Press Enter to continue...")
		exit()


isAdmin()

checkAdmin()

text_menu()