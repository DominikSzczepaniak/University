package struktury;

public class ZbiorTablicowy implements Zbior, Cloneable{
    private Para[] zbior;
    private int zapelnienie;
    public ZbiorTablicowy(int rozmiar){
        zbior = new Para[rozmiar];
        zapelnienie = 0;
    }
    @Override
    public Para szukaj(String k) {
        for(int i = 0; i<zapelnienie; i++){
            if(zbior[i].getKlucz().equals(k)){
                return zbior[i];
            }
        }
        return null;
    }

    @Override
    public void wstaw(Para p) {
        if(zapelnienie >= zbior.length){
            throw new IllegalStateException("Tablica calkowicie zapelniona");
        }
        zbior[zapelnienie++] = p;
    }

    @Override
    public void usuń(String k) {
        int miejsce = 0;
        for(int i = 0; i<zapelnienie; i++){
            if(zbior[i].getKlucz().equals(k)){
                for(int j = 0; i+j+1<zapelnienie; j++){
                    zbior[i+j] = zbior[i+j+1];
                }
                zapelnienie--;
                break;
            }
        }

    }

    @Override
    public void czysc() {
        for(int i = 0; i<zapelnienie; i++){
            zbior[i] = null;
        }
        zapelnienie = 0;
    }

    @Override
    public int ile() {
        return zapelnienie;
    }

    @Override
    public ZbiorTablicowy clone(){
        try{
            return (ZbiorTablicowy) super.clone();
        }catch(CloneNotSupportedException e){
            return null;
        }
    }

    @Override
    public String toString() {
        String out = "";
        for(int i = 0; i<zapelnienie; i++){
            out += zbior[i] + " ";
        }
        return out;
    }
}
