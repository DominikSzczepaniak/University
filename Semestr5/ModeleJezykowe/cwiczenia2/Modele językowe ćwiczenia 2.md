# Modele językowe ćwiczenia 2
# 7/8
## ==🟢Zadanie 1== 
Perplexity to metryka która mówi jak źle model przewiduje kolejne słowo. Im niższy wynik tym lepszy jest model.
n-gram - przewidujemy kolejne słowo na podstawie n-1 poprzednich słów
unigramowy - korzystamy tylko z ostatniego słowa
bigramowy - korzystamy tylko z dwóch ostatnich słów
k = 10

Zakładamy, że tokeny to pojedyczne cyfry. Wtedy n = k, żebyśmy wiedzieli kiedy kończy się blok i robimy ppb jednostajne na dowolną liczbę. 
Dla unigramu i bigramu nie wiemy w zasadzie nic, więc losujemy z takim samym ppb kolejną cyfrę. Czyli perplexity = 10
Dla n-gramowego używamy n=10 i wtedy wiemy kiedy możemy zakończyć blok, a kiedy losować losową cyfrę która zacznie kolejny blok. 
Perplexity ma wzór:
![](Modele%20je%CC%A8zykowe%20c%CC%81wiczenia%202/Zrzut%20ekranu%202024-11-3%20o%2017.52.06.png)
Gdzie x to wydarzenia, a p(x) to ich prawdopodobieństwa. Mamy 10 wydarzeń - 9 z nich to kontynuowanie bloku, a 1 to losowanie kolejnego wydarzenia, więc nasze perplexity jest równe
![](Modele%20je%CC%A8zykowe%20c%CC%81wiczenia%202/Zrzut%20ekranu%202024-11-3%20o%2017.54.02.png) = 10

## ==🟢Zadanie 2== 
Jeśli perplexity jest liczone na podstawie prawdpodobieństwa kolejnych wyrazów w zdaniu, to jeżeli perplexity ogólnej próbki statystycznej jest mniejsze niż danych tekstów, to te teksty miały inny rozkład prawdopodobieństwa niż ogólna próbka statystyczna tekstów. Ponieważ model statystyczny trzyma bardzo dużą ilość tekstów w swojej pamięci, to można założyć, że jego próbka statystyczna jest tą poprawną. To byłoby rozwiązanie w sytuacji idealnej, w której bot produkuje teksty bez wpływu promptera. 

Model językowy może stosować natomiast różne techniki - np. znak wodny albo zostać zmuszony przez promptera na odpowiadanie w dany sposób. Wtedy prawdopodobieństwo będzie zmienione i próbka statystyczna z wszystkich tekstów nie będzie miarodajna. Prompter może prosić o takie odpowiedzi które w normalnym świecie mają bardzo niskie prawdopodobieństwo wystąpienia. 

## ==🟢Zadanie 3== 
**a)** Jeżeli na k-tej pozycji mamy określony wyraz, a jest on rzadki np. w języku angielskim zaczynamy zdania od I, ale rzadko kiedy I występuje w środku zdania (oprócz np. zdań pytających) no to jeżeli nie zaczniemy zdania od formy pytającej to może się trafić, że jeżeli wstawimy słowo na k-tą pozycję to nie będzie istnieć ppb dla 2 czy 3 gramowego modelu, ani w zasadzie dla żadnego innego. 

Chcemy wybrac takie wyrazy aby P(xk | xk-1 xk-2 xk-3 …) bylo jak najwieksze.
Ja bym najpierw wybral teksty ktore maja najwieksze prawdopodobienstwo P(xk | xk-1 xk-2) w modelach 2 gramowych i odpowiednie ppb w modelu 3-gramowym. Nastepnie na podstawie tego musialbym wybierac tylko jeden wyraz aby uzupelniac poprzednikow. Generowanie tekstow na prawo od k jest łatwe znając poprzednie wyrazy.
Czyli generowałbym bardzo dużo tekstów i sprawdzał które mają na k-tym miejscu wyraz który ma tam być.

