import brutx4.hash


def menu():
    print("[*] Hash Cracking [*]")
    print("[Zip File Cracking [*]")
    print("[*] FTP Cracking [*]")
    
    menu_input = int(input("[!] Ya Options => [!] "))

    if menu_input==1:
        hash()
    elif menu_input==2:
        zip()
    elif menu_input==3:
        ftp()


def hash():
    ya_w_list = input("Your Wordlist Path => ")
    brutx4.hash.md5(hash,ya_w_list)


def zip():

    ya_w_list = input("Your Zip Path => ")
    ya_w_list_p = input("Your Wordlist Path => ")
    brutx4.Zip.start(ya_w_list,ya_w_list_p)


def ftp():
    hst_n3m = input("Enter Your Hostname => ")
    usr_n3m = input("Enter Your Us3rn3me =>")
    w3rlis3t_p3swd = input("Enter Your W3rli3st Path => ")
    brutx4.FTP.start(hst_n3m,usr_n3m,w3rlis3t_p3swd)