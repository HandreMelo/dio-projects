# Projeto - criar um port scanner em python
Através da plataforma Digital Innovation One, foi proposto pelo Bruno Dias, dois scripts em Python que escaneassem as portas em um determinado IP / Host.

## Tecnologia e Bibliotecas utilizadas
Linguagem: Python 3.7.4 <br>
Softwares: Nmap

Bibliotecas built-in: tkinter e socket <br>
Bibliotecas adicionais: ipaddress e python-nmap

## Uma prévia...
### pscan.py
É um escaner simples de portas, basta abrir o terminal e rodar, python pscan.py ou python3 pscan.py <br>
Ao iniciar vai ser pedido que entre com os as portas desejadas a serem varridas, quantas forem preciso, e
em seguida o host/ip do destino.
O resultado será porta Aberta ou Fechada para cada uma.

### app.py
A implementação inicial proposta também foi de criar um escaner, mas desta vez utilizando o nmap, que é uma ferramenta poderosa e n-opções para todo tipo de trabalho de descoberta de rede. <br>
A modificação maior que fiz foi implementar uma GUI, estilo apps de desktop, com a biblioteca tkinter para ficar visualmente mais amigável.
Para iniciar, basta ir ao terminal e rodar, também. Então essa GUI irá abrir e poderão ser digitados Ip/Hostname e o range de portas, ex. 1-1024.
Em seguida basta clicar no botão "Scan" que ele fará uma chamada ao script pscan_nmap_v2.py, por isso é importante tê-lo na mesma pasta.
O resultado será mostrado na GUI.

<img src="https://i.imgur.com/J4n1wFB.png" title="source: imgur.com" /></a>


  
