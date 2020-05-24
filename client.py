import socket,os,time,platform


def MY_OS_CHECK():
    os_inf = platform.system()
    if os_inf == "Linux":
        os.system("clear")
    elif os_inf == "Windows":
        os.system("cls")


PORT = 42

def Client(HOST):

    BUF = 1024

    ADDR = (HOST,PORT)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    sock.connect((HOST,PORT))

    User_Command(sock,HOST,ADDR,BUF)


def User_Command(sock,HOST,ADDR,BUF):
    user_command = str(input(" [+] -> "))
    sock.sendto(bytes(user_command,encoding="utf-8"),ADDR)
    if user_command == "PUT":
        PUT(sock,HOST,ADDR)
    elif user_command == "GET":
        GET(sock)
    elif user_command == "LIST":
        LIST(HOST,ADDR)


def PUT(sock,HOST,ADDR):
    file_name = str(input(" [+] Enter to file name -> "))
    print(" [*] File Name : ",file_name)
    sock.sendto(bytes(file_name,encoding="utf-8"),ADDR)
    read_file = open(file_name,"rb")
    for read_file_line in read_file:
        sock.sendto(read_file_line,ADDR)

def GET(sock):
	sock.close()
	Reverse_Client()

def Reverse_Client():
	HOST = "0.0.0.0"
	PORT = 42
	BUFF = 1024
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind((HOST,PORT))
	server_data, addr = sock.recvfrom(BUFF)
	new_data = server_data.decode("utf-8").strip()
	for print_data in new_data:
		print(print_data)


if __name__ == "__main__":
    MY_OS_CHECK()
    print("CLIENT".center(40,'-'))
    host = str(input(" [+] Ip Address : -> "))
    Client(host)

