import javax.swing.*;
import java.awt.*;

public class DataController {
    private DataModel model;
    private DataView view;

    public DataController(DataModel model, DataView view) {
        this.model = model;
        this.view = view;
    }

    public void setYear(int year){
        model.setYear(year);
    }

    public void setMonth(int month){
        model.setMonth(month);
    }

    public int getMonth(){
        return model.getMonth();
    }

    public int getYear(){
        return model.getYear();
    }

    public Component getView(){
        JList<String> dateList = new JList<>(model);
//        var test = view.getListCellRendererComponent(dateList, model.getElementAt(0),0, true, true );
        dateList.setCellRenderer(view);
        return dateList;
    }

    public JPanel getMonthTable(){
        return view.getMonthTable();
    }

    public void decreaseMonth(){
        model.decreaseMonth();
    }

    public void increaseMonth(){
        model.increaseMonth();
    }


}
