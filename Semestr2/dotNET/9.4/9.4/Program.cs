using System.Globalization;

namespace _9._4
{
    using System;
    using System.Globalization;
    using System.Windows.Forms;

    class Program
    {
        static void Main(string[] args)
        {
            CultureInfo[] cultures = {
            CultureInfo.GetCultureInfo("en-US"),   // angielski
            CultureInfo.GetCultureInfo("de-DE"),   // niemiecki
            CultureInfo.GetCultureInfo("fr-FR"),   // francuski
            CultureInfo.GetCultureInfo("ru-RU"),   // rosyjski
            CultureInfo.GetCultureInfo("ar-SA"),   // arabski
            CultureInfo.GetCultureInfo("cs-CZ"),   // czeski
            CultureInfo.GetCultureInfo("pl-PL")    // polski
        };

            DateTime currentDate = DateTime.Now;

            foreach (CultureInfo culture in cultures)
            {
                string monthNames = string.Join(", ", culture.DateTimeFormat.MonthNames);
                string abbreviatedMonthNames = string.Join(", ", culture.DateTimeFormat.AbbreviatedMonthNames);
                string dayNames = string.Join(", ", culture.DateTimeFormat.DayNames);
                string abbreviatedDayNames = string.Join(", ", culture.DateTimeFormat.AbbreviatedDayNames);

                string output = $"Language: {culture.DisplayName}\n" +
                                $"Full month names: {monthNames}\n" +
                                $"Abbreviated month names: {abbreviatedMonthNames}\n" +
                                $"Full day names: {dayNames}\n" +
                                $"Abbreviated day names: {abbreviatedDayNames}\n" +
                                $"Current date: {currentDate.ToString("D", culture)}\n";

                // Sprawdzenie, czy konsola tekstowa obs³uguje czcionki
                if (Console.OutputEncoding.CodePage == 65001)  // UTF-8
                {
                    Console.WriteLine(output);
                }
                else
                {
                    MessageBox.Show(output, "Language Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }

            Console.ReadLine();
        }
    }

}