Jednym z pomysłów byłoby też branie słów z dużym prawdopodobieństwem i następnie permutacje tych zdań w których dany wyraz ma być na k-tym miejscu.


**b)** Nie sprawdzi się ponieważ wylosowanie x-1 wyrazów nie gwarantuje że wyraz na pozycji x będzie pasował. Możemy forcować, że jeżeli zadnie w ogóle nie będzie pasowało to zakończymy poprzednie zdanie kropką i spróbujemy rozpocząć kolejne. 

**Proponowane rozwiązanie:**

	1.	**Dynamiczne przypisywanie wartości do pozycji nieparzystych:** Najpierw ustal wartości na pozycjach parzystych, a następnie generuj słowa na pozycjach nieparzystych tak, by dopasować się do kontekstu.
	2.	**Metoda wsteczna (backtracking):** Jeśli żadne z możliwych losowanych słów na pozycji nieparzystej nie pasuje do wyrazu na następnej pozycji parzystej, wracamy do poprzedniej pozycji nieparzystej i zmieniamy wybór.
	3.	**Metoda sekwencyjnego optymalizowania z użyciem beam search:** Każda kombinacja zaczyna się od pewnych wyrazów na parzystych pozycjach, a następnie generujemy możliwe wartości na nieparzystych pozycjach, co pozwala na dopasowanie kontekstowe.

**c)** Podobnie jak w poprzednim - możemy wylosować takie słowa, że ostatni wyraz będzie niemożliwy w danym zdaniu. Zdania mają nie być jakoś bardzo długie, więc myślę, że beam-search powinien tutaj zadziałać. Zawsze też jest opcja zakończenia jednej części zdania i rozpoczęcia kolejnej po kropce.

**Proponowane rozwiązanie:**

	1.	**Beam search z optymalizacją na końcowe dopasowanie:** Rozpocznij generowanie od pierwszego słowa, jednocześnie próbując zachować możliwy kontekst końcowego słowa, używając beam search do zachowania kilku najbardziej prawdopodobnych wersji tekstu.
	2.	**Heurystyka ograniczenia długości:** Tworząc tekst, wprowadź heurystykę, aby długość była zgodna z założonym M, a równocześnie kończyła się słowem o wysokim prawdopodobieństwie w kontekście ostatniego słowa.
	3.	**Dwukierunkowe losowanie:** Rozpocznij generację zarówno od pierwszego słowa w przód, jak i od ostatniego słowa wstecz, łącząc te fragmenty tam, gdzie kontekst jest spójny.


**d)** Ponieważ takich wyrazów jest bardzo mało i mamy ograniczony wybór to ppb że każde kolejne słowo będzie pasowało do poprzedniego które kończyło się na dany sufiks jest bardzo niskie. To co bym zrobił to, ze względu na małą ilość wyrazów, używał beam-searcha. Rozpatrujemy bardzo dużo opcji, ale nie jest ich aż tak dużo, a możemy się cofać do bardziej prawdopodobnych opcji.

Oto bardziej szczegółowe uzupełnienie Twoich odpowiedzi dla każdego z podpunktów:

### a) Losowanie tekstu o długości M, który na pozycji k ma określony wyraz

Problem z naturalnym podejściem polega na tym, że losowe generowanie od początku do końca tekstu prowadzi do bardzo niskiej szansy wylosowania słowa na pozycji , jeśli to słowo ma rzadkie wystąpienie w kontekście modelu n-gramowego. Dlatego, po uzyskaniu losowego tekstu, musimy wielokrotnie powtarzać generację, co jest nieefektywne.

**Proponowane rozwiązanie:**

	1.	**Algorytm oparty na maksymalizacji prawdopodobieństwa kontekstu:** Wybieramy słowa do pozycji  i , bazując na maksymalnym prawdopodobieństwie warunkowym, np.  dla bigramów lub  dla trigramów. Następnie, konstruujemy ścieżki od początku aż do pozycji , by zapewnić zgodność kontekstową.
	2.	**Użycie beam search z priorytetem dla tekstów o dużym prawdopodobieństwie:** Ustalając priorytet dla słów najczęściej pojawiających się w kontekście z pozycją , możemy generować kilka równoległych wersji tekstu, a następnie wybrać tę, która spełnia wymóg wystąpienia słowa na pozycji .

