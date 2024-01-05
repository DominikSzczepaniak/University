package calendar_app;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;

public class MonthGUI extends JPanel {
    GUI gui;
    JLabel name;
    JPanel dayTable;
    Date date;

    public MonthGUI(GregorianCalendar calendar, GUI parent) {
        super();
        this.gui = parent;
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        this.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        this.setBackground(Color.GREEN);
        date = calendar.getTime();

        name = new JLabel(new SimpleDateFormat("MMMM", Locale.ENGLISH).format(calendar.getTime()));
        name.setAlignmentX(Component.CENTER_ALIGNMENT);

        String week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
        JPanel weekPanel = new JPanel(new GridLayout(1, 7, 2, 2));
        for(var i : week){
            weekPanel.add(new JLabel(i));
        }


        dayTable = new JPanel(new GridLayout(6, 7, 2, 2));

        for (int i = 0; i < 6 * 7; i++) {
            DayGUI day = new DayGUI(i % 7);
            dayTable.add(day);
        }

        updateMonthUI(calendar);

        this.add(name);
        this.add(weekPanel);
        this.add(dayTable);

        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                calendar.set(Calendar.MONTH, date.getMonth());
                gui.fireContentsChanged();
                gui.switchTab(1);
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                MonthGUI.this.setBackground(Color.cyan);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                MonthGUI.this.setBackground(Color.GREEN);
            }
        });
    }

    public void updateMonthUI(GregorianCalendar calendar) {
        for (int i = 0; i < 6 * 7; i++)
            dayTable.getComponent(i).setVisible(false);

        Date original = calendar.getTime();

        int it = (calendar.get(Calendar.DAY_OF_WEEK) + 5) % 7;
        while (calendar.get(Calendar.MONTH) == original.getMonth()) {
            dayTable.getComponent(it).setVisible(true);
            ((DayGUI) dayTable.getComponent(it)).setNumber(calendar.get(Calendar.DAY_OF_MONTH));
            calendar.add(Calendar.DAY_OF_MONTH, 1);
            it++;
        }

        calendar.setTime(original);
    }
}
