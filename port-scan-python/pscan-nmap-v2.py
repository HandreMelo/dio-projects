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

menuOptions = ['1','2','3','4']

modos = {
        '1':['-v -sS','tcp'],
        '2':['-v -sU','udp'],
        '3':['-v -sC','tcp']
        }

resultado = {}
def testarIp(ip):
    err,warn = '',''
    try:
        ipaddress.ip_address(ip)
    except:
        try:
            ip = socket.gethostbyname(ip)
            print("Hostname precisou ser convertido para um endereço de IP: {ip} \n".format(ip=ip))
        except:
            print("IP inválido")
            return False
    return ip
    
def startScan(ip='google.com', portas='1-1024', menu='1'):

    ip = testarIp(ip)
    if ip:
        resultado['version'] = str(scanner.nmap_version())
        print("Versao do nmap :", resultado['version'])
        
        scanner.scan(ip, portas, modos[menu][0])
        resultado['scanInfo'] = str(scanner.scaninfo())
        print(resultado['scanInfo'])
        
        resultado['status'] = str(scanner[ip].state())
        print("Status do IP: ", resultado['status'])
        
        resultado['protocols'] = str(scanner[ip].all_protocols())
        print("Protocolos: ", resultado['protocols'])
        
        resultado['doors'] = str(list(scanner[ip][modos[menu][1]].keys()))
        print("\nPortas Abertas:", resultado['doors'])

    return resultado


if __name__ == '__main__':
    print("Seja bem vindo ao DIOScanner --modificado")
    print("<----------------------------------------------->")
    menu = ''
    while menu != '4':
        ip = input("Entre com o ip / hostname a ser varrido: ")
        print("O ip / hostname digitado foi: {ip}".format(ip=ip))

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