### b) Losowanie tekstu o długości M, który na pozycjach parzystych ma określone wyrazy

Naturalne losowanie od lewej do prawej często nie spełni wymagania, aby wyrazy na pozycjach parzystych odpowiadały z góry ustalonym słowom, ponieważ ich kontekst nie zawsze będzie pasował do tego, co wylosowaliśmy na pozycjach nieparzystych.

**Proponowane rozwiązanie:**

	1.	**Dynamiczne przypisywanie wartości do pozycji nieparzystych:** Najpierw ustal wartości na pozycjach parzystych, a następnie generuj słowa na pozycjach nieparzystych tak, by dopasować się do kontekstu.
	2.	**Metoda wsteczna (backtracking):** Jeśli żadne z możliwych losowanych słów na pozycji nieparzystej nie pasuje do wyrazu na następnej pozycji parzystej, wracamy do poprzedniej pozycji nieparzystej i zmieniamy wybór.
	3.	**Metoda sekwencyjnego optymalizowania z użyciem beam search:** Każda kombinacja zaczyna się od pewnych wyrazów na parzystych pozycjach, a następnie generujemy możliwe wartości na nieparzystych pozycjach, co pozwala na dopasowanie kontekstowe.

### c) Losowanie niezbyt długiego tekstu o zadanym pierwszym i ostatnim słowie

Naturalna metoda często generuje zdania, gdzie ostatnie słowo może nie pasować do kontekstu, dlatego sprawdzenie i ponowne losowanie są nieefektywne.

**Proponowane rozwiązanie:**

	1.	**Beam search z optymalizacją na końcowe dopasowanie:** Rozpocznij generowanie od pierwszego słowa, jednocześnie próbując zachować możliwy kontekst końcowego słowa, używając beam search do zachowania kilku najbardziej prawdopodobnych wersji tekstu.
	2.	**Heurystyka ograniczenia długości:** Tworząc tekst, wprowadź heurystykę, aby długość była zgodna z założonym M, a równocześnie kończyła się słowem o wysokim prawdopodobieństwie w kontekście ostatniego słowa.
	3.	**Dwukierunkowe losowanie:** Rozpocznij generację zarówno od pierwszego słowa w przód, jak i od ostatniego słowa wstecz, łącząc te fragmenty tam, gdzie kontekst jest spójny.

### d) Losowanie tekstu o długości n, w którym każde słowo ma określony sufiks

Problem polega na tym, że naturalna metoda nie gwarantuje trafienia na słowa o odpowiednim sufiksie w kolejnych losowaniach, co prowadzi do wielu nieudanych prób.

**Proponowane rozwiązanie:**

	1.	**Beam search skoncentrowany na dopasowaniu sufiksów:** Rozpocznij generowanie z możliwością wyboru słów z odpowiednimi sufiksami, stosując beam search, aby kontynuować tylko te ścieżki, które mają wysokie prawdopodobieństwo sukcesu.
	2.	**Budowanie sekwencyjne z filtracją sufiksów:** Tworząc kolejne słowa, filtruj słowa o odpowiednich sufiksach, jednocześnie minimalizując liczbę możliwych kontynuacji dla każdej ścieżki.
	3.	*Zastosowanie algorytmu A do optymalizacji tekstu z dopasowaniem sufiksów:** Algorytm A* wykorzystuje heurystykę, która priorytetuje najbardziej prawdopodobne przejścia zgodne z wymaganiami, pozwalając na szybsze znalezienie sekwencji o zadanych sufiksach.

