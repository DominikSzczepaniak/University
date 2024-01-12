package lista9.lista9.logika;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;
import javafx.util.Duration;
import lista9.lista9.HelloApplication;
import lista9.lista9.obiekty.Dziecko;
import lista9.lista9.obiekty.Mikolaj;
import lista9.lista9.obiekty.Para;
import lista9.lista9.obiekty.Plansza;

import java.io.IOException;
import java.util.Random;

public class Gra extends Application {
    private Plansza planszaGry;
    private Dziecko[] dzieci;
    private Mikolaj mikolaj;
    private final int ILOSC_DZIECI;
    public Gra(int n, int m){
        Random generator = new Random();
        ILOSC_DZIECI = generator.nextInt(7)+10;
        dzieci = new Dziecko[ILOSC_DZIECI];
        planszaGry = new Plansza(n, m);
        planszaGry.wygenerujDzieci(ILOSC_DZIECI);
        planszaGry.wygenerujMikolaja(ILOSC_DZIECI);
    }

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        scene.setOnKeyPressed(new EventHandler<KeyEvent>() {
            @Override
            public void handle(KeyEvent keyEvent) {
                switch(keyEvent.getCode()){
                    case UP:
                        planszaGry.ruchMikolaja(new Para(1, 0));
                        break;
                    case DOWN:
                        planszaGry.ruchMikolaja(new Para(-1, 0));
                        break;
                    case LEFT:
                        planszaGry.ruchMikolaja(new Para(0, -1));
                        break;
                    case RIGHT:
                        planszaGry.ruchMikolaja(new Para(0, 1));
                        break;
                    case SPACE:
                        planszaGry.mikolajPolozylPrezent();
                        break;
                }
            }
        });
        Timeline odswiezanie = new Timeline(
                new KeyFrame(Duration.seconds(0.4), new EventHandler<ActionEvent>(){
                    @Override
                    public void handle(ActionEvent event){
                        //rysujPlansze(); // osobny watek!!!!
                        //sprawdzanie w watkach dzieci

                    }
                })
        );
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();
    }
}
