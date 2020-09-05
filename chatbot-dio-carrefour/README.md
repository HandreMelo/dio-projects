# Projeto Lab - Construindo um ChatbotFit no Telegram com JavaScript e NodeJS

## Projeto proposto na Lab da Digital Innovation One.

### Montei um passo-a-passo simplificado com o que fiz para poder construir o projeto proposto:

1. instalar node
2. instalar npm
3. iniciar o projeto npm init
3. instalar chatbot no node via: https://www.npmjs.com/package/node-telegram-bot-api npm i node-telegram-bot-api --save "<---pra poder salvar no package-json"
5. Criar um arquivo chamado index.js onde vão os códigos iniciais daqui: https://www.npmjs.com/package/node-telegram-bot-api
6. (VER COMO FAZ) No telegram (no Botfather), criar um novo bot com /newbot
7. Pegar o token e inserir no arquivo index.js
8. Na pasta do projeto, npm start nome-projeto
9. Ir na aba do telegram, web mesmo e testar, clicar em COMEÇAR e BOOM!
10. Criar agente novo, criar projeto novo
11. Criar um service-account
12. Clicar em uma chave no local, Contas de serviço
13. Adicionar uma nova chave, salvar esta chave json na pasta do projeto
14. Ir em npm e procurar dialogflow (npm install dialogflow --save)
15. Intents no Dialogflow são intenções. Frases default de saudação por exemplo.
16. depois de preencher o dialogflow.js, rodar com node dialogflow.js
17. Baixar youtube node https://www.npmjs.com/package/youtube-node
18. Precisa da key específica que está no site (no youtube, google cloud para ativar a key)
19. Vai no site https://console.developers.google.com/apis/dashboard?project=diochatbot-xahc
ou aqui
https://developers.google.com/youtube/v3/quickstart/nodejs
20. Escolhe um projeto
21. Cria chave api com opção webservidor node e público
22. depois cria um arquivo com o nome yt-config.json (nome opcional) e cria
um parâmetro { "key": "CHVE OAISJdoijas"}
23. Criar um arquivo youtube.js com o código que precisar dentro
24. depois de rodar o projeto, node youtube.js, pegar o ID do vídeo,
ir na barra do youtube.com e adicionar, /watch?v=ID (via código ou manualmente)

Se o úsuário pedir vídeos...
Criar uma intenção do usuário em pedir vídeos
Então, ir no https://dialogflow.cloud.google.com/#/agent/diochatbot-xahc/intents
Dialogflow, criar intenções com as frases, do tipo, "quero vídeo de karaoke" etc,
depois usar palavras como entidades, então criar um grupo de entidade, que vai conter as palavras daquela categoria e por sinônimos,
depois no texto de resposta, por $nomeEntidade, ex. "Legal, vou te mandar um vídeo $nomeEntidade!"
por último é pegar essa resposta e fazer a requisição no youtube e mostrar o response


Aqui está um print do projeto em funcionamento no Instagram, onde o usuário pede por um vídeo de karaoke.
<img src="https://imgur.com/yhLbbAj.jpg"></img>

Aqui um print do DialogFlow onde mostra a diversidade de opções e combinações de respostas que podem ser feitas.

<img src="https://imgur.com/qMFaaq3.jpg"></img>
