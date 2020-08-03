using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Extensions.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.InlineQueryResults;
using Telegram.Bot.Types.ReplyMarkups;

namespace dio_chatbot_carrefour
{
    public static class Program
    {
        public static bool inicio = true;
        private static TelegramBotClient Bot;
        
        public static async Task Main()
        {
#if USE_PROXY
            var Proxy = new WebProxy(Configuration.Proxy.Host, Configuration.Proxy.Port) { UseDefaultCredentials = true };
            Bot = new TelegramBotClient(Configuration.BotToken, webProxy: Proxy);
#else
            Bot = new TelegramBotClient(Configuration.BotToken);
#endif

            var me = await Bot.GetMeAsync();
            Console.Title = me.Username;

            var cts = new CancellationTokenSource();

            // StartReceiving does not block the caller thread. Receiving is done on the ThreadPool.
            Bot.StartReceiving(
                new DefaultUpdateHandler(HandleUpdateAsync, HandleErrorAsync),
                cts.Token
            );

            Console.WriteLine($"Ouvindo o chatbot @{me.Username}");
            Console.ReadLine();

            // Send cancellation request to stop bot
            cts.Cancel();
        }

        public static async Task HandleUpdateAsync(Update update, CancellationToken cancellationToken)
        {
            var handler = update.Type switch
            {
                UpdateType.Message => BotOnMessageReceived(update.Message),
                UpdateType.EditedMessage => BotOnMessageReceived(update.Message),
                UpdateType.CallbackQuery => BotOnCallbackQueryReceived(update.CallbackQuery),
                UpdateType.InlineQuery => BotOnInlineQueryReceived(update.InlineQuery),
                _ => UnknownUpdateHandlerAsync(update)
            };

            try
            {
                await handler;
            }
            catch (Exception exception)
            {
                await HandleErrorAsync(exception, cancellationToken);
            }
        }

        private static async Task BotOnMessageReceived(Message message)
        {

            if (message.Type != MessageType.Text)
                return;
            var action = (message.Text.Split(' ').First()) switch
            {
                "/menu" => Inicio(message),
                _ => Inicio(message)

            };
            await action;

            static async Task Inicio(Message message)
            {
                if (Program.inicio)
                {
                    inicio = false;
                    await Bot.SendPhotoAsync(
                      chatId: message.Chat,
                      photo: "https://www.carrefoursolucoes.com.br/image/layout_set_logo?img_id=7846530&t=1596225774678",
                      parseMode: ParseMode.Html
                    );
                    const string usage = "Olá! Seja bem vindo ao assistente virtual\n" +
                                         "do Carrefour Soluções Financeiras.\n" +
                                         "Abaixo estão algumas das opções disponíveis para iniciarmos seu atendimento.\n" +
                                         "Ao selecionar um link será apresentado e você poderá acessar a area desejada.";

                    await Bot.SendChatActionAsync(message.Chat.Id, ChatAction.Typing);
                    await Task.Delay(500);

                    Bot.SendTextMessageAsync(chatId: message.Chat.Id, text: usage);

                    await Bot.SendChatActionAsync(message.Chat.Id, ChatAction.Typing);
                    await Task.Delay(200);

                    Bot.SendTextMessageAsync(chatId: message.Chat.Id, text: "Para mostrar o menu novamente basta digitar /menu a qualquer momento");
                }

                var inlineKeyboard = new InlineKeyboardMarkup(new[]
                {
                    // first row
                    new []
                    {
                        //("Texto Apresentado", "Texto enviado")
                        InlineKeyboardButton.WithCallbackData("Acessar / Cadastrar", "https://www.carrefoursolucoes.com.br/primeiro-acesso"),
                        InlineKeyboardButton.WithCallbackData("Cartão Carrefour", "https://www.carrefoursolucoes.com.br/cartao/beneficios"),
                        InlineKeyboardButton.WithCallbackData("Seguros", "https://www.carrefoursolucoes.com.br/seguros1")
                    },
                    // second row
                    new []
                    {
                        InlineKeyboardButton.WithCallbackData("Serviços", "https://www.carrefoursolucoes.com.br/servicos"),
                        InlineKeyboardButton.WithCallbackData("Promoção", "https://www.carrefoursolucoes.com.br/promocao"),
                        InlineKeyboardButton.WithCallbackData("Blog", "https://www.carrefoursolucoes.com.br/blog")
                    }
                }); ;
                await Bot.SendTextMessageAsync(
                    chatId: message.Chat.Id,
                    text: "Opções",
                    replyMarkup: inlineKeyboard
                );

            }
        }
        private static async Task BotOnCallbackQueryReceived(CallbackQuery callbackQuery)
        {
            await Bot.AnswerCallbackQueryAsync(
                callbackQuery.Id,
                $"Recebido {callbackQuery.Data}"
            );

            await Bot.SendTextMessageAsync(
                callbackQuery.Message.Chat.Id,
                $"Link para acesso : {callbackQuery.Data}"
            );
        }

        private static async Task BotOnInlineQueryReceived(InlineQuery inlineQuery)
        {
            Console.WriteLine($"Received inline query from: {inlineQuery.From.Id}");

            InlineQueryResultBase[] results = {
                // displayed result
                new InlineQueryResultArticle(
                    id: "3",
                    title: "TgBots",
                    inputMessageContent: new InputTextMessageContent(
                        "hello"
                    )
                )
            };

            await Bot.AnswerInlineQueryAsync(
                inlineQuery.Id,
                results,
                isPersonal: true,
                cacheTime: 0
            );
        }
        private static async Task UnknownUpdateHandlerAsync(Update update)
        {
            Console.WriteLine($"Unknown update type: {update.Type}");
        }

        public static async Task HandleErrorAsync(Exception exception, CancellationToken cancellationToken)
        {
            var ErrorMessage = exception switch
            {
                ApiRequestException apiRequestException => $"Telegram API Error:\n[{apiRequestException.ErrorCode}]\n{apiRequestException.Message}",
                _ => exception.ToString()
            };

            Console.WriteLine(ErrorMessage);
        }

    }
}
