import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.AdjustmentEvent;
import java.awt.event.AdjustmentListener;
import java.text.DateFormatSymbols;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class CalendarApp extends JFrame {

    private JTabbedPane tabbedPane;
    private JList<String> monthList;
    private JList<String> dayList;
    private DefaultListModel<String> monthListModel;
    private DefaultListModel<String> dayListModel;
    private JToolBar toolBar;
    private JSpinner yearSpinner;
    private JScrollBar monthScrollBar;

    private int currentYear;
    private int currentMonth;
    private int currentDay;

    public CalendarApp() {
        setTitle("Universal Calendar");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1000, 800);

        Calendar currentDate = new GregorianCalendar();
        currentYear = currentDate.get(Calendar.YEAR);
        currentMonth = currentDate.get(Calendar.MONTH);
        currentDay = currentDate.get(Calendar.DAY_OF_MONTH);

        tabbedPane = new JTabbedPane();
        monthList = new JList<>();
        dayList = new JList<>();
        monthListModel = new DefaultListModel<>();
        dayListModel = new DefaultListModel<>();
        toolBar = new JToolBar();
        yearSpinner = new JSpinner(new SpinnerNumberModel(currentYear, 1, Integer.MAX_VALUE, 1));
        monthScrollBar = new JScrollBar(Adjustable.HORIZONTAL, currentMonth + 1, 1, 1, 13);

        setupMonthTab();
        setupDayTab();
        setupToolBar();

        add(tabbedPane, BorderLayout.CENTER);
        add(toolBar, BorderLayout.SOUTH);

        // Set the initial state of the calendar
        updateCalendar();

        // Show the frame
        setVisible(true);
    }

    private void setupMonthTab() {
        // Set up the month tab
        JPanel monthPanel = new JPanel(new BorderLayout());
        monthList.setModel(monthListModel);
        monthList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        monthList.addListSelectionListener(new MonthSelectionListener());
        JScrollPane monthScrollPane = new JScrollPane(monthList);
        monthPanel.add(monthScrollPane, BorderLayout.CENTER);
        tabbedPane.addTab("Month", monthPanel);
    }

    private void setupDayTab() {
        // Set up the day tab
        JPanel dayPanel = new JPanel(new BorderLayout());
        dayList.setModel(dayListModel);
        dayList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        JScrollPane dayScrollPane = new JScrollPane(dayList);
        dayPanel.add(dayScrollPane, BorderLayout.CENTER);
        tabbedPane.addTab("Day", dayPanel);
    }

    private void setupToolBar() {
        // Set up the toolbar
        toolBar.add(new JButton(new PreviousMonthAction()));
        toolBar.add(new JLabel("Year:"));
        toolBar.add(yearSpinner);
        toolBar.add(new JLabel("Month:"));
        toolBar.add(monthScrollBar);
        toolBar.add(new JButton(new NextMonthAction()));
        toolBar.setFloatable(false);

        // Add listeners to components
        yearSpinner.addChangeListener(new YearChangeListener());
        monthScrollBar.addAdjustmentListener(new MonthScrollBarListener());
    }

    private void updateCalendar() {
        updateMonthList();
        updateDayList(currentYear, currentMonth);
    }

    private void updateMonthList() {
        monthListModel.clear();
        DateFormatSymbols dfs = new DateFormatSymbols();
        String[] monthNames = dfs.getMonths();
        for (int i = 0; i < monthNames.length - 1; i++) {
            monthListModel.addElement(monthNames[i]);
        }
        monthList.setSelectedIndex(currentMonth);
    }

    private void updateDayList(int year, int month) {
        dayListModel.clear();
        Calendar calendar = new GregorianCalendar(year, month, 1);
        int daysInMonth = calendar.getActualMaximum(Calendar.DAY_OF_MONTH);
        for (int day = 1; day <= daysInMonth; day++) {
            calendar.set(year, month, day);
            String dayOfWeek = new DateFormatSymbols().getShortWeekdays()[calendar.get(Calendar.DAY_OF_WEEK)];
            String dayString = dayOfWeek + " " + day;
            if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                dayString = "<html><font color='red'>" + dayString + "</font></html>";
            }
            dayListModel.addElement(dayString);
        }
        dayList.setSelectedIndex(currentDay - 1);
    }

    private class MonthSelectionListener implements ListSelectionListener {
        @Override
        public void valueChanged(ListSelectionEvent e) {
            if (!e.getValueIsAdjusting()) {
                currentMonth = monthList.getSelectedIndex();
                updateDayList(currentYear, currentMonth);
            }
        }
    }

    private class YearChangeListener implements ChangeListener {
        @Override
        public void stateChanged(ChangeEvent e) {
            currentYear = (int) yearSpinner.getValue();
            updateCalendar();
        }
    }

    private class MonthScrollBarListener implements AdjustmentListener {
        @Override
        public void adjustmentValueChanged(AdjustmentEvent e) {
            currentMonth = monthScrollBar.getValue() - 1;
            updateDayList(currentYear, currentMonth);
        }
    }

    private class PreviousMonthAction extends AbstractAction {
        public PreviousMonthAction() {
            super("Previous Month");
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (currentMonth == 0) {
                currentMonth = 11;
                currentYear--;
            } else {
                currentMonth--;
            }
            updateCalendar();
        }
    }

    private class NextMonthAction extends AbstractAction {
        public NextMonthAction() {
            super("Next Month");
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (currentMonth == 11) {
                currentMonth = 0;
                currentYear++;
            } else {
                currentMonth++;
            }
            updateCalendar();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CalendarApp::new);
    }
}
