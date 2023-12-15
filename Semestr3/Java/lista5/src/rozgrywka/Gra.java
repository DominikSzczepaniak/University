package rozgrywka;
import obliczenia.Wymierna;
import prezentacja.Log;

public class Gra {
    private int zakres;
    private Wymierna liczba;
    private int maksIloscProb;
    private int licznikProb = 0;
    private int statusGry = 0; //0 nieaktywna 1 aktywna 2 rezygnacja 3 porazka 4 zwyciestwo
    private Log logger = new Log();

    public void start(int nowyZakres) throws Exception{
        if(nowyZakres < 5 || nowyZakres > 20){
            throw new Exception("Zakres ma byc miedzy 5 a 20");
        }
        this.zakres = nowyZakres;
        handleStart();
    }
    public void start(){
        handleStart();
    }
    public void handleStart(){
        int licz, mian;
//        do {
            licz = (int) (Math.random() * zakres) + 1;
            mian = (int) (Math.random() * zakres) + 1;
//        }while (licz >= mian);
        liczba = new Wymierna(licz, mian);
        if (licz >= mian) throw new AssertionError();
        statusGry = 1;
        maksIloscProb = (int) Wymierna.log2(zakres*zakres) + 5;
        logger.logStart();

    }



    public String getStatusGry(){
        switch(statusGry){
            case 0 -> {
                return "Nieaktywna";
            }
            case 1 ->{
                return "Aktywna";
            }
            case 2 ->{
                return "Rezygnacja";
            }
            case 3 ->{
                return "Porazka";
            }
            case 4 ->{
                return "Zwyciestwo";
            }
        }
        return "";
    }

    public void zmianaZakresu(int nowyZakres) throws Exception{
        if(this.getStatusGry() == "Nieaktywna"){
            if(nowyZakres < 5 || nowyZakres > 20){
                throw new Exception("Zakres ma byc miedzy 5 a 20");
            }
            this.zakres = nowyZakres;
        }
    }
    public String strzal(Wymierna sprawdz) throws Exception{
        logger.logStrzal();
        licznikProb += 1;
        if(getStatusGry().equals("Aktywna")){
            if(licznikProb < maksIloscProb) {
                int porownanie = sprawdz.compareTo(liczba); // -1 mniejsza 1 wieksza
                if(porownanie == 1){
                    return "Podana liczba jest za duża";
                }
                else if(porownanie == -1){
                    return "Podana liczba jest za mała";
                }
                else{
                    statusGry = 4;
                    logger.logEnd();
                    logger.logWin();
                    return "Wygrales";
                }
            }
            else{
                if(sprawdz.equals(liczba)){
                    statusGry = 4;
                    logger.logEnd();
                    logger.logWin();
                    return "Wygrales";
                }
                else{
                    statusGry = 3;
                    logger.logEnd();
                    logger.logLose();
                    return "Przegrales. Poprawna liczba to " + liczba;
                }
            }
        }
        else{
            throw new Exception("Gra nie jest aktywna");
        }
    }

    public int getMaksIloscProb() {
        return maksIloscProb;
    }

    public int getLicznikProb() {
        return licznikProb;
    }

    public void surrender(){
        statusGry = 2;
    }
}
