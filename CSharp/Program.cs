using System;
using System.Text.RegularExpressions;
using System.Threading;

using Telegram.Bot;
using Telegram.Bot.Args;

namespace ModeroBot
{
    class Program
    {
        private static ITelegramBotClient _botClient;

        static void Main(string[] args)
        {
            _botClient = new TelegramBotClient("1016890779:AAGdcZTjL1158sv3L6g8kscSbWB7Km23j54");

            var me = _botClient.GetMeAsync().Result;
            Console.WriteLine(
                $"Hello, World! I am user {me.Id} and my name is {me.FirstName}."
            );

            _botClient.OnMessage += Bot_OnMessage;
            _botClient.StartReceiving();
            Thread.Sleep(int.MaxValue);
        }

        static async void Bot_OnMessage(object sender, MessageEventArgs e)
        {
            var messageText = e.Message.Text;
            if (messageText != null)
            {
                Console.WriteLine($"Received a text message in chat {e.Message.Chat.Id}: {messageText}");
                
                var originalMessage = messageText;
                
                var regexUrl = new Regex(@"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)");

                if (regexUrl.Match(originalMessage).Success)
                {
                    Console.WriteLine($"Url regex found. Deleting message in chat {e.Message.Chat.Id}: {messageText}");
                    
                    try
                    {
                        await _botClient.DeleteMessageAsync(
                            chatId: e.Message.Chat,
                            messageId: e.Message.MessageId
                        );

                        await _botClient.SendTextMessageAsync(
                            chatId: e.Message.Chat,
                            text: "Шилтеме өчүрүлдү"
                        );
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"{ex}");
                    }
                }
            }

            if (e.Message.NewChatMembers != null && e.Message.NewChatMembers.Length > 0)
            {
                foreach (var newChatMember in e.Message.NewChatMembers)
                {
                    var message = $"Салам Урматтуу '{newChatMember.Username}'. Кош келипсиз биздин груупага!";
                    Console.WriteLine(message);

                    await _botClient.SendTextMessageAsync(
                        chatId: e.Message.Chat,
                        text: message
                    );
                }
            }
        }
    }
}