## ==🟢Zadanie 4==
Jednym z przykładów jest przykładowo podpunkt a w poprzednim zadaniu. Jeżeli nauczyliśmy bota układać zdania od tyłu to jest w stanie zacząć od zdania które na k-tym miejscu ma wyraz k-ty i ułożyć zdanie danej długości. Jesteśmy więc w stanie układać dość dobrze zdania które mają na jakimś miejscu dany wyraz, bo najpierw użyjemy odwróconego bota, a później już normalnego (lewo-prawo).
 
### 3. Model może służyć jako fundament do transferu wiedzy

	* 	**Przyspieszenie treningu nowego modelu:** Z racji podobnej struktury i wielu wspólnych wzorców językowych, wnioski wyciągnięte z analizy wyników tego modelu mogą posłużyć jako „podkład” do transfer learningu w niektórych specyficznych zadaniach lub przy optymalizacji parametrów treningu. W związku z tym istnieje szansa na przyspieszenie treningu i poprawę jakości nowego modelu.
	* 	**Stworzenie sieci eksperymentalnej:** Model może posłużyć do badań nad transferem wiedzy pomiędzy modelami przeszkolonymi na różnych wersjach danych, zwłaszcza w przypadku nietypowych układów tekstu.

### 4. Model odwróconego języka może mieć potencjalne zastosowania praktyczne

	* 	**Analiza struktury i odwrotnych fraz:** Można zbadać model, by lepiej zrozumieć, jak radzi sobie z odwrotnymi sekwencjami i czy dałoby się go wykorzystać w zadaniach związanych z odwracaniem tekstu lub generowaniem tekstu z nietypową strukturą.
	* 	**Aplikacje w przetwarzaniu zaszyfrowanych i zniekształconych danych:** Model może mieć zastosowanie w obszarze analizy zaszyfrowanych tekstów, dekodowania nietypowych danych czy przetwarzania struktur o odwrotnej kolejności, co mogłoby być cenne np. w szyfrowaniu lub kompresji tekstu.

## ==🟢Zadanie 7==
Dla wyrazów z większym prawdopodobieństwem nadajemy krótsze ciągi bitowe, a dla wyrazów z większym prawdopodobieństwem nadajemy dłuższe ciągi bitowe. 

Model językowy działa tak, że na podstawie poprzednich wyrazów daje prawdopodobieństwa wyrazów kolejnych. Ponieważ zawsze prawdopodobieństwa są takie same możemy użyc to do kompresji. Jeśli znamy cały poprzedni tekst oraz dostajemy jakiś skompresowany token który mówi nam które prawdopodobieństwo wybrać możemy odszyfrować skompresowany tekst.
Więc kompresujemy go w następujący sposób: 
Idąc po kolei słowami patrzymy jakie prawdopodobieństwa zostały przypisane odpowiednim wyrazom i na podstawie tego nadajemy jakiś kod wyrazowi który odpowiada temu który powinien być kolejny w oryginalnym tekście. **Ja bym to widział tak, że możemy przypisywać po prostu wartość liczbową równą miejscu w posortowanej malejąco tablicy prawdopodobieństw.** Wtedy nasz skompresowany tekst ma dla każdego wyrazu tylko jedną liczbę zamiast ciągu znaków. Możemy to kompresować mocniej i np. używać ciągu binarnego który przypiszemy w jakiś sposób.


## ==🟢Zadanie 8==

Problemem jest tokenizer, którego token może się zaczynać od spacji. Takich tokenów będzie o wiele mniej niż tokenów niezaczynających się od spacji przez to możemy dostawać o wiele mniej prawdopodobne słowa jako wynik.


## ==🟢Zadanie 9==
Ten tekst charakteryzuje się dużą ilością rymów które powtarzają się w jakiś określonych schematach (np. na końcu linii która może mieć różną długość). Te rymy czasem się również zmieniają (nie chcemy ciągle rymować tej samej końcówki wyrazu przez cały tekst).
Ja bym to generował w następujący sposób:
1. Losujemy wyraz który będziemy rymować.  
2. Losujemy wyrazy i rymujemy na końcu kolejnej linii z wyrazem który mieliśmy rymować.
3. Z jakimś ppb zmieniamy rym i losujemy odpowiednio dla niego.


