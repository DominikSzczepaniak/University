def kompresja(tekst):
    ilosc = 1
    ostatnia_litera = tekst[0]
    wynik = []
    for i in tekst[1:]:
        if(ostatnia_litera != i):
            wynik.append([ilosc, ostatnia_litera])
            ilosc = 1
            ostatnia_litera = i
        else:
            ilosc += 1
    wynik.append((ilosc, ostatnia_litera))
    return wynik

def dekompresja(tab):
    tekst = ""
    for i in tab:
        tekst += i[0] * i[1]
    return tekst

tekst = """
Tom pierwszy
I
Marta i Justyna wracają z kościoła. Po drodze spotykają Janka, powożącego drabiniastym wozem, oraz Różyca i Kirłę, jadących do dworku Korczyńskich.

II
Korczyńscy, wraz z przybyłymi gośćmi, oczekują na przyjazd Witolda i Leoni (dzieci mają spędzić w domu wakacje). Kirło pozwala sobie na niesmaczny żart: sprowadza przed zgromadzonych niekompletnie ubranego ojca Justyny. Dziewczyna oburza się. Przybywają dzieci Korczyńskich.
III
Ojciec Benedykta, Stanisław, studiował niegdyś w akademii wileńskiej i pragnął, aby jego synowie (Andrzej, Dominik i Benedykt) również posiadali wyższe wykształcenie. Z tego powodu wszystkich wysłał na studia. W 1861 r. Benedykt powrócił do Korczyna. W tym czasie jego rodzice już nie żyli, siostra zaś była mężatką. W domu Benedykta znalazła schronienie Marta Korczyńska - sierota wychowana przez jego rodziców. Bracia żyli ze sobą w zgodzie. Andrzej zginął w powstaniu w 1863 r. Dominik wyjechał i osiedlił się gdzieś w Rosji. Benedykt jest człowiekiem pracowitym i sam prowadzi gospodarstwo, ale nie powodzi mu się najlepiej. Wiedzie ciągłe spory z Bohatyrowiczami, nie potrafi też dojść do porozumienia ze swą żoną, która czuje się zawiedziona małżeństwem.

IV
W Korczynie odbywa się przyjęcie wydane z okazji imienin Emilii (jest dzień 30 czerwca). Wśród licznie przybyłych gości toczą się najróżniejsze rozmowy. Witold atakuje Różyca i innych bogatych posiadaczy, że nic nie robią dla dobra tej ziemi i jej mieszkańców. Benedykt rozmawia z innymi mężczyznami o polityce, gazetach, gospodarstwie i procesach. W pewnym momencie dochodzi do - radosnego dla obojga - spotkania Witolda z szesnastoletnią córką Kirłów - Marynią. Ignacy gra na skrzypcach, Justyna zaś akompaniuje mu. Później dochodzi do rozmowy Zygmunta z Justyną. Zygmunt zwierza się pannie ze swych uczuć, jednak Justyna broni się i odrzuca jego miłosne deklaracje. Natomiast Różyc ciągle z daleka przypatruje się pannie, która coraz bardziej mu się podoba.

V
Justyna spaceruje po okolicy, przypominając sobie swoje dzieje i rozmyślając nad własnym życiem. Niegdyś wychowywała się ona w domu pani Andrzejowej Korczyńskiej i wówczas zrodziło się pomiędzy nią a Zygmuntem szczere uczucie. Zygmunt pragnął ją poślubić, jednak sprzeciwiła się temu jego matka. Po pewnym czasie młodzieniec wyjechał za granicę celem kształcenia się, a po dwóch latach powrócił razem z młodą żoną. Justyna od tego czasu czuje się pokrzywdzona i zraniona, co jest powodem jej oziębłości i melancholii.

W trakcie rozważań Justyna dochodzi do pola, na którym pracuje Janek Bohatyrowicz. Jest on uradowany tym nieoczekiwanym spotkaniem. Rozmawiając dochodzą do chaty Janka, który zaprasza pannę do środka. Tutaj Justyna styka się z Anzelmem i przyrodnią siostrą Janka - Antolką. W trakcie ich rozmowy do chaty schodzą się sąsiedzi zaciekawieni niecodzienną wizytą “panienki z dworu”. Fabian Bohatyrowicz prowadzi swoje wywody na temat procesów toczących się pomiędzy mieszkańcami zaścianka a Benedyktem. Anzelm - w przeciwieństwie do Fabiana - jest nastrojony pokojowo i przyznaje rację Korczyńskiemu. Pomimo dziwnego nieco przyjęcia, Justyna dochodzi do wniosku, że w chacie tej czuje się lepiej niż w domu Benedykta.

VI
Anzelm, Janek i Justyna idą do parowu Jana i Cecylii - protoplastów rodu Bohatyrowiczów. Po drodze spotykają licznych mieszkańców wsi, między innymi starego, zdziwaczałego Jakuba i jego wnuczkę Jadwigę. Przy drodze stoi grupka mężczyzn, którzy wiodą dyskurs dotyczący procesów. Ludzie ci są nieprzychylnie nastawieni do Korczyńskiego.

W parowie znajduje się mogiła Jana i Cecylii, na której widnieje data: 1549 r. Anzelm przygotowuje tu nowy krzyż, aby ustawić go na miejscu starego i bardzo już zniszczonego. O zachodzie słońca Anzelm przerywa swą pracę i opowiada Justynie historię życia Jana i Cecylii oraz powstania rodu. Jan pochodził z gminu, Cecylia zaś z bogatego rodu. Oboje przybyli w to miejsce, aby ukryć się przed oczami ludzi. Odważnie rozpoczęli podbój dziewiczej puszczy i przekształcili ją w żyzne pola i łąki. Mieli sześciu synów i sześć córek, którzy wchodząc w związki małżeńskie z mieszkańcami okolicznych osad - osiedlali się tu i pracowali wraz z rodzicami. Budowali domy, karczowali lasy, uprawiali zboża, hodowali owce, krowy i konie. Po osiemdziesięciu latach od przybycia założycieli osada bardzo się rozwinęła. Pewnego razu zjechał tu król Zygmunt August i w nagrodę za trud żyjących jeszcze, ponad stuletnich Jana i Cecylii, nobilitował ich ród i pozwolił im używać herbu Pomian - głowy żubra umieszczonej na żółtym polu.

Tom drugi
I
Kirłowie są ludźmi raczej ubogimi, ale ich dom (Olszynka) i zagroda tętnią życiem. Pewnego dnia z wizytą przybywa Różyc, daleki kuzyn Marii Kirłowej. Podczas rozmowy przyznaje się do używania narkotyków. Wyznaje też, że pożąda Justyny, ale nie ma zamiaru jej poślubić z uwagi na jej pochodzenie i brak majątku. Następnie proponuje Kirle posadę zarządcy swej posiadłości - Wołowszczyzny. Kirłowa jednak nie przyjmuje tej propozycji. Różyc proponuje jej jeszcze, że przejmie finansową stronę wykształcenia jej synów, na co pani domu wyraża zgodę. W tym czasie Witold z Marynią wiodą długą rozmowę, której tematem jest praca wśród chłopów.
II
Witold z Leonią chcą nakłonić Martę do leczenia się, ona jednak broni się przed tym na różne sposoby i ucieka przed natrętnymi dziećmi i lekarzem do spiżarni. Emilia dostaje ostrych ataków choroby nerwowej, więcej w tym jednak udawania niż prawdziwych dolegliwości. Do Korczyna przybywa Darzecki z dwiema córkami i upomina się u Benedykta o posag żony. Po odjeździe Darzeckiego Witold wypowiada swój krytyczny sąd o osobie wuja i zarzuca ojcu, że płaszczy się przed człowiekiem tak egoistycznym i bezwartościowym. Dochodzi do ostrego starcia pomiędzy ojcem i synem. Wkrótce potem do Witolda przychodzi Julek Bohatyrowicz. Obaj młodzieńcy wychodzą. W czasie śniadania przybywa Kirło. Żartuje z Teresy mówiąc, że o jej rękę będzie się starał Różyc. Teresa traktuje poważnie słowa Kirły, ale szybko spotyka ją bolesne rozczarowanie, ponieważ zebrani sądzą, że owszem: Różyc będzie się starał o rękę, ale o rękę Justyny. Myśli Justyny krążą natomiast coraz częściej wokół osoby Janka Bohatyrowicza.

III
W Bohatyrowiczach trwają żniwa. Jan spotyka się w polu z Justyną, która decyduje się pomóc mu w pracy. Pomiędzy Fabianem i jego synami a Ładysiem i jego żoną wybucha bójka. Janek uspokaja walczących. Zjawia się tu też Witold. Później Witold spotyka Anzelma, który odkrywa podobieństwo panicza do nieżyjącego Andrzeja Korczyńskiego. Witold z Anzelmem wiodą długą i poważną rozmowę.

IV
Janek i Justyna płyną łodzią do grobu poległych powstańców. Po drodze spostrzegają Julka łowiącego ryby. Na piaszczystym brzegu Niemna Janek opowiada, jak ostatni raz w życiu - w tym właśnie miejscu - widział swego ojca odchodzącego z powstańcami.

Tamtego zimowego wieczoru wielu ludzi żegnało tu swoich krewnych i znajomych. W miesiąc później Anzelm, wracający prosto z pola bitwy, przyniósł wiadomość o śmierci Andrzeja Korczyńskiego i Jerzego Bohatyrowicza.

Zrywa się burza, która skłania młodych do powrotu do chaty Anzelma. W czasie przeprawy rzeką Janek daje dowody swej odwagi, zręczności i siły, walcząc ze wzburzonym żywiołem. Justynę widok ten napełnia spokojem i zaufaniem do osoby Janka oraz podsyca rodzące się w jej sercu uczucie.

V
W chacie Anzelma Antosia, Elżunia i Justyna rozmawiają o strojach i zbliżającym się weselu Elżuni. Anzelm włącza się do rozmowy. Następnie wszyscy - wraz z Jankiem - zasiadają do wieczerzy, nie przerywając konwersacji. Anzelm przez cały czas jest niezwykle grzeczny i przyjacielsko odnosi się do Justyny. Po kolacji Anzelm pozostaje sam na sam z Justyną i opowiada jej historię swej odwzajemnionej miłości do Marty. Pomimo łączącego ich uczucia Marta odrzuciła jego oświadczyny, co wzbudziło w nim wielki żal i doprowadziło do tego, że zapadł na ciężką chorobę, która trwała przez dziewięć lat. Po częściowym wyzdrowieniu Anzelm zajął się urządzeniem i pielęgnacją swego wspaniałego sadu i pomagał Jankowi w prowadzeniu gospodarstwa.

Do chaty przybywa stary Jakub wraz z wnuczką, Jadwigą Domuntówną. Starzec opowiada historię o swoim bracie Franciszku, który w 1812 r. wyruszył z legionami Napoleona na wojnę. Po pewnym czasie, będąc niedaleko domu, Franciszek zapragnął choć na chwilę odwiedzić krewnych, ale w drodze zabłądził (a była to zimowa noc) i zamarzł o kilkadziesiąt metrów od rodzinnej chaty. W czasie trwania opowieści i po jej zakończeniu Jadwiga okazuje Janowi i Justynie swą zazdrość (kocha Janka, była pewna, że młody Bohatyrowicz właśnie ją wybierze na żonę), a następnie rozgniewana wychodzi wraz z Jakubem. Jan, Anzelm i Justyna wychodzą nocą, aby popatrzeć na Niemen. Na czółnach, wśród rybaków, dostrzegają Witolda. Niedługo potem Justyna wraca do Korczyna. Tutaj spotyka się z Martą, która opowiada, że w dworku była Kirłowa, która pragnęła dowiedzieć się, czy Justyna nie zgodziłaby się poślubić Różyca. Justyna niezbyt zainteresowana tą propozycją wypytuje, dlaczego Marta nie wyszła za Anzelma. Ta przyznaje się, że obawiała się wówczas szyderstw ze strony ludzi oraz ciężkiej pracy. Potem długo jeszcze kobiety rozmawiają o Anzelmie i jego gospodarstwie.

Tom trzeci
I
Pani Andrzejowa Korczyńska zawsze była osobą powściągliwą i opanowaną. Za mąż wyszła z miłości. Była patriotką. Nie potrafiła tylko nigdy pokonać samej siebie w jednym względzie: nie umiała zmusić się do bliskiego obcowania z chłopami i tym różniła się od swego męża. Stan taki nie wynikał z pychy, ale ze zbytniego przyzwyczajenia do wykwintnych form, poezji i wzniosłości. Po śmierci męża powróciła do rodzinnego domu, ale choć nie okazywała na zewnątrz rozpaczy, również uśmiechu na jej twarzy nikt nie widywał. Benedykt pomagał jej w zarządzaniu gospodarstwem i majątkiem, ponieważ sama nie umiałaby sobie poradzić. Doszło jednak między nimi do sprzeczki, gdyż Benedykt zarzucał jej, że Zygmunta wychowuje “na francuskiego markiza, nie na polskiego obywatela, na panienkę, a nie na mężczyznę”. Ona natomiast twierdziła, że pragnie uchronić syna przed materializmem i przyziemnością, a wychować go dla wzniosłych myśli i idei.

Pani Andrzejowa zauważa, że Zygmunt nie tylko nie ma talentu, który od dawna przepowiadali mu liczni krewni i znajomi, ale w dodatku nie kocha nikogo i niczego, jest zimny i obojętny. Nie kocha nawet swej żony. Ta jednak - pomimo całej obojętności, jaką jej okazywał - nie potrafi nigdy dłużej niż przez dwie godziny być urażona. Pomiędzy małżonkami dochodzi do czułej rozmowy, która schodzi na temat zamążpójścia Justyny. Klotylda okazuje zazdrość, jednak Zygmunt - nie zważając na to - jedzie do Korczyna. Klotylda jest z tego powodu bardzo rozżalona i skarży się pani Andrzejowej. Ta pociesza synową i podejmuje decyzję poważnej rozmowy z synem.

II
Justyna i Witold powracają z Bohatyrowicz do Korczyna wesoło rozmawiając. Słysząc podniesiony głos Benedykta Witold w pewnym momencie przyspiesza kroku i spostrzega, że jego ojciec łaje jednego z parobków za to, że ten uszkodził żniwiarkę. Witold objaśnia chłopu zasadę działania maszyny i podejmuje się ją naprawić. Później rozmawia z ojcem (wypowiada między innymi następujące słowa: “szczytem moich marzeń jest to, aby ludzie nie obchodzili się z ludźmi jak z bezmyślnymi bydlętami”). Benedykt zarzuca synowi zbytni idealizm i brak przywiązania do osoby ojca. Witold jest tym zdaniem zaszokowany i zasmucony.

Do dworku przybywa w tym czasie Kirło i wychwala zalety Różyca. Zamierza w ten sposób zachęcić Justynę do poślubienia tego człowieka. Benedykt reaguje na to wypowiadając niepochlebne zdanie dotyczące “darmozjadów”.

Po odejściu ojca, matki, Teresy i Kirły Witold wypowiada o Kirle swoje zdanie: że człowiek ten jest zacofany i że jest pasożytem.

Do dworu przybywa Elżunia i w imieniu Fabiana zaprasza Justynę do swej chaty. Tam Justyna poznaje Starzyńskiego - trzeciego z kolei męża matki Janka - oraz przyszłego zięcia Fabianów - Franka Jaśmonta. Do chaty tej po pewnym czasie przybywa też Witold. Następnie pojawia się Antosia, a w chwilę później Michał. Fabian skarży się nieco na biedę, jednak ogólnie panuje wesoły nastrój. Wieczorem Justyna z Witoldem powracają do domu. Następnego dnia Witold prosi matkę o pozwolenie, aby Leonia mogła pójść razem z nimi na wesele do Bohatyrowicz. Matka jednak słysząc tę prośbę - dostaje kolejnego ataku swej choroby.

Przez kilka następnych dni Benedykt i Witold często stykają się ze sobą i rozmawiają, ale rozmowy te traktują o obojętnych meczach i codziennych sprawach. Syn nie chce mówić o swoich przekonaniach i planach na przyszłość, natomiast ojciec niechętnie, a nieraz gwałtownie odnosi się do milczenia Witolda. Obaj stają się nerwowi i nie potrafią się porozumieć. Benedykt dowiaduje się w tym czasie, że wygrał proces z Bohatyrowiczami i poleca swojemu prawnikowi wyegzekwować należne 1000 rubli. Tego samego dnia przybywa do Korczyna Zygmunt i spotyka się z Justyną. Proponuje jej, aby przeniosła się do niego i została jego kochanką. Panna, która przyjęła go ozięble, stanowczo stwierdza, że nie żywi do niego żadnych uczuć. Obrażony Zygmunt wraca do domu. Tu dochodzi do rozmowy matki z synem. Zygmunt prosi, aby matka sprzedała Osowce i aby wraz z nim podróżowała po świecie. Matka odmawia. Rozmawiają o Klotyldzie i Justynie. Pani Andrzejowa dopiero teraz dostrzega błędy, które popełniła wychowując syna. Zygmunt porównuje miejscowy lud do bydła, a swojego nieżyjącego ojca nazywa szkodliwym szaleńcem. Dla matki jest to bolesny cios, który zabija w niej miłość do syna.

III
Do Bohatyrowicz zjeżdżają goście zaproszeni na wesele Elżuni. Wśród przybyłych znajdują się Bohatyrowicze, Jaśmontowie, Zaniewscy, Obuchowicze, Osipowicze, Łozowiccy, Staniewscy, Maciejewscy, Strzałkowscy, trzej Domuntowie - stryjeczni bracia Jadwigi, dwie panny Siemaszczanki z dwoma braćmi, właściciel folwarku stary Koroza wraz z dorosłymi dziećmi, Albin Jaśmont - właściciel folwarku ekonom z Osowiec, felczer oraz dzierżawca Józef Gieczołd z małżonką. Wszyscy są ubrani strojnie, choć nie według jednej mody. Następuje oczekiwanie na młodą parę i orszak weselny. Przybywa nieco spóźniony Kazimierz Jaśmont - właściciel folwarku pierwszy drużba. Wraz z jego przyjazdem rozpoczynają się uroczystości. Kazimierz od razu zwraca swą uwagę na Justynę, która mu się niezmiernie podoba. Jednak nie przeszkadza mu to pełnić obowiązków drużby. Na początek wygłasza piękną mowę skierowaną do młodej pary. Potem następuje błogosławieństwo młodych udzielone im przez rodziców i orszak wyrusza bryczkami w kierunku kościoła. Część gości jednak pozostaje i zasiada od razu do stołów. Fabian pełni obowiązki gospodarza, ale w duchu trapi się myślą o przegranym procesie. Po pewnym czasie rozmowa schodzi na ten właśnie temat. Przed wieczorem rozpoczyna się weselisko. Dochodzi do spotkania Marty i Anzelma. Spotykają się też Janek i Justyna. Przybywa Domuntówna, która jest teraz adorowana przez Kazimierza Jaśmonta. Witold przysłuchuje się gawędom Jakuba. Późnym wieczorem, po tańcach, wszyscy wypływają czółnami na Niemen. Tylko Anzelm i Marta pozostają przed chatą i wspominają czasy swej młodości. Bohatyrowicze pragną zgody z Benedyktem i proszą Witolda o wstawiennictwo u jego ojca w sprawie przegranego procesu.

IV
Benedykt rozmyśla nad swą przeszłością. Czyta też list od swego brata Dominika, który został mianowany w Rosji wysokim urzędnikiem (“tajnym sowietnikiem” - czyli tajnym radcą). Rozważania przerywa przybycie Witolda. Dochodzi do poważnej rozmowy. Ojciec po raz pierwszy od wielu lat szczerze mówi o swoich przeżyciach dawnych i teraźniejszych i odpiera liczne zarzuty syna. Wyrzuca z siebie wszystko to, co tłumił przez długie lata. Ojciec i syn wreszcie nawiązują między sobą autentyczny dialog.

Z rana Witold niesie do domu weselnego radosną wieść o pojednaniu i zawiadamia o tym zebranych tam jeszcze gości. Później przez cały dzień przebywa razem z ojcem radząc nad czymś, zaś wieczorem płynie razem z nim “na Mogiłę”, w której spoczywa Andrzej Korczyński.

Również pod wieczór kończą się gody Elżuni, którą orszak weselny odprowadza do domu męża. Jadwiga przeprasza Janka za przykry incydent, który miał miejsce poprzedniego wieczoru (rozżalona i załamana utratą ukochanego Janka rzuciła w niego i Justynę kamieniem, który na szczęście nie wyrządził im krzywdy). Janek - tak jak poprzedniego wieczoru - zachowuje się po rycersku i przebacza zniewagę. Później spotyka się nad Niemnem z Justyną i wyznaje jej swoją miłość.

V
Następnego dnia do Korczyna przybywają: Kirło z żoną i dziećmi oraz Zygmunt. Kirłowie rozmawiają z Justyną, Emilią i Benedyktem. Okazuje się, że Różyc przysyła ich, aby prosili w jego imieniu o rękę dziewczyny. W tym gronie Justyna oznajmia, że jest już zaręczona z Jankiem i odrzuca propozycję Różyca. Dla Emilii i Zygmunta jest to wstrząs, ale Benedykt i Kirłowa - widząc niezłomność postanowienia - popierają decyzję Justyny. Popiera ją też Witold, ciesząc się równocześnie z jej wyboru. Stary Orzelski początkowo jest wzburzony, ale Benedykt zapewnia go, że będzie mógł nadal żyć w ukochanym, spokojnym Korczynie. Marta początkowo pragnie przenieść się razem z Justyną, ale Benedykt nie chce jej puścić, gdyż - jak twierdzi - od samego początku jest mu ona niezastąpioną pomocą w gospodarstwie i jedną z najukochańszych osób na świecie. Benedykt wraz z Justyną idą do chaty Anzelma, gdzie dokonuje się ostateczne - choć bez słów prawie wyrażone - pojednanie.
"""
#https://www.bryk.pl/lektury/eliza-orzeszkowa/nad-niemnem.streszczenie-szczegolowe
print(kompresja(tekst))
print()
print(dekompresja(kompresja(tekst)))