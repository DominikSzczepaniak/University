using System;
public class zbiorN
{
    public static int sumaCyfr(int liczba, string liczba_jako_string, int dlugosc){
        int wynik = 0;
        for(int i = 0; i<dlugosc; i++)
        {
            wynik += liczba_jako_string[i] - '0';
        }
        return wynik;
    }

    public static bool podzielnosc(int liczba)
    {

        string liczba_jako_string = liczba.ToString();
        int dlugosc = liczba_jako_string.Length;
        int wynik = sumaCyfr(liczba, liczba_jako_string, dlugosc);
        if(liczba%wynik != 0)
        {
            return false;
        }
        for (int i = 0; i<dlugosc; i++)
        {
            if (liczba_jako_string[i] - '0' == 0)
            {
                return false;
            }
            if (liczba % (liczba_jako_string[i] - '0') != 0)
            {
                return false;
            }
        }
        return true;   
    }

    public static void Main(){

        List<int> liczby = new List<int>();
        for(int i = 1; i<=1e5; i++){
            if (podzielnosc((int)i))
            {
                liczby.Add(i);
            }
        }
        foreach(int i in liczby)
        {
            Console.Write(i);
            Console.Write(" ");
        }
    }
}