Taki tekst, jak podany wierszyk, charakteryzuje się kilkoma cechami, które mają wpływ na generację:

	1.	**Rym i rytm**: Każda linijka lub co najmniej każda para linijek powinna rymować się i mieć odpowiedni rytm, czyli liczbę sylab lub akcentów w linijce.
	2.	**Powtarzalność i struktura**: W wierszykach często stosuje się powtórzenia fraz lub struktur zdań (np. „W prawym bucie, w lewym bucie”), co nadaje tekstowi melodyczność.
	3.	**Prosty język i tematyka**: Wierszyki zwykle opisują proste sytuacje lub emocje w sposób obrazowy, co jest zrozumiałe nawet dla dzieci.
	4.	**Często ograniczona liczba wyrazów**: Większość wierszyków jest krótka, więc trzeba efektywnie wybierać wyrazy, aby zachować treść i rymy.

### Proponowany algorytm do generacji wierszyków z wykorzystaniem modelu (np. jak Papuga):

**Krok 1: Określenie struktury wiersza**

Zacznij od określenia liczby linijek, schematu rymów (np. ABAB lub AABB) oraz liczby sylab w każdej linijce. Na przykład:

	* 	Wierszyk będzie miał 4 linijki.
	* 	Struktura rymów to AABB (linijka 1 rymuje się z linijką 2, a linijka 3 z linijką 4).
	* 	Każda linijka powinna mieć np. 8 sylab.

**Krok 2: Wygenerowanie fraz rymujących**

	1.	**Wybór pierwszego wersu**: Używając modelu, wygeneruj początkowy wers (np. „Biega, krzyczy pan Hilary”).
	2.	**Generowanie rymów**: Dla każdego nowego wersu potrzebującego rymu (np. 2 i 4 wers), sprawdź, jakie wyrazy końcowe zostały wygenerowane dla poprzednich wersów i dopasuj rymy. Można to zrobić poprzez:
	* 	Przeszukiwanie bazy rymów lub słownika rymów, aby znaleźć pasujące wyrazy.
	* 	Wymuszanie modelu na generowanie określonego rymu przez iteracyjne próby, z użyciem promptu podpowiadającego.

**Krok 3: Zapewnienie rytmu (sylab i akcentów)**

	* 	Po wygenerowaniu każdej linijki przelicz liczbę sylab. Jeśli rytm jest nieodpowiedni, można lekko modyfikować linijkę lub używać narzędzi do wymiany słów na synonimy, zachowując odpowiednią liczbę sylab.
	* 	Można również wymuszać na modelu generowanie prostych, rytmicznych konstrukcji przez ustawienie prostej struktury zdań i konkretnego słownictwa.

**Krok 4: Użycie beam search dla zwiększenia spójności**

	* 	Generując kolejne linijki, możesz użyć beam search, aby wybrać najlepsze frazy w kontekście całości wiersza. Beam search pozwala na rozważenie kilku alternatywnych fraz i wybór tej, która najlepiej pasuje zarówno pod względem treści, jak i rymów.
	* 	Dla każdej linijki generuj kilka wersji i wybieraj te, które mają największe prawdopodobieństwo przy zachowaniu sensu i rymów, by stworzyć spójny wierszyk.

**Krok 5: Automatyczne dopasowanie struktury do wierszyka**

	* 	Jeśli model generuje wersy, które nie pasują do schematu rytmicznego lub rymowego, możesz wprowadzić dodatkową funkcję korekty struktury: przeformułowanie lub zamianę fragmentów wersu na pasujące wyrażenia.
	* 	Możesz także wymusić wprowadzenie konkretnych wyrazów lub fraz, by model powtarzał określone struktury (np. „W prawym bucie, w lewym bucie”).

**Podsumowanie**

Dzięki tej strategii można generować wierszyki o pożądanych właściwościach – z rymami, odpowiednim rytmem i spójnością treści, minimalizując potrzebę ręcznych poprawek i maksymalizując efektywność generacji.