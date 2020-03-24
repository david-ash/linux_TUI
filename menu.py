import os
# Changing the color
os.system("tput setaf 1")
print("\t\tWelcome to TUI")
os.system("tput setaf 7")
print("\t\t---------------")


print("local/remote : ", end="")
location = input()
print(location)



print("""
	Press 1 to see date
	Press 2 to check cal
	Press 3 to conf web server
	Press 4 to create user
	Press 5 to create file
	Press 6 to setup n/w
	Press 7 to exit
	""")

print("Enter your choice : ", end="")
ch=input()

print(ch)

if location == 'local':
	if int(ch)==1:
		os.system("date")
	elif int(ch)==2:
		os.system("cal")
	elif int(ch)==3:
		os.system("date")
	elif int(ch)==4:
		print("Enter the username : ", end="")
		create_user = input();
		os.system("sudo useradd {}".format(create_user))
	elif int(ch)==5:
		os.system("date")
	elif int(ch)==6:
		os.system("date")
	elif int(ch)==7:
		os.system("date")
	else:
		print("Option not supported")
elif location == 'remote':
	remoteIP = input("Enter the IP of the remote server : ")
	# Check if the given ip is connected or not

	if int(ch)==1:
		os.system("ssh ashishsingh@{0} date".format(remoteIP))
	elif int(ch)==2:
		os.system("cal")
	elif int(ch)==3:
		os.system("date")
	elif int(ch)==4:
		print("Enter the username : ", end="")
		create_user = input();
		os.system("sudo useradd {0}".format(create_user))
	elif int(ch)==5:
		os.system("date")
	elif int(ch)==6:
		os.system("date")
	elif int(ch)==7:
		os.system("date")
	else:
		print("Option not supported")
else :
	print("Location does not support")