Zadanie 1:

Moc zużywana przez pracujący procesor:
$$P = CV^2*f$$
Algorytm wykonywany na dwóch rdzeniach wykona się dwa razy szybciej, niż gdyby wykonany został na jednym rdzeniu z taką samą częstotliwością. Chcemy aby czas wykonania algorytmu pozostał taki sam. Możemy to uzyskać zmniejszając dwukrotnie częstotliwość: $$t_2 = 2 * t_1 * \frac{1}{2} = t_1$$

Z liniowej zależności podanej w zadaniu: $$C = a * n \text{ gdzie } a \text{ to stała, a } n \text{ to liczba tranzystorów.}$$ $$V = b * f \text{ gdzie } b \text{ to stała, a } f \text{ to częstotliwość.}$$ 
Zatem:
$$P = CV^2*f = a * n * b^2 * f^3$$

Możemy teraz porównać moc obydwóch procesorów:
$$
P_2 = a * n_2 * b^2 * f_2^3 = a * 2 * n_1 * b^2*(\frac{1}{2}*f_1)^3=\\
a * 2 *n_1*b^2*\frac{1}{8}*f_1^3 = \frac{1}{4}*a*n_1*b^2*f_1^3 = \frac{1}{4}P_1
$$
Pokazaliśmy, że jest możliwość zaprojektowania procesora o takim samym czasie wykonania, ale zużywającego znacznie mniej mocy.


Zadanie 2:

**Problem sekcji krytycznej** - dwa wątki korzystają ze wspólnego zasobu, np. tak jak w tym przypadku - jeziora, podczas gdy w danym momencie tylko jeden proces może z niego korzystać.

Alicja:
1. Podnieś flagę
2. Dopóki flaga Boba jest w górze
    1. Jeśli napis wskazuje Bob:
        1. Obniż flagę
        2. Czekaj aż napis wskaże Alicja
        3. Podnieś flagę
3. Wypuść smoka
4. Poczekaj aż smok wróci
5. Ustaw napis na Bob
6. Obniż flagę

Bob:
1. Podnieś flagę
2. Dopóki flaga Alicji jest w górze:
    1. Jeśli napis wskazuje Alicja:
        1. Obniż flagę
        2. Poczekaj aż napis wskaże Bob
        3. Podnieś flagę
3. Wypuść smoka
4. Poczekaj aż smok wróci
5. Ustaw napis na Alicja
6. Opuść flagę

Zadanie 3:
Problem **producenta-konsumenta**, nazywany również problemem bufora, to klasyczny problem synchronizacji w systemach wieloprocesowych, gdzie dwie strony – producent i konsument – współdzielą ograniczone zasoby. Producent produkuje dane lub zasoby, które konsumowane są przez konsumenta, a celem jest zapewnienie, że nie wystąpią żadne błędy, takie jak nadpisywanie niewykorzystanych zasobów (gdy producent produkuje zbyt szybko) lub próba konsumpcji zasobów, gdy ich nie ma.

W historyjce o karmieniu smoków, przedstawionej na wykładzie, mamy następujący scenariusz:

	1.	Alicja to postać odpowiedzialna za wypuszczanie smoków do jedzenia.
	2.	Bob to postać odpowiedzialna za dostarczanie jedzenia.
	3.	Smoki są konsumentami jedzenia.

Pomiędzy Alicją i Bobem istnieje puszka na parapecie, która pełni rolę sygnalizatora stanu. Protokół działa w następujący sposób:

•	Alicja:
	1.	Czeka, aż puszka zniknie z parapetu, co oznacza, że Bob dostarczył jedzenie.
	2.	Wypuszcza smoki, aby mogły zjeść.
	3.	Po powrocie smoków sprawdza, czy jedzenie zostało w pełni zjedzone. Jeśli tak, odkłada puszkę z powrotem na parapet, sygnalizując, że Bob może dostarczyć nową porcję.
•	Bob:
	1.	Czeka, aż puszka pojawi się na parapecie, co oznacza, że jedzenie zostało zjedzone i można dostarczyć nową porcję.
	2.	Dostarcza jedzenie do jeziora.
	3.	Strąca puszkę z parapetu (ciągnąc za sznurek), co oznacza, że jedzenie jest gotowe do spożycia.

Ten protokół spełnia warunki klasycznego problemu producenta-konsumenta, w tym wzajemnego wykluczania (Bob i smoki nie są jednocześnie w jeziorze) oraz zapobiegania zagłodzeniu (smoki będą miały jedzenie, o ile Bob i Alicja będą działać sprawnie). Problemem jednak jest to, że Bob musi mieć widoczność na balkon Alicji, aby monitorować stan puszki, co jest wadą w sytuacji, gdy nie ma takiej widoczności (np. jezioro zasnute mgłą).

