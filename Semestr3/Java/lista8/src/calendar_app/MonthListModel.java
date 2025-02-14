package calendar_app;

import javax.swing.*;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

public class MonthListModel extends AbstractListModel {
    int year;
    int month;

    MonthListModel() {
    }

    public void changeDate(Date date) {
        if (date == null) {
            year = 0;
        } else {
            year = date.getYear() + 1900;
            month = date.getMonth();
        }
        fireContentsChanged(this, 0, getSize() - 1);
    }

    @Override
    public int getSize() {
        if (year == 0)
            return 0;
        if (year == 1582 && month == 9)
            return 21;
        Calendar cal = Calendar.getInstance();
        cal.set(year, month, 1);
        return cal.getActualMaximum(Calendar.DAY_OF_MONTH);
    }

    @Override
    public Object getElementAt(int index) {
        Calendar cal = Calendar.getInstance();
        cal.set(year, month, 1);
        while (index-- != 0)
            cal.add(Calendar.DAY_OF_MONTH, 1);
        return "" + DateHelper.yearFormat(cal) + " " + DateHelper.dayOfMonth(cal) + " " + DateHelper.dayOfWeek(cal);
    }
}
