#Tech Challenge do Banco Carrefour

## A proposta:
Criar uma solução técnica que otimize a comunicação entre clientes e o Banco Carrefour. <br>

Critérios:

-> Utilizar C# ou Python. <br>
-> Utilizar Angular, caso tenha front-end (Opcional).<br>
-> Ter integração com o Telegram (API).<br>
-> Vídeo de até 3 minutos explicando a solução.<br>
-> Código fonte disponível no seu Github .<br>

## Descrição do projeto:

### Objetivo:
 <br> Facilitar o acesso das principais funcionalidades do site através de um chatbot.
 
### O Projeto:

Foi desenvolvido um back-end em C# ao qual faz integração com o telegram através de uma API e que fornece as funcionalidades mencionadas em botões clicáveis.

<img src="https://imgur.com/Llolbrl.jpg"></img>

### Instalação:

A instalação dos pacotes necessários para funcionar o projeto é simples. <br>

#### Chatbot Telegram

Para poder utilizar a solução, é preciso também criar um novo Bot através do link -> https://t.me/botfather <br>
seguindo as instruções. <br>
Uma vez criado, é preciso copiar o token e substituir o que está no arquivo configuration.cs do projeto. <br>

<img src="https://imgur.com/Kcb0t3S.jpg"></img>

#### .NET CORE

É preciso ter instalado o .NET Core, e a versão utilizada foi a 3.3.

#### Compilador C#

Para compilar o projeto / solução, foi utilizado o Visual Studio 2019.

#### Biblioteca do Telegram para C# :

Disponível em: https://www.nuget.org/packages/Telegram.Bot/
Para instalar basta adicionar o seguinte comando no prompt de comando do Windows (CMD) <br>
dotnet add package Telegram.Bot --version 15.7.1

Deve ser adicionado essa referência de pacote no .csproj
<PackageReference Include="Telegram.Bot.Extensions.Polling" Version="0.1.3" />
<PackageReference Include="Microsoft.EntityFrameworkCore.Sqlite" Version="3.1.6" />
