//polymorphism
public class zad1b {
    public static void wypisz(String napis){ 
        System.out.println(napis);
    }

    public static void wypisz(int napis){
        System.out.println(Integer.toString(napis));
    }

    public static void main(String[] args) {
        wypisz("Hello World!");
        wypisz(123);
    }
}