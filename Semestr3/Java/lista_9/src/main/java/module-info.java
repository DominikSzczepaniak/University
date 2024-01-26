module org.example.lista_ {
    requires javafx.controls;
    requires javafx.fxml;


    opens lista9.lista9 to javafx.fxml;
    exports lista9.lista9;
}