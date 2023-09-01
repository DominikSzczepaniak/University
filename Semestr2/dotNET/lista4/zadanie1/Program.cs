//Zaimplementować metodę bool IsPalindrome() rozszerzającą klasę string.
//Implementacja powinna być niewrażliwa na białe znaki i znaki przestankowe występujące
//wewnątrz napisu ani na wielkość liter. Klient tej metody powinien wywołać ją tak:
//string s = "Kobyła ma mały bok.";
//bool ispalindrome = s.IsPalindrome();

namespace Extensions
{
    public static class StringExtensions
    {
        public static bool isPalindrome(this string s)
        {
            s = s.ToLower();
            string news = "";
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == ' ' || s[i] == '.' || s[i] == ',')
                {
                    continue;
                }
                news += s[i];
            }
            s = news;
            for (int i = 0; i < s.Length / 2; i++)
            {
                if (s[i] != s[s.Length - 1 - i])
                {
                    return false;
                }
                return true;
            }
            return true;
        }
    }

    class Program
    {
        public static void Main()
        {
            string s = "Kobyła ma mały bok.";
            Console.WriteLine(s.isPalindrome());
        }
    }
}