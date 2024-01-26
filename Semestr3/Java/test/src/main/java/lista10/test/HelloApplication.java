package lista10.test;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        System.out.println("javafx.runtime.version: " + System.getProperty("javafx.runtime.version"));
        System.exit(0);
    }

    public static void main(String[] args) {

        launch();
    }
}