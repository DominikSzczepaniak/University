package struktury;

public class Para implements Cloneable, Comparable<Para>{
    public final String klucz;
    private double wartosc;
    public Para(String klucz, double wartosc){
        if(klucz == null || klucz.isEmpty()){
            throw new IllegalArgumentException("Klucz musi byc niepustym napisem");
        }
        this.klucz = klucz;
        this.wartosc = wartosc;
    }

    public double getWartosc() {
        return wartosc;
    }

    public void setWartosc(double wartosc) {
        this.wartosc = wartosc;
    }

    public String getKlucz() {
        return klucz;
    }

    @Override
    public String toString() {
        return "[" + klucz + "] = " + wartosc;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Para)) return false;
        Para p = (Para) obj;
        return this.getKlucz().equals(p.getKlucz());
    }

    @Override
    public Para clone(){
        try {
            return (Para) super.clone();
        }catch(CloneNotSupportedException e){
            return null;
        }
    }
    @Override
    public int compareTo(Para p){
        return this.getKlucz().compareTo(p.getKlucz());
    }
}
