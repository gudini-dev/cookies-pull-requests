import os
import re
import sys
import time
import threading
from os import path
from os import system
from colorama import Fore, Back, Style

class Design:
	@staticmethod
	def softName():
		return("COOKIES PULL REQUESTS")

	@staticmethod
	def softVersion():
		return(" (v0.2)")

	@staticmethod
	def printHeader():
		system("title " + Design.softName() + Design.softVersion())
		os.system("cls")
		print("\n " + Fore.GREEN + "█████████████████████████████████" + Style.RESET_ALL)
		print(" " + Fore.GREEN + "██" + Style.RESET_ALL + Fore.WHITE + "                             " + Style.RESET_ALL + Fore.GREEN + "██" + Style.RESET_ALL)
		print(" " + Fore.GREEN + "██" + Style.RESET_ALL + Fore.WHITE + "    " + Design.softName() + "    " + Style.RESET_ALL + Fore.GREEN + "██" + Style.RESET_ALL)
		print(" " + Fore.GREEN + "██" + Style.RESET_ALL + Fore.WHITE + "          by GUDINI          " + Style.RESET_ALL + Fore.GREEN + "██" + Style.RESET_ALL)
		print(" " + Fore.GREEN + "██" + Style.RESET_ALL + Fore.WHITE + "                             " + Style.RESET_ALL + Fore.GREEN + "██" + Style.RESET_ALL)
		print(" " + Fore.GREEN + "█████████" + Style.RESET_ALL + Back.GREEN + Fore.MAGENTA + "t.me/gudini_dev" + Style.RESET_ALL + Fore.GREEN + "█████████\n" + Style.RESET_ALL)
		
class CookiesPullRequests:
	def __init__(self):
		self.count = 0

	def WorkerStats(self):
		system("title " + Design.softName() + Design.softVersion() + "  \\  Statistics bar loading ...")
		while True:
			system("title " + Design.softName() + Design.softVersion() + "  \\  LEFT COUNT: [" + str(self.count_file) + "]")
			time.sleep(0.5)
			if self.count_file == 0:
				system("title " + Design.softName() + Design.softVersion() + "  \\  RESULT COUNT: [" + str(self.count) + "]")
				sys.exit()

	def print_error(self, text):
		print(Fore.RED + "\n [ERROR] " + text + Style.RESET_ALL)

	def parse(self, keys_list, folder_cookies, filenames_cookies, folder_new):
		for filename in filenames_cookies:
			with open(folder_cookies + "/" + filename, encoding = 'utf-8', errors = 'ignore') as file_in:
				result = []
				for line in file_in:
					line = line.strip()
					params = line.split("	")
					for key in keys_list:
						if key in params[0]:
							result.append(line)
			if len(result):
				self.count += 1
				with open(folder_new + "/" + filename, 'w', encoding = 'utf-8', errors = 'ignore') as f:
					for line in result:
						f.write(line + "\n")
			self.count_file -= 1

	def start(self):
		Design.printHeader()
		print(Fore.WHITE + "\n [INFO] Enter your keys separated by commas, (ex: .youtube.com, google.com, instagram)" + Style.RESET_ALL)
		keys_list = input(Fore.GREEN + "\n -> "  + Style.RESET_ALL)
		if keys_list == "":
			self.print_error("The line cannot be empty.")
			return
		keys_list = list(filter(None, {key.strip() for key in keys_list.split(",")}))
		if not len(keys_list):
			self.print_error("The line cannot be empty.")
			return
		print(Fore.BLUE + "\n You entered (" + str(len(keys_list)) +") keys:\n" + Style.RESET_ALL)
		c = 1
		for key in keys_list:
			print(Fore.BLUE + "  " + str(c) + ") " + key + Style.RESET_ALL)
			c += 1
		print(Fore.WHITE + "\n [INFO] Enter the path to the cookie folder, (ex: Desktop/cookies/*.txt)" + Style.RESET_ALL)
		folder_cookies = input(Fore.GREEN + "\n -> "  + Style.RESET_ALL)
		if not os.path.exists(folder_cookies):
			self.print_error("This folder does not exist.")
			return
		filenames_cookies = [file_name for file_name in os.listdir(folder_cookies) if os.path.isfile(folder_cookies + "/" + file_name)]
		if not len(filenames_cookies):
			self.print_error("Cookies folder is empty, no format " + folder_cookies + "/*.txt")
			return
		print(Fore.BLUE + "\n Found (" + str(len(filenames_cookies)) +") cookies file" + Style.RESET_ALL)
		print(Fore.WHITE + "\n [INFO] Enter the path where to save new cookies, (ex: Desktop/new_cookies)" + Style.RESET_ALL)
		folder_new = input(Fore.GREEN + "\n -> "  + Style.RESET_ALL)
		if folder_new == "":
			self.print_error("The line cannot be empty.")
			return
		if not os.path.exists(folder_new):
			os.mkdir(folder_new)
		print("\n " + Fore.BLUE + "███████████████████████" + Style.RESET_ALL)
		print(" " + Fore.BLUE + "██" + Style.RESET_ALL + Fore.WHITE + "     LOADING ...   " + Style.RESET_ALL + Fore.BLUE + "██" + Style.RESET_ALL)
		print(" " + Fore.BLUE + "███████████████████████" + Style.RESET_ALL)
		threading.Thread(target = self.WorkerStats).start()
		self.count_file = len(filenames_cookies)
		self.parse(keys_list, folder_cookies, filenames_cookies, folder_new)
		print(Fore.GREEN + "\n [FINISH] Result count cookies: " + str(self.count) + Style.RESET_ALL)

if __name__ == "__main__":
	soft = CookiesPullRequests()
	soft.start()

	input(Fore.WHITE + "\n ENTER TO EXIT" + Style.RESET_ALL)