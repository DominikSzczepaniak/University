import java.io.Serializable;

class ProduktSpozywczy extends Przedmiot implements Serializable {
    protected String terminWaznosci;
    protected int iloscBialka;
    protected int iloscWeglowodanow;

    public ProduktSpozywczy(String nazwa, int waga, double cena, String terminWaznosci, int iloscBialka, int iloscWeglowodanow) {
        super(nazwa, waga, cena);
        this.terminWaznosci = terminWaznosci;
        this.iloscBialka = iloscBialka;
        this.iloscWeglowodanow = iloscWeglowodanow;
    }

    @Override
    public String toString() {
        return super.toString() + " Termin Wazności: " + terminWaznosci + " Ilość białka: " + iloscBialka + " Ilość węglowodanów: " + iloscWeglowodanow;
    }
}