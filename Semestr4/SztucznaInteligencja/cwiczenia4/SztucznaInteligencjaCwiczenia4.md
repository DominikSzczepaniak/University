ZADANIE 1
Null move heuristic - technika która próbuje zgadnąć kiedy można odciąć drzewo poszukiwań z mniejszym wysiłkiem niż normalnie.
Ta heurystyka jest bazowana na tym, że jeżeli gracz który ma się ruszyć się nie ruszy (pominie ruch) i dalej będzie miał pozycje wystarczająco dobrą, żeby odciąć drzewo poszukiwań, to pozycja raczej na pewno spowoduje odcięcie drzewa przeszukiwania jeśli gracz zrobi jakikolwiek ruch.

Problemem jest to, że może być pozycja w której każdy ruch jest gorszy niż pozostanie w stanie obecnym. W tej pozycji null move heuristic mogłaby odciąć drzewo poszukiwania, gdzie pełny search by go nie odciął i założyć, że pozycja jest dobra, mimo iż jest zupełnie przeciwnie. 

ZADANIE 3
Rozważam lis i gęsi z takimi zasadami:
Lis ma jeden pionek, gęsi mają 13 pionków. Gęsi wygrywają gdy otoczą lisa, lis wygrywa gdy gęsi nie mogą go otoczyć. Lis nie musi bić gęsi, lis bije gęsi przeskakując je, może zbić wiele gęsi (jeśli zgadza się orientacja ruchu) oraz nie może wykonać przeskoku jeśli wyskoczy poze plansze.

Heurystyka:
Jeśli lis ma gorszą pozycję gdy jest wokół niego dużo gęsi to chcemy unikać takich pozycji, bo mogą one prowadzić do przegranej.
Chcemy też faworyzować pozycję gdy lis może zbić więcej niż jedną gęś i dalej być bezpieczny.

Heurystyka:
x - ilość pozostałych gęsi 
y - ilość gęsi w zasięgu 1 od lisa 
Heurystyka: x + 2y - lis stara się minimalizować, gęsi maksymalizować.

ZADANIE 4
PYTANIE:
Czy można prosić o jakiś przykład jak klasyfikować dane w której części wykresu będą? Wg mnie jak już umieścimy coś w jakiejś części wykresu to raczej wiemy już do jakiej kategorii coś należy?

Algorytm K najbliższych sąsiadów (KNN, od ang. K-Nearest Neighbors) to prosty, ale skuteczny algorytm używany w statystyce do klasyfikacji i regresji. W przypadku klasyfikacji, algorytm identyfikuje K najbliższych punktów danych w przestrzeni cech względem nowego punktu, którego klasę chcemy przewidzieć. Klasyfikacja nowego punktu dokonywana jest poprzez przypisanie mu klasy, która jest najczęściej reprezentowana przez K najbliższych sąsiadów.

Algorytm KNN opiera się na kilku kluczowych założeniach:
1. **Zbliżoność**: Zakłada, że podobne przypadki znajdują się blisko siebie w przestrzeni cech.
2. **Głosowanie większościowe**: W przypadku klasyfikacji, przewidziana klasa dla nowego punktu jest określana przez większość klas wśród jego najbliższych sąsiadów.
3. **Parametr K**: Użytkownik musi określić wartość K, czyli liczbę sąsiadów do rozważenia. Wybór K może wpłynąć na skuteczność algorytmu – mniejsze wartości K mogą prowadzić do nadmiernego dopasowania (overfitting), a większe do niedopasowania (underfitting).

W regresji KNN, wartość wyjściowa dla nowego punktu jest średnią (lub inną formą agregacji) wartości odpowiedzi sąsiadów. Algorytm ten jest bardzo intuicyjny i łatwy do zaimplementowania, ale może być nieefektywny przy bardzo dużych zbiorach danych lub gdy liczba wymiarów (cech) jest duża, co jest znane jako przekleństwo wymiarowości.
----------------------------------
Drzewo punktu widokowego (Vantage Point Tree, VP-Tree) jest strukturą danych, która może być używana do optymalizacji algorytmów wyszukiwania najbliższego sąsiada, takich jak KNN (K najbliższych sąsiadów). Związek między VP-Tree a KNN wynika głównie z potrzeby efektywnego wyszukiwania najbliższych punktów w przestrzeniach o dużych wymiarach, co jest typowym wyzwaniem dla algorytmów bazujących na sąsiedztwie.
Jak działa VP-Tree

