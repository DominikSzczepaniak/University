module lista10.test {
    requires javafx.controls;
    requires javafx.fxml;


    opens lista10.test to javafx.fxml;
    exports lista10.test;
}