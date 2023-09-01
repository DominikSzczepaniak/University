using System;
using System.IO;
using System.ServiceProcess;
using System.Timers;
using System.Diagnostics;

namespace MyApp
{
    public partial class MyService : ServiceBase
    {
        private Timer timer;

        public MyService()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            // Tworzenie i konfigurowanie timera
            timer = new Timer();
            timer.Interval = 60000; // 1 minuta
            timer.Elapsed += TimerElapsed;
            timer.Start();
        }

        protected override void OnStop()
        {
            // Zatrzymanie timera
            timer.Stop();
            timer.Dispose();
        }

        private void TimerElapsed(object sender, ElapsedEventArgs e)
        {
            // Zapisywanie listy uruchomionych aplikacji do pliku tekstowego
            string filePath = "C:\\Path\\To\\LogFile.txt";

            try
            {
                using (StreamWriter writer = new StreamWriter(filePath, true))
                {
                    writer.WriteLine("==========");
                    writer.WriteLine($"Timestamp: {DateTime.Now}");
                    writer.WriteLine("Running Applications:");

                    Process[] processes = Process.GetProcesses();
                    foreach (Process process in processes)
                    {
                        if (!string.IsNullOrEmpty(process.MainWindowTitle))
                        {
                            writer.WriteLine(process.MainWindowTitle);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                // Obsługa błędów zapisu do pliku
                EventLog.WriteEntry("MyService", $"An error occurred while writing to the log file: {ex.Message}", EventLogEntryType.Error);
            }
        }

        public static void Main()
        {
            ServiceBase.Run(new MyService());
        }
    }
}
