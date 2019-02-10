import time
import get_state as api

def main():
	while(1):
		cmd = str(input("1 - status\n2 - on\n3 - off\n4 - modules\n"))

		if(cmd == "1"):
			information = api.get_information()
			print(information)
		elif(cmd == "2"):
			api.power("ON")
		elif(cmd == "3"):
			api.power("OFF")
		elif(cmd == "4"):
			modules = api.get_active_modules()
			print(modules)
		else:
			print("Error")
		time.sleep(3)

if __name__ == "__main__":
	main()