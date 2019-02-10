import time
import get_state as api

def main():
	while(1):
		cmd = str(input("1 - status\n2 - on\n3 - off\n"))

		if(cmd == "1"):
			api.get_information()
		elif(cmd == "2"):
			api.power("ON")
		elif(cmd == "3"):
			api.power("OFF")	
		else:
			print("Error")
		time.sleep(3)

if __name__ == "__main__":
	main()