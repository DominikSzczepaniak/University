import java.util.Scanner;
import java.lang.StringBuilder;
class Main{
private static String[] rzymskie = {"M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"};
private static int[] arabskie = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

public static String rzymska(int n){
    if(n <= 0 || n >= 4000){
        throw new IllegalArgumentException("liczba" + n + "spoza zakresu 1-3999");
    }
    StringBuilder wynik = new StringBuilder("");
    int licznik = 0;
    while(n > 0){
        if(arabskie[licznik] <= n){
            wynik.append(rzymskie[licznik]);
            n -= arabskie[licznik];
        }
        else{
            licznik++;
        }
    }
    return wynik.toString();
}

public static String zodiak(int n){
    n -= 1900;
    n %= 12;
    n = (n+12)%12;
    n++;
    String answer = "";
    switch(n){
        case 1 -> answer = "Szczur";
        case 2 -> answer = "Wół";
        case 3 -> answer = "Tygrys";
        case 4 -> answer = "Królik";
        case 5 -> answer = "Smok";
        case 6 -> answer = "Wąż";
        case 7 -> answer = "Koń";
        case 8 -> answer = "Koza";
        case 9 -> answer = "Małpa";
        case 10 -> answer = "Kogut";
        case 11 -> answer = "Pies";
        case 12 -> answer = "Świnia";
    }
    return answer;
}

public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    System.out.println("imie: ");
    String imie = in.nextLine();
    System.out.println("data urodzenia (format 10.10.2023): ");
    String data_urodzenia = in.nextLine();
    char przerywnik = '.';
    StringBuilder data_urodzenia_rzymskie = new StringBuilder("");
    StringBuilder liczba = new StringBuilder("");
    for(int i = 0; i<data_urodzenia.length(); i++){
        if(data_urodzenia.charAt(i) != przerywnik){
            liczba.append(data_urodzenia.charAt(i));
        }
        else{
            data_urodzenia_rzymskie.append(rzymska(Integer.parseInt(liczba.toString())));
            data_urodzenia_rzymskie.append(" ");
            liczba = new StringBuilder("");
        }
    }  
    data_urodzenia_rzymskie.append(rzymska(Integer.parseInt(liczba.toString())));
    int rok_urodzenia = Integer.parseInt(liczba.toString());
    System.out.println("Cześć " + imie);
    System.out.println("Twoja data urodzenia w systemie rzymskim to: " + data_urodzenia_rzymskie);
    System.out.println("Twoj znak zodiaku w kalendarzu chinskim to " + zodiak(rok_urodzenia));
}
}