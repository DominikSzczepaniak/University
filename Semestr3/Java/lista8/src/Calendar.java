//import javax.swing.*;
//import javax.swing.event.ChangeEvent;
//import javax.swing.event.ChangeListener;
//import javax.swing.event.ListSelectionEvent;
//import javax.swing.event.ListSelectionListener;
//import javax.xml.crypto.Data;
//import java.awt.*;
//import java.awt.event.ActionEvent;
//import java.awt.event.AdjustmentEvent;
//import java.awt.event.AdjustmentListener;
//
//public class Calendar extends JFrame{
//    JTabbedPane central;
//    private JToolBar toolBar;
//    private JSpinner yearSpinner;
//    private JScrollBar monthScrollBar;
//    DataController controller;
//
//
//    public Calendar(){
//        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        setSize(800, 600);
//        DataModel a = new DataModel();
//        controller = new DataController(a, new DataView(a));
//        central = new JTabbedPane();
//
//        toolBar = new JToolBar();
//        yearSpinner = new JSpinner(new SpinnerNumberModel(controller.getYear(), 1, Integer.MAX_VALUE, 1));
//        monthScrollBar = new JScrollBar(Adjustable.HORIZONTAL, controller.getMonth() + 1, 1, 1, 13);
//
//        yearTab();
//        monthTab();
//        navigationMenu();
//
//        add(central);
////        add(navigation);
//        setSize(1400, 800);
//        setVisible(true);
//    }
//
//    private void monthTab(){
//        JScrollPane previous, current, next;
//        var dataModel2 = new DataModel(controller.getYear(), controller.getMonth());
//        var dataModel3 = new DataModel(controller.getYear(), controller.getMonth());
//        dataModel2.decreaseMonth();
//        dataModel3.increaseMonth();
//        var controller2 = new DataController(dataModel2, new DataView(dataModel2));
//        var controller3 = new DataController(dataModel3,new DataView(dataModel3));
//        current = new JScrollPane(controller.getView());
//        previous = new JScrollPane(controller2.getView());
//        next = new JScrollPane(controller3.getView());
//
//
//        previous.setSize(previous.getWidth(), previous.getHeight()*3);
//        next.setSize(next.getWidth(), next.getHeight()*3);
//        current.setSize(current.getWidth(), current.getHeight()*3);
//        //javy to nie obchodzi i guess? spoko rozumiem, po co sie sluchac, te linijki wstawilem dla beki xD
//
//        JPanel monthMenu = new JPanel();
//        monthMenu.add(previous);
//        monthMenu.add(current);
//        monthMenu.add(next);
//
//        central.add("Month", monthMenu);
//    }
//
//    private void yearTab(){
//        JPanel panel = new JPanel();
//        DataModel[] models = new DataModel[12];
//        DataController[] controllers = new DataController[12];
//        GridLayout gridCalendar = new GridLayout(3, 4);
//        panel.setLayout(gridCalendar);
//        for(int i = 1; i<=12; i++){
//            models[i-1] = new DataModel(2023, i); //TODO: YEAR TO CHANGE TO VALUE FROM JBUTTON, JSPINNER ETC.
//            controllers[i-1] = new DataController(models[i-1], new DataView(models[i-1]));
//            panel.add(controllers[i-1].getMonthTable());
//        }
//        central.add("Year", panel);
//    }
//
//    private void navigationMenu(){
//        toolBar.add(new JButton(new Calendar.PreviousMonthAction()));
//        toolBar.add(new JLabel("Year:"));
//        toolBar.add(yearSpinner);
//        toolBar.add(new JLabel("Month:"));
//        toolBar.add(monthScrollBar);
//        toolBar.add(new JButton(new Calendar.NextMonthAction()));
//        toolBar.setFloatable(false);
//
//        // Add listeners to components
//        yearSpinner.addChangeListener(new Calendar.YearChangeListener());
//        monthScrollBar.addAdjustmentListener(new Calendar.MonthScrollBarListener());
//
//
//        //JButton, JSpinner, JScrollBar -  nawigacja po latach i miesiacach
//        //za kazdym razem odpalaj fireContentsChange() po zmianie
//        //Pamiętaj, że przechodząc z grudnia do stycznia lub ze stycznia do grudnia przy zmianie miesiąca na
//        //następny lub poprzedni, powinieneś zmienić rok. Zadbaj też o poprawne wyświetlenie dni w
//        //październiku 1582 roku: po czwartku 4 października następował piątek 15 października.
//
//    }
//
////    private class MonthSelectionListener implements ListSelectionListener {
////        @Override
////        public void valueChanged(ListSelectionEvent e) {
////            if (!e.getValueIsAdjusting()) {
////                controller.setMonth(monthList.getSelectedIndex());
////                updateDayList(currentYear, currentMonth);
////            }
////        }
////    }
////
////    private class YearChangeListener implements ChangeListener {
////        @Override
////        public void stateChanged(ChangeEvent e) {
////            currentYear = (int) yearSpinner.getValue();
////            updateCalendar();
////        }
////    }
////
////    private class MonthScrollBarListener implements AdjustmentListener {
////        @Override
////        public void adjustmentValueChanged(AdjustmentEvent e) {
////            currentMonth = monthScrollBar.getValue() - 1;
////            updateDayList(currentYear, currentMonth);
////        }
////    }
//
//    private class PreviousMonthAction extends AbstractAction {
//        public PreviousMonthAction() {
//            super("Previous Month");
//        }
//
//        @Override
//        public void actionPerformed(ActionEvent e) {
//            controller.decreaseMonth();
//        }
//    }
//
//    private class NextMonthAction extends AbstractAction {
//        public NextMonthAction() {
//            super("Next Month");
//        }
//
//        @Override
//        public void actionPerformed(ActionEvent e) {
//            controller.increaseMonth();
//        }
//    }
//
//
//
//    public static void main(String[] args){
//        SwingUtilities.invokeLater(Calendar::new);
//    }
//}
