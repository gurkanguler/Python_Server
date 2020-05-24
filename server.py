import socket,os,platform,time
import subprocess
import pickle

def MY_OS_CHECK():
    os_inf = platform.system()
    if os_inf == "Linux":
        os.system("clear")
    elif os_inf == "Windows":
        os.system("cls")




def Server():
    HOST = "0.0.0.0"
    PORT = 42
    BUF = 1024
    ADDR = (HOST,PORT)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    result = sock.bind((HOST,PORT))
    if result == None:
        print("\n")
        print(" [*] Server Started...")
        user_command,address = sock.recvfrom(BUF)
        user_command = user_command.decode("utf-8").strip()
        if user_command == "PUT":
            file_name,address = sock.recvfrom(BUF)
            file_name = file_name.decode("utf-8").strip()
            print(" [*] File Name : ",file_name)
            file_create = open(file_name,"wb")
            file_txt, address = sock.recvfrom(BUF)
            file_txt_new = file_txt.decode("utf-8").strip()
            for file_write in file_txt_new:
                file_create.write(bytes(file_write,encoding="utf-8"))
        if user_command == "GET":
        	sock.close()
        	Reverse_Server(address)
        	



    else:
        print(" [*] Server Error...")

def Reverse_Server(host):
	HOST = host[0]
	PORT = 42
	ADDR = (HOST,PORT)
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.connect((HOST,PORT))
	data = subprocess.check_output(["ls"]).decode("utf-8").split("\n")
	print(len(data))
	for list_data in data:
		sock.sendto(bytes(list_data,encoding="utf-8"),ADDR)
	



if __name__ == "__main__":
    MY_OS_CHECK()
    print("Server".center(40,'-'))
    Server()