VP-Tree organizuje dane w sposób, który pozwala na szybkie odrzucenie dużych części przestrzeni danych podczas wyszukiwania najbliższych sąsiadów. Drzewo jest budowane poprzez:

    Wybór punktu (zwany punktem widokowym) z zestawu danych.
    Obliczenie odległości między tym punktem widokowym a wszystkimi innymi punktami w zestawie danych.
    Podział zestawu danych na dwa podzbiory na podstawie mediany obliczonych odległości – jedna połowa zawiera punkty bliższe punktowi widokowemu niż mediana, druga połowa zawiera punkty dalsze.
    Rekurencyjne powtórzenie procesu dla każdego podzbioru, aż do osiągnięcia określonego kryterium zatrzymania (np. gdy liczba punktów w podzbiorze spadnie poniżej pewnego progu).

Zastosowanie VP-Tree w KNN

Podczas wyszukiwania K najbliższych sąsiadów przy użyciu VP-Tree, algorytm zaczyna od korzenia drzewa i na każdym poziomie decyduje, które gałęzie drzewa eksplorować, opierając się na odległości od punktu widokowego do szukanego punktu oraz na odległościach międzygałęziowych. To pozwala na efektywne zredukowanie liczby obliczeń odległości potrzebnych do identyfikacji najbliższych sąsiadów, szczególnie w przestrzeniach o wielu wymiarach.

Dzięki VP-Tree, proces wyszukiwania w KNN może być znacznie przyspieszony, ponieważ algorytm nie musi obliczać odległości od szukanego punktu do każdego punktu w zestawie danych, a zamiast tego skupia się tylko na najbardziej obiecujących kandydatach. To sprawia, że VP-Tree jest bardzo przydatnym narzędziem w przypadkach, gdzie klasyczne metody wyszukiwania najbliższych sąsiadów okazują się zbyt wolne lub niewydajne.

ZADANIE 5
Klasyfikacja na granicach decyzyjnych: Jeżeli próbka znajduje się dokładnie na granicy decyzyjnej między klasami i wybrane k sąsiadów nie daje jednoznacznego wyniku (np. każda klasa ma połowę głosów), to algorytm może popełnić błąd w jej klasyfikacji.

Szum i wartości odstające w danych: Jeżeli dane zawierają szum (nieprawidłowe etykiety) lub wartości odstające (outliery), to nawet przy odpowiednio dobranym k, k-NN może niepoprawnie klasyfikować niektóre próbki, nawet te z zbioru uczącego. Na przykład, jeżeli jedna z próbek ma błędnie przypisaną etykietę, a jest brana pod uwagę przy klasyfikacji swoich sąsiadów, może spowodować ich błędną klasyfikację.

Zbyt mała wartość k: Jeżeli wartość k jest zbyt mała (np. k=1), to klasyfikacja może być bardzo wrażliwa na pojedyncze próbki, co zwiększa wpływ szumu i wartości odstających na wynik klasyfikacji. W takim przypadku, nawet próbki z błędnymi etykietami mogą wpływać na klasyfikację swoich sąsiadów.

Zbyt duża wartość k: Przeciwnie, zbyt duża wartość k może prowadzić do sytuacji, gdzie wpływ na klasyfikację nowej próbki mają sąsiednie próbki, które są stosunkowo daleko i mogą należeć do innych wzorców rozkładu danych, co również może powodować błędy.

ZADANIE 6
a) losowanie ze zbioru możliwych kart - t.j. tych które nie zostały już pokazane, które mamy my oraz tych które nie może mieć żaden przeciwnik (bo np. skończyłby już grę)