**Rozwiązanie problemu mgły**

Aby rozwiązać problem braku wzajemnej widoczności balkonów, możemy wykorzystać dwie puszki oraz mechanizm sznurków, co umożliwi komunikację bez potrzeby wizualnej kontroli. Protokół można zmodyfikować w następujący sposób:

1.	Alicja i Bob mają każdą swoją puszkę.
	•	Puszka u Alicji sygnalizuje Bobowi, że jedzenie zostało zjedzone i może dostarczyć nową porcję.
	•	Puszka u Boba sygnalizuje Alicji, że jedzenie zostało dostarczone i smoki mogą zostać wypuszczone.
2.	Alicja:
	1.	Czeka, aż puszka u niej zostanie przewrócona przez sznurek, co oznacza, że jedzenie zostało dostarczone przez Boba.
	2.	Wypuszcza smoki, aby mogły zjeść.
	3.	Gdy smoki wrócą i jedzenie zostanie zjedzone, Alicja odwraca swoją puszkę, co sygnalizuje Bobowi, że może dostarczyć nową porcję.
3.	Bob:
	1.	Czeka, aż puszka Alicji zostanie przewrócona, co oznacza, że smoki zjadły wszystko.
	2.	Dostarcza jedzenie do jeziora.
	3.	Strąca puszkę u siebie, aby poinformować Alicję, że jedzenie jest gotowe.

Dzięki temu rozwiązaniu, choć Alicja i Bob nie widzą nawzajem swoich balkonów, mogą efektywnie komunikować się za pomocą puszek i sznurków, zapewniając synchronizację między producentem (Bobem) a konsumentem (smokami).



Zadanie 4:
1. Własność bezpieczeństwa, ponieważ definiuje, że nigdy nie zdarzy się, aby klient został obsłużony niezgodnie z kolejnością.
2. Własność żywotności, ponieważ obiecuje, że w pewnym momencie, po wzroście, nastąpi pożądane zdarzenie (zejście na dół).
3. Własność żywotności, ponieważ opisuje, że prędzej czy później wątek wejdzie do sekcji krytycznej.
4. Własność żywotności, ponieważ gwarantuje, że w ciągu sekundy nastąpi pożądane zdarzenie (drukowanie komunikatu).
5. Własność żywotności, ponieważ obiecuje, że komunikat zostanie wydrukowany w odpowiedzi na przerwanie, chociaż nie określa, kiedy to nastąpi.
6. Własność bezpieczeństwa, ponieważ opisuje sytuację, w której coś złego (spadek kosztu życia) nigdy się nie wydarzy.
7. Własność żywotności:
To zdanie wyraża pewność, że pewne wydarzenia na pewno kiedyś się staną — czyli śmierć i podatki. W kontekście własności systemów:

Chociaż śmierć i podatki mogą być postrzegane jako niepożądane, w formalnej definicji własności żywotności chodzi o to, że pewne zdarzenie na pewno nastąpi w przyszłości, niezależnie od jego natury.


Zadanie 5:
Rozwiązanie tego problemu opiera się na odpowiedniej strategii, w której jeden z więźniów zostaje wyznaczony jako lider, a pozostali pełnią rolę liczników. Kluczowym elementem tej strategii jest kontrolowanie liczby zmian stanu przełącznika w taki sposób, aby lider mógł ostatecznie stwierdzić, że każdy więzień odwiedził przełączalnię przynajmniej raz.

Strategia krok po kroku:

1.	Ustalenie ról:
	•	Na spotkaniu przed rozpoczęciem odosobnienia grupa więźniów wybiera jedną osobę jako lidera. Lider ma specjalną rolę, która polega na liczeniu, ilu więźniów odwiedziło przełączalnię.
	•	Pozostali więźniowie pełnią rolę liczników i mają za zadanie sygnalizować liderowi, że odwiedzili przełączalnię, poprzez odpowiednie manipulowanie przełącznikiem.
2.	Zachowanie lidera:
	•	Lider nigdy nie włącza przełącznika. Jego jedynym zadaniem jest zliczanie, ile razy inni więźniowie włączyli przełącznik. Każde włączenie przełącznika będzie oznaczało, że kolejny więzień odwiedził przełączalnię po raz pierwszy.
	•	Za każdym razem, gdy lider wejdzie do przełączalni i zobaczy, że przełącznik jest włączony, wyłącza go i zwiększa licznik o 1. Kiedy licznik osiągnie liczbę równą liczbie więźniów minus jeden (ponieważ lider sam nie sygnalizuje swojego wejścia), lider ogłasza, że każdy więzień odwiedził przełączalnię przynajmniej raz.
