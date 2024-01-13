module lista9.lista9 {
    requires javafx.controls;
    requires javafx.fxml;


    opens lista9.lista9.wyglad to javafx.fxml;
    exports lista9.lista9.wyglad;
}