b) Na podstawie licytacji możemy szacować, że niektóre rozdania sa bardziej prawdopodobne (lub mniej). Przykład: tysiąc. Grę gracze rozpoczynają liczytacją mówiąc ile punktów uda im się zdobyć. Jednak niektóre wartości nie są możliwe do uzyskania za pomocą samych kart, wymagają dodatkowo punktowanych meldunków (meldunek to król i dama jednego koloru). Jeżeli gracz wylicytuje na początku dużą wartość to możemy przewidywać, że ma jakiś meldunek. Dodatkowo zagrania gracza też mogą nam coś powiedzieć o jego kartach. Przykładowo Makao, jeżeli gracz dobiera zamiast wykładać kartę to możemy podejrzewać, ze nie ma tej figury/koloru. Pozwala nam to lepiej szacować prawdopodobieństwo rozdania, przez co podejmujemy lepsze, trafniejsze decyzje. Problemy : możemy źle zinterpretować co się dzieje w grze.

c) Jaki istotny aspekt gier karcianych jest pomijany w tym podejściu?
Pomijamy całkowicie oszukiwanie (i zachowanie graczy, które może wiele zdradzić), gracze w trakcie licytacji (czy dalej w trakcie gry) nie muszą mówić prawdy. Dodatkowo gracze nie muszą podejmować mądrych, optymalnych decyzji.

ZADANIE 7
Agenci do gry w oszukiwanie (lepsi niż losowi)

Agent 1
Pierwszą rzeczą, która przychodzi na myśl, jest po prostu gracz, który liczy karty, które na pewno są w grze. Gdy przeciwnik deklaruje niemożliwą ilość kart, możemy założyć, że oszukuje, i możemy go sprawdzić.

Agent 2
Kolejną prostą poprawą byłby nasz styl gry - sposób, w jaki kładziemy karty na stosie. Zawsze, gdy jest to możliwe, możemy kłaść bez oszustwa najniższe możliwe karty aż do pewnej ustalonej liczby (którą obliczyliśmy jako optymalną, powiedzmy, że jest to 8). Następnie oszczędzalibyśmy mocniejsze karty na później i w innym zakresie (przedobliczonym - od 9 do Damy) staralibyśmy się wkomponować najniższe karty, które mamy. Dla kart powyżej tego zakresu gramy normalnie, jeśli to możliwe.

Wyjaśnienie
Agent 1 koncentruje się na liczeniu kart, aby identyfikować oszustwa, na podstawie deklaracji przeciwnika, które są niemożliwe przy znanej liczbie kart. Dzięki temu można podejmować decyzję o sprawdzeniu przeciwnika w odpowiednim momencie.

Agent 2 koncentruje się na strategicznym zarządzaniu kartami w swojej ręce. Przez umiejętne rozplanowanie, kiedy i jakie karty kłaść na stos, agent stara się zoptymalizować wykorzystanie swojego zestawu kart, zachowując silniejsze karty na kluczowe momenty gry i stosując słabsze karty tam, gdzie jest to możliwe, by unikać ryzyka i oszustwa.

ZADANIE 8
sigma to jakaś funkcja (na wykładzie nie było sprecyzowane więc ja też nie precyzuję)

x v y 
sigma(x + y)

---
x ^ y 
sigma(x + y - 1)

---
x xor y = (x v y) ^ not (x ^ y) 
lewa częśc - sigma(x + y)
prawa część - (1 - sigma(x + y - 1)) 

to są nasze neurony pomocnicze, oznaczmy je:
a = sigma(x + y)
b = 1- sigma(x + y - 1)

Wtedy nasza sięc neuronowa to:
sigma(a + b - 1)


xor nie mozna bo nie jest funkcja liniowo separowalną - nie istnieje taka prosta która oddziela punkty należące do jednej klasy punktów od drugiej klasy punktów. 

ZADANIE 9
Wiemy z logiki, że or and oraz not są zbiorem zupełnym, więc odpowiedzą na wszystkie zapytania logiczne, a te umiemy wyrazić w sieciach neuronowych, więc tak możemy odpowiedzieć na wszystkie możliwe funkcje boolowskie.
Ponieważ niektóre zapytania logiczne są bardziej złożone bedziemy potrzebować dwie lub jedną warstwę (zależnie od zapytania)




