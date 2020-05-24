import socket,time,os,platform


############# Istemci Fonk. #############
def Client(host):
    #################
    HOST = host     
    PORT = 42       
    BUFF = 1024
    ADDR = (HOST,PORT)     
    #################

    ######### Istemci Olustur ###############
    main_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    main_client.connect((HOST,PORT))
    ######### Veri Gonder ################
    send_data = str(input("[*] -> "))

    ######### Komutu Gonder ###############
    main_client.sendto(bytes(send_data,encoding="utf-8"),ADDR)

    ########## VERI KONTROL ##############
    if send_data == "PUT":
        ########### Dosya Ismi ###################
        file_name = str(input("[+] Dosya Ismi : ->"))
        ########## Ismi Gonder ##############
        main_client.sendto(bytes(file_name,encoding="utf-8"),ADDR)
        ####### PUT Fonk. Cagir ############
        PUT(main_client,file_name,HOST,PORT,ADDR)
    
    if send_data == "GET":
        ######### DOSYA ISMI AL ##########
        file_name = str(input("[*] Dosya Ismi -> "))
        ############ ISMI GONDER ################
        main_client.sendto(bytes(file_name,encoding="utf-8"),ADDR)
        ######### GET FONK. CAGIR #############
        GET(file_name)


############## PUT ################

def PUT(main_client,file_name,HOST,PORT,ADDR):

    ######### Dosyayi AC #################
    open_file = open(file_name,"rb")

    ######### Dosyayı Oku ##################
    for read_file in open_file:
        ########## Dosyayı GONDER ##############
        main_client.sendto(read_file,ADDR)

    print("[*] Dosya Gonderildi...\n")


################ GET ####################

def GET(open_file):
    HOST = "0.0.0.0"
    PORT = 42
    BUFF = 1024
    new_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    new_server.bind((HOST,PORT))
    txt,addr = new_server.recvfrom(BUFF)
    create_file = open(open_file,"wb")
    new_txt = txt.decode("utf-8").strip()
    for write_file in new_txt:
        create_file.write(bytes(str(write_file),encoding="utf-8"))


######## CALISTIR ###################
if __name__ == "__main__":
    ######## Isletim sistemi kontrolu ########
    os_inf = platform.system()
    if os_inf == "Linux":
        os.system("clear")
    elif os_inf == "Windows":
        os.system("cls")
    print("Istemci\n")
    host = str(input("[*] Ip Adresini Giriniz -> "))
    Client(host)