import obliczenia.*;
import struktury.Para;
import struktury.Zbior;
import struktury.ZbiorTablicowy;

public class Main {
    public static void main(String[] args){
        /*ZbiorTablicowy z1 = new ZbiorTablicowy(5);
        z1.wstaw(new Para("Test", 1.0));
        z1.wstaw(new Para("Test 2", 2.0));
        z1.wstaw(new Para("Test 3", 3.0));
        z1.wstaw(new Para("Test 4", 4.0));
        z1.wstaw(new Para("Test 5", 5.0));
        //z1.wstaw(new Para("Test 6", 6));
        System.out.println(z1);
        z1.usuń("Test 2");
        System.out.println(z1);
        Wyrazenie w = new Dodawanie(
                new Liczba(7.2),
                new Mnozenie(
                        new Zmienna(z1, "Test 4"),
                        new Liczba(2.4)
                ));
        Wyrazenie z = new Mnozenie(
                new Zmienna(z1, "Test 4"),
                new Liczba(2.4)
        );
        Wyrazenie c = new Dodawanie(z, new Liczba(7.2));
        System.out.println(c.licz());
        System.out.println(w.licz());
        System.out.println(c.equals(w));*/

        ZbiorTablicowy z = new ZbiorTablicowy(1);
        z.wstaw(new Para("x", 1.618));
        Wyrazenie jeden = new Odejmowanie(
                new Dodawanie(
                        new Liczba(7),
                        new Mnozenie(
                                new Liczba(5),
                                new Liczba(3))),
                new Liczba(1));
        System.out.println(jeden.licz());
        Wyrazenie dwa = new Mnozenie(
                new ZmianaZnaku(
                        new Odejmowanie(
                                new Liczba(2),
                                new Zmienna(z, "x"))),
                new Stala("e"));
        System.out.println(dwa.licz());
        Wyrazenie trzy = new Dzielenie(
                new Odejmowanie(
                        new Mnozenie(
                                new Liczba(3),
                                new Stala("π")),
                        new Liczba(1)
                ),
                new Dodawanie(
                        new Zmienna(z, "x"),
                        new Liczba(5)
                ));
        System.out.println(trzy.licz());
        Wyrazenie cztery = new Sinus(
                new Dzielenie(
                        new Mnozenie(
                                new Dodawanie(
                                        new Zmienna(z, "x"),
                                        new Liczba(13)
                                ),
                                new Stala("π")
                        ),
                        new Odejmowanie(
                                new Liczba(1),
                                new Zmienna(z, "x")
                        )
                )
        );
        System.out.println(cztery.licz());
        Wyrazenie piec = new Dodawanie(
                new Silnia(new Liczba(5)),
                new Mnozenie(
                        new Zmienna(z, "x"),
                        new Logarytm(
                                new Stala("e"),
                                new Zmienna(z, "x"))
        ));
        System.out.println(piec.licz());
        Wyrazenie dwa_test = new Dzielenie(
                new Liczba(3),
                new Liczba(0)
        );
        System.out.println(dwa_test.licz());
        Wyrazenie jeden_test = new Dodawanie(
                new Stala("c"),
                new Liczba(1)
        );
        System.out.println(jeden_test.licz());

    }
}