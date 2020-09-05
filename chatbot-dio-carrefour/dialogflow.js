//básico do que precisa para enviar mensagem pro dialogflow
const dialogflow = require('dialogflow');
const configs = require('./diochatbot.json');

const sessionClient = new dialogflow.SessionsClient({
	projectId: configs.project_id,
	credentials: {
		private_key: configs.private_key,
		client_email: configs.client_email
	}
});

//importante criar sessão para o usuário
//tem exemplo no site
async function sendMessage(chatId, message){
	const sessionPath = sessionClient.sessionPath(configs.project_id, chatId);
	const request = {
		session: sessionPath,
		queryInput: {
			text: {
				text: message,
				languageCode: 'pt-BR'
			},
		},
	};
	//para trabalhar com as intenções
	//resposta do dialogflow, espera a resposta
	const responses = await sessionClient.detectIntent(request);
	//pegar a primeira resposta
	const result = responses[0].queryResult;
    console.log(JSON.stringify(result, null, 2));
	
	return {
        text: result.fulfillmentText,
        intent: result.intent.displayName,
        fields: result.parameters.fields
    };
    
};

module.exports.sendMessage = sendMessage;