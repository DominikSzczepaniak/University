package W9;

import javax.swing.*;
import java.awt.*;

public class DayUI extends JPanel {
    JLabel number;
    JLabel name;

    String week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

    public DayUI(int weekDay) {
        super();

        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        this.setBorder(BorderFactory.createLineBorder(Color.BLACK));

        if (weekDay == 6)
            this.setBackground(Color.PINK);

        number = new JLabel("#");
        number.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 20));
        number.setAlignmentX(Component.CENTER_ALIGNMENT);


        name = new JLabel(week[weekDay]);
        name.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 10));
        name.setAlignmentX(Component.CENTER_ALIGNMENT);

        this.add(number);
        this.add(name);
    }

    public void setNumber(int number) {
        this.number.setText("" + number);
    }
}
