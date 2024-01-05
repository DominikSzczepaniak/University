package kalendarz;

import javax.swing.*;
import java.awt.*;

public class App {
    public static void main(String[] args){
        EventQueue.invokeLater(() -> {
            MainWindow window = new MainWindow("Calendar");
            window.pack();
            window.setSize(1200, 800);
            window.setLocationRelativeTo(null);
            window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            window.setVisible(true);
        });
    }
}
