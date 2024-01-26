module lista10.demo {
    requires javafx.controls;
    requires javafx.fxml;


    opens lista10.demo to javafx.fxml;
    exports lista10.demo;
}