3.	Zachowanie pozostałych więźniów (liczników):
	•	Każdy więzień, który nie jest liderem, jeśli wejdzie do przełączalni i zobaczy, że przełącznik jest wyłączony, włącza go, ale tylko jeden raz w trakcie całej gry.
	•	Jeśli dany więzień wszedł do przełączalni po raz kolejny i przełącznik jest włączony, nie zmienia jego stanu. Oznacza to, że tylko raz ma prawo zmienić stan z wyłączonego na włączony.

Dlaczego to działa?

	•	Lider ma pewność, że za każdym razem, gdy wchodzi do przełączalni i widzi włączony przełącznik, oznacza to, że jeden nowy więzień odwiedził przełączalnię po raz pierwszy i włączył przełącznik. Po wyłączeniu przełącznika przez lidera, lider zwiększa swój licznik.
	•	Każdy więzień inny niż lider włącza przełącznik tylko raz, a więc każde włączenie przełącznika daje liderowi sygnał, że nowy więzień odwiedził pokój.
	•	Gdy licznik lidera osiągnie liczbę równą liczbie więźniów minus jeden (ponieważ sam lider nigdy nie włącza przełącznika), lider wie, że wszyscy więźniowie (łącznie z nim samym) odwiedzili przełączalnię przynajmniej raz.

Dlaczego to jest efektywne?

	•	Każdy więzień odwiedzi przełączalnię przynajmniej 𝑁 razy, więc istnieje pewność, że wszyscy więźniowie w końcu odwiedzą przełączalnię przynajmniej raz. Liczba wejść jest nieograniczona, co pozwala strategii zakończyć się sukcesem.
	•	Dzięki temu, że tylko lider śledzi liczbę odwiedzin, a pozostali więźniowie manipulują przełącznikiem tylko raz, minimalizujemy ryzyko błędów i chaosu w zmianach stanu przełącznika.
	•	Po osiągnięciu przez lidera odpowiedniego licznika (liczba więźniów minus jeden), strategia kończy się, a więźniowie mogą ogłosić, że wszyscy byli w przełączalni, co prowadzi do ich uwolnienia.

Tym samym, nawet mając tylko jeden bit informacji (przełącznik włączony/wyłączony), więźniowie są w stanie skutecznie się uwolnić, stosując tę strategię.


Zadanie 6:
Podobnie jak wcześniej, potrzebujemy jednego lidera oraz pozostałych więźniów, którzy będą działać jako liczniki. Kluczowa różnica polega na tym, że musimy wziąć pod uwagę możliwość, że przełącznik może być początkowo zarówno włączony, jak i wyłączony, i odpowiednio dostosować strategię.

Krok po kroku:

1.	Ustalenie ról:
	•	Na spotkaniu przed izolacją, więźniowie wybierają lidera, który będzie zliczał, ilu więźniów odwiedziło przełączalnię.
	•	Pozostali więźniowie będą licznikami, których zadaniem jest sygnalizowanie liderowi, że odwiedzili przełączalnię po raz pierwszy.
2.	Zachowanie więźniów (liczników):
	•	Każdy więzień (oprócz lidera) ma za zadanie włączyć przełącznik, jeśli wejdzie do pokoju i zobaczy, że jest on wyłączony. Jest to sygnał dla lidera, że dany więzień był w pokoju po raz pierwszy.
	•	Ważne: więzień może włączyć przełącznik tylko raz. Jeśli wszedł do pokoju i przełącznik jest włączony, więzień nic nie zmienia.
3.	Zachowanie lidera:
	•	Lider, podobnie jak poprzednio, nie włącza przełącznika. Jego zadaniem jest zliczanie, ile razy inni więźniowie włączyli przełącznik.
	•	Jeśli lider wejdzie do pokoju i przełącznik jest włączony, wyłącza go i zwiększa swój licznik o 1.
	•	Jeśli lider wejdzie do pokoju i przełącznik jest wyłączony, nie robi nic, ponieważ oznacza to, że nikt nowy nie odwiedził przełączalni od czasu jego ostatniej wizyty.
	4.	Radzenie sobie z nieznanym początkowym stanem:
	•	Jeśli przełącznik jest początkowo wyłączony: W tym przypadku strategia działa tak, jak w poprzednim zadaniu. Pierwszy więzień, który wejdzie do pokoju, włączy przełącznik, a lider będzie zliczał te zmiany.
	•	Jeśli przełącznik jest początkowo włączony: Pierwszy więzień, który wejdzie do pokoju, nie włączy przełącznika, ponieważ już jest włączony. Dopiero lider, który wejdzie do pokoju, wyłączy przełącznik i od tego momentu strategia będzie działała normalnie — kolejni więźniowie będą włączać przełącznik po raz pierwszy, jeśli wejdą do pokoju i zobaczą go wyłączonym.
	5.	Warunek końcowy:
	•	Lider czeka, aż jego licznik osiągnie liczbę równą liczbie więźniów minus jeden (ponieważ sam lider nie sygnalizuje swojej obecności przez włączanie przełącznika). Gdy licznik osiągnie tę wartość, lider może ogłosić, że wszyscy więźniowie odwiedzili przełączalnię przynajmniej raz.

