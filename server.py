import socket,time,os
import platform



def Main_Server():
    #################
    HOST = "0.0.0.0"#
    PORT = 42       #
    BUFF = 1024     #
    #################

    ######## SERVER OLUSTUR ############
    main_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    ######## SERVER DINLE ###############
    main_server.bind((HOST,PORT))

    ######## Istemci Komut Kontrol ################
    client_command,address = main_server.recvfrom(BUFF)
    
    client_command = client_command.decode("utf-8").strip()
    
    if client_command == "PUT":
        ############ PUT Fonk Cagir ############
        PUT(main_server,HOST,PORT,BUFF)
    if client_command == "GET":
        ############ DOSYA ISMINI AL #################
        file_name,address = main_server.recvfrom(BUFF)
        ############ GET FONK. CAGIR #################
        client_addr = address[0]

        GET(file_name,client_addr)



def GET(file_name,client_addr):
    file_open = open(file_name,"rb")
    for file_read in file_open:
        print(file_read)
    print(client_addr)
    New_Socket(client_addr,42,file_read)



def New_Socket(client_host,port,file_name):
    new_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    new_socket.connect((client_host,port))
    file_send = new_socket.sendto(file_name,(client_host,port))
       


def PUT(main_server,HOST,PORT,BUFF):
    ######### Dosya Adını Al ###############
    file_name,address = main_server.recvfrom(BUFF)
    ########### Dosyayı Olustur #############
    create_file = open(file_name,"wb")
    ############ Dosyayı Yaz ##############
    file_txt,address = main_server.recvfrom(BUFF)
    new_file_txt = file_txt.decode("utf-8").strip()
    for write_file in new_file_txt:
        create_file.write(bytes(str(write_file),encoding="utf-8"))




   




############# CALISTIR ################
if __name__ == "__main__":
    ########### Isletim Sistemi Kontrolu ###########
    os_inf = platform.system()
    if os_inf == "Linux":
        os.system("clear")
    elif os_inf == "Windows":
        os.system("cls")
    print('SERVER')
    Main_Server()
