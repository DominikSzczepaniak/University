package gra;

import java.io.*;

public class gra implements Serializable {
    public short[][] plansza = new short[7][7];
    Para[] kierunki = {new Para(-1, 0), new Para(1, 0), new Para(0, 1), new Para(0, -1)};
    int pionki = 32;

    public int getPionki() {
        return pionki;
    }

    public gra(boolean europejska){

        for(int i = 0; i<7; i++){
            for(int j = 0; j<7; j++){
                plansza[i][j] = 1;
            }
        }
        plansza[3][3] = 0;
        for(int i = 0; i<2; i++){
            for(int j = 0; j<2; j++){
                plansza[i][j] = -5;
                plansza[6-i][j] = -5;
                plansza[i][6-j] = -5;
                plansza[6-i][6-j] = -5; //rogi planszy chcemy na -5
            }
        }
        if(europejska){
            pionki += 4;
            plansza[1][1] = plansza[1][5] = plansza[5][1] = plansza[5][5] = 1;
        }
    }
    public boolean dozwolonePrzesuniecie(Para STo){
        if(STo.getSecond() < 0 || STo.getSecond() > 6 || STo.getFirst() < 0 || STo.getFirst() > 6){
            return false;
        }
        if(plansza[STo.getFirst()][STo.getSecond()] == -5){
            return false;
        }
        return true;
    }
    public boolean dozwolonyRuch(Para SFrom, Para STo){
        if(STo.getSecond() < 0 || STo.getSecond() > 6 || STo.getFirst() < 0 || STo.getFirst() > 6){
            return false;
        }
        if(plansza[STo.getFirst()][STo.getSecond()] != 0){
            return false;
        }
        if(Math.abs(SFrom.getFirst()-STo.getFirst()) == 2 && SFrom.getSecond() == STo.getSecond()){ //pomiedzy musi byc jeszcze jakis pionek
            if(STo.getFirst() > SFrom.getFirst() && plansza[SFrom.getFirst()+1][SFrom.getSecond()] == 1){
                return true;
            }
            return STo.getFirst() < SFrom.getFirst() && plansza[SFrom.getFirst() - 1][SFrom.getSecond()] == 1;
        }
        if(Math.abs(SFrom.getSecond()-STo.getSecond()) == 2 && SFrom.getFirst()==STo.getFirst()){
            if(SFrom.getSecond() > STo.getSecond() && plansza[SFrom.getFirst()][SFrom.getSecond()-1] == 1){
                return true;
            }
            return SFrom.getSecond() < STo.getSecond() && plansza[SFrom.getFirst()][SFrom.getSecond() + 1] == 1;
        }
        return false;
    }

    public int koniecGry(){
        if(pionki == 1 && plansza[3][3] == 1){
            return 1; //wygrana
        }
        for(int i = 0; i<7; i++){
            for(int j = 0; j<7; j++){
                if(plansza[i][j] == 1){
                    for(Para p : kierunki){
                        if(i+p.getFirst() >= 0 && i+p.getFirst() < 7 && j+p.getSecond() >= 0 && j+p.getSecond() < 7 && plansza[i+p.getFirst()][j+p.getSecond()] == 1 && dozwolonyRuch(new Para(i,j),new Para(i+p.getFirst()*2,j+p.getSecond()*2))){
                            return 0; //w trakcie
                        }
                    }
                }
            }
        }
        return 2; //przegrana
    }
    public void wykonajRuch(int yFrom, int xFrom, int yTo, int xTo){
        if(!dozwolonyRuch(new Para(yFrom,xFrom), new Para(yTo,xTo))){
            return;
        }
        plansza[yFrom][xFrom] = 0;
        plansza[yTo][xTo] = 1;
        if(xTo != xFrom){
            if(xTo > xFrom){
                plansza[yFrom][xFrom+1] = 0;
            }
            else{
                plansza[yFrom][xFrom-1] = 0;
            }
        }
        else{
            if(yTo > yFrom){
                plansza[yFrom+1][xFrom] = 0;
            }
            else{
                plansza[yFrom-1][xFrom] = 0;
            }
        }
        pionki--;
    }

    public void zapiszStanGry() {
        try (ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream("solitaire.ser"))) {
            outputStream.writeObject(this);
        } catch (IOException e) {

        }
    }

    public static gra wczytajStanGry() {
        try (ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream("solitaire.ser"))) {
            gra wczytanaGra = (gra) inputStream.readObject();
            File plik = new File("solitaire.ser");
            if (plik.exists()) {
                plik.delete();
            }
            return wczytanaGra;
        } catch (IOException | ClassNotFoundException e) {
            return null;
        }
    }

}