Dlaczego to działa?

	•	Dzięki temu, że każdy więzień (poza liderem) włącza przełącznik tylko raz, a lider zawsze wyłącza przełącznik, strategia skutecznie adaptuje się do początkowego stanu przełącznika.
	•	Jeśli przełącznik jest początkowo włączony, lider po prostu pierwszy raz wyłączy go i później będzie działać tak samo jak w scenariuszu z początkowo wyłączonym przełącznikiem.
	•	Niezależnie od początkowego stanu przełącznika, więźniowie będą włączać go tylko raz, co oznacza, że lider będzie mógł poprawnie zliczać liczbę odwiedzin.

Podsumowanie:

	•	Jeśli przełącznik był wyłączony od początku, strategia działa bez żadnych problemów.
	•	Jeśli przełącznik był włączony od początku, pierwszy raz lider go wyłączy, a potem wszystko przebiega zgodnie z planem.
	•	W każdym scenariuszu lider będzie w stanie poprawnie zliczyć wszystkie wizyty, a więźniowie będą mogli ogłosić, że każdy z nich odwiedził przełączalnię przynajmniej raz.

Zadanie 7:

**1. Wykazanie istnienia przebiegu prowadzącego do zakleszczenia**

Uruchamiając program mamy, że każdy filozof wykonuje w pętli następujące kroki:

1.	Myśli przez losowy czas.
2.	Staje się głodny i wypisuje komunikat.
3.	Podnosi lewą pałeczkę (left.get()).
4.	Podnosi prawą pałeczkę (right.get()).
5.	Je przez chwilę.
6.	Odkłada pałeczki (left.put() i right.put()).

Jeśli wszyscy filozofowie jednocześnie staną się głodni i podniosą swoją lewą pałeczkę, każda pałeczka będzie zajęta przez jednego filozofa. Następnie wszyscy będą próbowali podnieść prawą pałeczkę, która jest już trzymana przez sąsiada po prawej stronie. W efekcie żaden filozof nie będzie mógł kontynuować — nastąpi zakleszczenie.

Przykład przebiegu prowadzącego do zakleszczenia:

1.	Wszyscy filozofowie jednocześnie stają się głodni.
2.	Każdy filozof podnosi lewą pałeczkę.
3.	Każdy próbuje podnieść prawą pałeczkę, ale jest ona zajęta przez sąsiada.
4.	Filozofowie czekają w nieskończoność na zwolnienie prawej pałeczki.

**2. Modyfikacja pętli while w metodzie run() filozofa**

Aby zapobiec zakleszczeniu, możemy zmienić strategię podnoszenia pałeczek. Kluczowe jest przerwanie cyklu oczekiwania. Możemy to osiągnąć, zmieniając kolejność podnoszenia pałeczek dla części filozofów.

Modyfikacja:

Niech filozofowie o parzystych identyfikatorach podnoszą najpierw prawą, a potem lewą pałeczkę, a pozostali filozofowie — odwrotnie.

Zmodyfikowany kod metody run():

```
public void run() {
    Random random = new Random();
    while (true) {
        try {
            sleep(random.nextInt(1000));
            System.out.println("Philosopher " + id + " is hungry");

            if (id % 2 == 0) {
                right.get();
                left.get();
            } else {
                left.get();
                right.get();
            }

            System.out.println("Philosopher " + id + " is eating");
            sleep(random.nextInt(1000));

            left.put();
            right.put();

            System.out.println("Philosopher " + id + " is thinking");
        } catch (InterruptedException ex) {
            return;
        }
    }
}
```

Dzięki temu, jeśli wszyscy filozofowie staną się głodni jednocześnie:

	•	Filozofowie parzyści podniosą prawą pałeczkę, filozofowie nieparzyści lewą.
	•	Nie powstanie cykl oczekiwania, ponieważ przynajmniej jeden z sąsiadów każdego filozofa będzie mógł podnieść obie pałeczki i zjeść.
	•	Po zakończeniu jedzenia filozof odkłada pałeczki, umożliwiając sąsiadom podjęcie działania.

**3. Założenie o braku zagłodzenia**

Zgodnie z założeniem, wątki czekające na metodę get() nie zostaną zagłodzone. Oznacza to, że każdy filozof, który czeka na pałeczkę, w końcu ją otrzyma.