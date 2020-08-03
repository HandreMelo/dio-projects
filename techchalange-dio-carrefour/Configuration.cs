using System;
using System.Collections.Generic;
using System.Text;

namespace dio_chatbot_carrefour
{
    public static class Configuration
    {
        public readonly static string BotToken = "1158503808:AAEq2-cfGLV7YKMig8oWr170bhMKaa9_n5k";

#if USE_PROXY
        public static class Proxy
        {
            public readonly static string Host = "localhost";
            public readonly static int Port = 8080;
        }
#endif
    }
}
