#Programa criado por Bruno Dias para aula de Python
#Licença para uso e edição desde que citado o autor
#brunocdias@live.com
#Programa editado por André F.C. Melo
#handremelo@gmail.com

import nmap
import ipaddress
import socket

#vai receber todos os atributos da biblioteca nmap
scanner = nmap.PortScanner()

modos = {
        '1':['-v -sS','tcp'],
        '2':['-v -sU','udp'],
        '3':['-v -sC','tcp']
        }

def startScan(ip='google.com', portas='1-1024', menu='1'):

    print("Versao do nmap :", scanner.nmap_version())
    scanner.scan(ip, portas, modos[menu][0])
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print("Protocolos: ", scanner[ip].all_protocols())
    portasAbertas = scanner[ip][modos[menu][1]].keys()
    print("\nPortas Abertas:", list(portasAbertas))
    
print("Seja bem vindo ao DIOScanner --modificado")
print("<----------------------------------------------->")

menuOptions = ['1','2','3','4']
menu = ''

while menu != '4':
    ip = input("Entre com o ip / hostname a ser varrido: ")
    print("O ip / hostname digitado foi: {ip}".format(ip=ip))
    
    try:
        ipaddress.ip_address(ip)
    except:
        ip = socket.gethostbyname(ip)
        print("Hostname precisou ser convertido para um endereço de IP: {ip} \n".format(ip=ip))
    
    portas = input("Entre com o range de portas desejada. Ex. 1-1024: ")
    print("O range de portas digitado foi: {portas}".format(portas=portas))
    
    menu = input("""\n Escolha o tipo de varredura a ser realizada
    1 -> Varredura do tipo SYN
    2 -> Varredura do Tipo UDP
    3 -> Varredura do Tipo Instensa
    4 -> Sair
    Digite a opção desejada:  """)
    print("Voce escolheu o scan de numero: ", menu)

    if menu not in menuOptions:
        print("Escolha uma opção correta!")
        continue
    
    
    startScan(ip, portas, menu)    