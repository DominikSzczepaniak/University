package lista9.lista9;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import lista9.lista9.logika.Gra;
import lista9.lista9.logika.MikolajZnalezionyListener;
import lista9.lista9.obiekty.Para;
import lista9.lista9.obiekty.Prezent;

import java.util.Optional;
import java.util.Timer;
import java.util.TimerTask;

public class App extends Application implements MikolajZnalezionyListener {
    int N = 15;
    int M = 15;
    Timer timer;
    Gra gra;
    @FXML
    GridPane gridPane;

    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        gridPane = loader.load();
        gra = new Gra(N, M);
        gra.planszaGry.setMikolajZnalezionyListener(this);
        rysujPlansze();
        Scene scene = getScene();
//        Thread timerThread = new Thread(() -> {
//            timer = new Timer(true);
//            TimerTask timerTask = new TimerTask() {
//                @Override
//                public void run() {
//                    if(gra.planszaGry.koniecGry()){
//                        zakonczGre("WYGRAŁEŚ");
//                    }
//                    Thread rysujThread = new Thread(() -> rysujPlansze());
//                    rysujThread.start();
//                    for(var dziecko : gra.planszaGry.dzieci){
//                        Thread dzieckoThread = new Thread(() -> gra.planszaGry.dzieckoUpdate(dziecko));
//                        dzieckoThread.start();
//                    }
//                    Thread mikolajThread = new Thread(() -> gra.planszaGry.mikolajUpdate(gra.planszaGry.mikolaj));
//                    mikolajThread.start();
//                }
//            };
//            timer.scheduleAtFixedRate(timerTask, 0, 400);
//        });
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();
//        try{
//            Thread.sleep(5000);
//        }catch(InterruptedException ignored){}
//        timerThread.start();
        stage.show();
    }

    private Scene getScene() {
        Scene scene = new Scene(gridPane, 320, 240);
        scene.setOnKeyPressed(keyEvent -> {
            switch(keyEvent.getCode()){
                case UP:
                    gra.planszaGry.ruchMikolaja(new Para(1, 0));
                    gra.planszaGry.mikolaj.kierunekStrzalki = 0;
                    break;
                case DOWN:
                    gra.planszaGry.ruchMikolaja(new Para(-1, 0));
                    gra.planszaGry.mikolaj.kierunekStrzalki = 2;
                    break;
                case LEFT:
                    gra.planszaGry.ruchMikolaja(new Para(0, -1));
                    gra.planszaGry.mikolaj.kierunekStrzalki = 3;
                    break;
                case RIGHT:
                    gra.planszaGry.ruchMikolaja(new Para(0, 1));
                    gra.planszaGry.mikolaj.kierunekStrzalki = 1;
                    break;
                case SPACE:
                    gra.planszaGry.mikolajPolozylPrezent();
                    break;
            }
        });
        return scene;
    }

    void rysujPlansze(){
        gridPane = new GridPane();
        for(int i = 0; i<N; i++){
            for(int j = 0; j<M; j++){
                Color kolor;
                if(gra.planszaGry.plansza[i][j] instanceof Prezent){
                    kolor = Color.CYAN;
                }
                else{
                    kolor = Color.WHITE;
                }
                Rectangle pole = new Rectangle(40, 40, kolor);
                gridPane.add(pole, i, j);
            }
        }
        for(var dziecko : gra.planszaGry.dzieci){
            int y = dziecko.getPos().getFirst();
            int x = dziecko.getPos().getSecond();
            Circle poleDziecko = new Circle(20, Color.YELLOW);
            gridPane.add(poleDziecko, y, x);
        }
        Circle poleMikolaj = new Circle(20, Color.RED);
        gridPane.add(poleMikolaj, gra.planszaGry.mikolaj.getPos().getFirst(), gra.planszaGry.mikolaj.getPos().getSecond());
    }

    @Override
    public void znalezionoMikolaja() {
        zakonczGre("PRZEGRAŁEŚ");
    }

    public void zakonczGre(String komunikat){
        Platform.runLater(() ->{
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Koniec gry");
            alert.setHeaderText(null);
            alert.setContentText(komunikat);
            alert.setOnHidden(event -> {
                timer.cancel();
                Platform.exit();
                System.exit(0);
            });

            Optional<ButtonType> result = alert.showAndWait();
            if (result.isPresent() && result.get() == ButtonType.OK) {
                timer.cancel();
                Platform.exit();
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        launch();
    }
}