ZADANIE 10
Superrationality, czyli nadracjonalność, to koncepcja w teorii gier, która została wprowadzona przez Douglasa Hofstadtera. Jest to rozszerzenie tradycyjnego pojęcia racjonalności używanego w ekonomii i teorii gier. Superrationality opisuje podejście do gier o sumie stałej, w których uczestnicy, przyjmując założenie o identycznych procesach decyzyjnych innych graczy, wybierają strategię, która jest najlepsza dla każdego, gdy wszyscy myślą w ten sam sposób.

### Główne założenia superrationality:

1. **Podobieństwo uczestników**: Superrationality zakłada, że wszyscy uczestnicy gry są podobni do siebie i korzystają z tego samego procesu decyzyjnego. W efekcie, jeśli gracz dochodzi do wniosku, że pewne rozwiązanie jest najlepsze, może oczekiwać, że inni gracze również dojdą do tego samego wniosku.

2. **Optymalizacja zbiorowa**: W przeciwieństwie do tradycyjnej racjonalności, gdzie każdy gracz stara się maksymalizować własny zysk, superrationality skupia się na znalezieniu rozwiązania, które jest optymalne dla wszystkich graczy jako grupy.

3. **Długoterminowa współpraca**: Superrationality często wskazuje na wartość długoterminowej współpracy nad krótkoterminowym zyskiem. Gracze, którzy są 'superrationalni', mogą podejmować decyzje, które na pierwszy rzut oka wydają się nieoptymalne, ale przynoszą większe korzyści wszystkim uczestnikom w dłuższym okresie.

### Przykłady zastosowania:

- **Dylemat więźnia**: W klasycznym dylemacie więźnia dwóch graczy ma wybór między współpracą a zdradą. Tradycyjna teoria gier sugeruje, że racjonalne jest zdradzenie partnera, aby zminimalizować ryzyko. Jednak w podejściu superrationalnym, jeśli obaj gracze uznają, że najlepszym rozwiązaniem dla obu jest współpraca, to obaj wybiorą współpracę, osiągając lepszy wynik ogólny.

Superrationality jest interesującą koncepcją, która wskazuje na potencjalne korzyści płynące z rezygnacji z indywidualnie racjonalnych decyzji na rzecz podejścia bardziej zorientowanego na wspólnotę i wspólne dobro.



ZADANIE 11

Punkt równowagi Nasha to pojęcie w teorii gier, które odnosi się do sytuacji, w której żaden z graczy nie może poprawić swojego wyniku przez zmianę strategii, zakładając, że strategie innych graczy pozostają niezmienione. Jest to kluczowe pojęcie w niemal każdej grze strategicznej, ponieważ wskazuje na stabilne rozwiązania, w których żaden z uczestników nie ma motywacji do jednostronnej zmiany swojego wyboru.

### Dylemat więźnia

Dylemat więźnia to klasyczny przykład w teorii gier, który demonstruje, jak racjonalne podejmowanie decyzji przez indywidualnych graczy może prowadzić do suboptymalnych wyników dla wszystkich uczestników. Jest to gra o sumie niezerowej, w której każdy gracz ma wybór między współpracą (C) a zdradą (D). Nagrody są rozdzielane na podstawie wyborów obu graczy:

- Jeśli obaj gracze współpracują, obaj otrzymują stosunkowo korzystną nagrodę (na przykład 3 punkty dla każdego).
- Jeśli jeden gracz zdradza, a drugi współpracuje, zdrajca otrzymuje najwyższą nagrodę (na przykład 5 punktów), a współpracujący gracz otrzymuje najniższą nagrodę (0 punktów).
- Jeśli obaj gracze zdradzają, obaj otrzymują nagrodę niższą niż za współpracę, ale wyższą niż dla zdradzanego (na przykład 1 punkt dla każdego).

### Punkt równowagi Nasha w dylemacie więźnia

W dylemacie więźnia punkt równowagi Nasha występuje, gdy obaj gracze decydują się na zdradę. Dlaczego tak jest?

1. **Rozważanie decyzji**: Jeśli gracz A współpracuje, gracz B może zyskać więcej, decydując się na zdradę (5 punktów zamiast 3). Analogicznie, jeśli gracz A zdradza, najlepszym wyborem dla gracza B jest również zdrada, aby uniknąć najgorszego wyniku (0 punktów) i zdobyć 1 punkt. 

