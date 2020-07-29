#Programa criado por Bruno Dias para aula de Python
#Licença para uso e edição desde que citado o autor
#brunocdias@live.com
#Programa editado por André F.C. Melo
#handremelo@gmail.com


import socket


ip = input("Digite o host ou ip a ser verificado : ")
ports = []
while True:
    
    try:
        port = int(input("Digite as portas a serem verificadas, uma por vez (digite 0 para finalizar)"))
    except ValueError:
        print("\nValor incorreto, favor digitar portas em válidas. Ex. 80\n")
        continue
        
    if port == 0:
        break
    ports.append(port)

for port in ports:

    #AF_INET, conexao tipo IPV4, SOCK_STREAM, tipo TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    #vai receber um codigo da requisicao TCP
    code = client.connect_ex((ip, port))
    
    if code == 0:
        print("Porta {} Aberta".format(port))
        continue
    print("Porta {} fechada".format(port))
    print("Com o código {} retornado".format(code))
