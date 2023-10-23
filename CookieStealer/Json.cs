using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CookieStealer
{
    public static class Json
    {
        public static Dictionary<string, object> DeserializeJson(string json)
        {
            var result = new Dictionary<string, object>();
            string[] tokens = json.Split(new char[] { '{', '}', '%', ',' }, StringSplitOptions.RemoveEmptyEntries);

            for (int i = 0; i < tokens.Length; i += 2)
            {
                string key = tokens[i].Trim().Trim('"');
                string value = tokens[i + 1].Trim().Trim('"');

                if (!result.ContainsKey(key))
                {
                    if (long.TryParse(value, out long longValue))
                    {
                        result[key] = longValue;
                    }
                    else
                    {
                        result[key] = value;
                    }
                }
            }

            return result;
        }
    }
}
