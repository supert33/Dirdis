import sys
import time
from termcolor import colored
import requests
import os
import threading

global the
the = 500
global te
global file
global direc
global o
o = 0
 
        
        
    

def banner():
        print(colored(" __   ____ ____    __    ____    _s_s_s   ", 'red'))
        print(colored(" | \\    |  |   \  |  \     |  ss/      ", 'red'))
        print(colored(" |   \\  |  | _/   |   \\   |     \ss    ", 'green'))
        print(colored(" |   /   |  | \    |   /    |   ss/   ", 'green'))
        print(colored(" |__/   _|_ |  |   |__/    _|  s_s_s/  ", 'yellow'))
        print(colored("-------------------------------------------------", 'red'))
        print(colored("BY SUPER DUPE", 'red'))

banner()



giga = False
yay = False
te = 0
want_txt = input(colored("[!]Enter do you want to save results in txt Y or y:", 'yellow'))

if want_txt == "Y" or want_txt == "y":
    f_name = input(colored("[]Enter the name of the file:", 'yellow'))
    export = open(f_name, 'x')
    export.close()
    yay = True
    print(colored("[-] Storing in current dir: " + os.getcwd(), 'cyan'))

UrL = input(colored("[+] Enter URL: ", 'yellow'))
want_giga = input(colored("[*]Do you want giga speed(Y or y)", 'yellow'))
custom = input(colored("[-]Do you want a custom list (Y for yes)", 'yellow'))

if custom == "Y" or custom == "y" :
    list = input(colored("[+] Enter List : ", 'yellow'))
        

else : 
    print("[/]Using Default List")
    list = "storage/common.txt"

if want_giga == 'Y' or want_giga =='y':
        giga = True
file = open(list, 'r')
def normal_execute(URL, offset):
    global te
        
    te = 0
    ha = False
    


    def request(link):
            
            global mes
            file = open(list, 'r')
            global fil
            fil = file.readlines()
            global success
            success = int()
            global fall
            fall = int()
            
            try:
                if URL[:5] == "http:":
                    if_http = link.replace("http://", "")
                    success+=1

                    return requests.get("http://" + if_http)
                elif URL[:5] == "https":
                    if_https = link.replace("https://", "")
                    success+=1
                    
                    return requests.get("https://" + if_https)
                else:
                    print(colored("[?]provide a proper url", 'red'))
                    exit(0)
            
            except requests.exceptions.ConnectionError:
                fall+=1
                print("test")
                pass
        
        
    once = False

    for dir in file:

        if once is False:
            for i in range(1, offset):
                dir = dir + '\n'
            
        
        direc = dir.strip()
            
        full_url = URL + '/' + direc 
        
        response = request(full_url)
          
        if response :
            te+=1
            if yay:
                export = open(f_name, 'a')
                export.write(full_url + '\n')
                export.close()
            print(colored("[**]Directry discoverd at :" + full_url, 'green'))
        if giga == True:
            h = len(fil)
            if len(dir) == h:
                return    



start_time = time.time()





                




if giga == False:
        normal_execute(UrL, 0)
        if te == 0:
            print(colored("[!!!!]NOT FOUND ANY", 'red'))
        

        file.close()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(colored("Execution time: " + str(elapsed_time), 'cyan'))
        exit(0)  

else:   

            def spawn_threads(of):
                t1 = threading.Thread(target=normal_execute, args=(UrL, of, ))
                t1.start()
                t1.join()
                t2 = threading.Thread(target=normal_execute, args=(UrL, of+1,))
                t2.start()
                t2.join()
                t3 = threading.Thread(target=normal_execute, args=(UrL, of+2,))
                t3.start()
                t3.join()
                t4 = threading.Thread(target=normal_execute, args=(UrL, of+3,))
                t4.start()
                t4.join()
                t5 = threading.Thread(target=normal_execute, args=(UrL, of+4 ,))
                t5.start()
                t5.join()
            def mega_thread():
                spawn_threads(0)
                spawn_threads(5)
                spawn_threads(9)
                spawn_threads(13)
            mega_thread()
            file.close()
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(colored("Execution time: " + str(elapsed_time), 'cyan'))
            exit(0)


