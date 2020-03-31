import socket
import threading
from queue import Queue
import time

again = 'o'

while again == 'o':
    print_lock = threading.Lock()

    # Set a and b for the range
    a = 0
    b = 0

    print("<--------------------------------------->")
    print("|       Bienvenue sur ScanPort V1       |")
    print("<--------------------------------------->\n")

    host = input("\nVeuillez entrer le nom de domaine de la target : ")
    # Translate a host name to ipv4 address format
    ip = socket.gethostbyname(host)
    print("")
    print("-" * 90)
    a = input("     Veuillez entrer le numéro du port ou le programme attaquera a scanner : ")
    a = int(a)
    b = input("     Veuillez entrer le numéro du port ou le programme terminera de scanner : ")
    b = int(b)
    t = input('     Combien de threads souhaitez vous allouer : ')
    print("-" * 90)
    print("")
    print ("-" * 64)
    print (" Debut du scan sur l'IP ", ip, " du port ", a, "au port ", b," ")
    print ("-" * 64,"\n")

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((ip, port))
            with print_lock:
                print('Port', port, 'is Open')
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()

    for x in range(int(t)):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(a,b):
        q.put(worker)
    q.join()
    again = input('\nSouhaitez vous effectuer un autre scan ? (" <o> Oui / <n> Non) : ')
    if again =='o':
        continue
    else:
        print('FIN DU PROGRAMME dans : ')
        down = 10
        while down > -1:
            m, s = divmod(down, 60)
            time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end="")
            time.sleep(1)
            down -= 1
