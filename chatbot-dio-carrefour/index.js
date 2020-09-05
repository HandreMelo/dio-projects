const TelegramBot = require('node-telegram-bot-api');
const dialogflow = require('./dialogflow');
const youtube = require('./youtube');

const token = 'TOKEN_TELEGRAM';

const bot = new TelegramBot(token, {polling: true});//pode ser webhook

//Aqui dentro vai toda a lógica das respostas!!!
//usar o dialogFlow, processamento de linguagem natural
bot.on('message', async function (msg) {
  const chatId = msg.chat.id;
  console.log(msg.text);
  //como o request do dialogflow é assíncrono então a função também tem de ser assícrona
  const dfResponse = await dialogflow.sendMessage(chatId.toString(), msg.text)
  
  let responseText = dfResponse.text;
  console.log(responseText);
  if (dfResponse.intent === 'Pedidos de Vídeos'){
    let values = encodeURIComponent(dfResponse.fields.karaoke.stringValue + ' ' + dfResponse.fields.tipokaraoke.stringValue);

    console.log(values);
    responseText = await youtube.searchVideoURL(responseText, values);
  }
  
  // send a message to the chat acknowledging receipt of their message
  bot.sendMessage(chatId, responseText);
});