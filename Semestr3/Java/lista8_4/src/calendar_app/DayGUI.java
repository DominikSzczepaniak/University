package calendar_app;

import javax.swing.*;
import java.awt.*;

public class DayGUI extends JPanel {
    JLabel number;
    public DayGUI(int weekDay) {
        super();

        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        if (weekDay == 6)
            this.setBackground(Color.RED);

        number = new JLabel("#");
        number.setAlignmentX(Component.CENTER_ALIGNMENT);

        this.add(number);
    }

    public void setNumber(int number) {
        this.number.setText("" + number);
    }
}