2. **Zmiana strategii nie poprawia wyniku**: W punkcie równowagi Nasha, zmiana strategii przez któregokolwiek z graczy (z zdrady na współpracę) tylko pogorszyłaby ich sytuację. Jeśli jeden z graczy postanowi zdradzić, a drugi zmieni na współpracę, ten, który zdecyduje się na współpracę, skończy z zerowym wynikiem.

### Zastosowanie równowagi Nasha

Punkt równowagi Nasha pokazuje ograniczenia i potencjalne pułapki w podejmowaniu decyzji w sytuacjach, gdzie interesy graczy są częściowo sprzeczne, ale też częściowo zbieżne. W dylemacie więźnia równowaga Nasha prowadzi do suboptymalnego wyniku, gdzie obaj gracze decydują się na zdradę, pomimo że obaj mogliby uzyskać lepszy wynik, gdyby obaj zdecydowali się na współpracę.

To rozwiązanie rzuca światło na wiele rzeczywistych scenariuszy, jak negocjacje, politykę czy strategie biznesowe, gdzie brak zaufania i ryzyko związane z uzależnieniem od decyzji innych często prowadzi do gorszych wyników. Pokazuje również wartość komunikacji i budowania zaufania w różnych interakcjach społecznych i ekonomicznych.

=====================================================================================
W kontekście gry w dylemat więźnia, gdzie istnieje wielu graczy, rozgrywki są powtarzalne, a gracze są rozpoznawalni przez unikalne identyfikatory, stworzenie agenta, który efektywnie maksymalizuje sumaryczny wynik z wielu gier, wymaga zastosowania bardziej zaawansowanych strategii niż prosta decyzja o zdradzie czy współpracy w pojedynczej grze. Oto kilka koncepcji, które mogą pomóc w konstrukcji takiego agenta:

### 1. Strategia tit-for-tat (wzajemność)
Jest to jedna z najbardziej znanych i skutecznych strategii w dylemacie więźnia. Agent zaczyna od współpracy, a następnie na każdy ruch przeciwnika odpowiada takim samym ruchem, jakiego przeciwnik użył w poprzedniej rundzie. Strategia ta promuje współpracę, ale również szybko karze zdradę, co zniechęca do wykorzystywania agenta.

### 2. Wykorzystanie unikalnych identyfikatorów
Ponieważ każdy gracz przedstawia się przed rozgrywką swoim unikalnym identyfikatorem, agent może użyć tej informacji do tworzenia i utrzymywania historii interakcji z każdym graczem. To pozwala na dostosowywanie strategii do konkretnego przeciwnika, na podstawie wcześniejszych doświadczeń z nim. Na przykład, jeśli gracz X zwykle zdradza, agent może zdecydować się na zdradę od początku, aby minimalizować straty.

### 3. Adaptacyjne strategie
Agent może na bieżąco dostosowywać swoją strategię w zależności od ogólnej dynamiki gry. Na przykład, jeśli większość graczy zazwyczaj współpracuje, agent może preferować współpracę, aby maksymalizować swoje zyski. W przeciwnym razie, jeśli dominuje zdrada, agent może zastosować bardziej ostrożne podejście.

### 4. Długoterminowa optymalizacja
Zamiast maksymalizować zysk w pojedynczej grze, agent powinien skupić się na maksymalizacji sumarycznego wyniku z wielu gier. To może oznaczać akceptowanie niższego wyniku w jednej grze na korzyść lepszego ogólnego rezultatu, szczególnie jeśli przez to buduje się reputację jako gracz godny zaufania.

### 5. Analiza ryzyka i zmienności
Agent powinien także analizować zmienność wyników i ryzyko związane z różnymi strategiami. W pewnych sytuacjach, minimalizowanie ryzyka dużych strat może być ważniejsze niż potencjalnie większe, ale ryzykowne zyski.

### 6. Wzmacnianie współpracy
Agent może stosować strategie wzmacniające współpracę wśród innych graczy, na przykład przez wyraźne nagradzanie współpracy innych, co może prowadzić do bardziej kooperacyjnego środowiska gry, korzystnego dla wszystkich uczestników.