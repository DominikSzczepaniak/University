import java.text.SimpleDateFormat;
import java.util.Date;

public class Person {
    String firstName;
    String lastName;
    Date birthDate;
    String address;

    public Person(String firstName, String lastName, Date birthDate, String address) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
        this.address = address;
    }

    @Override
    public String toString() {
        return firstName + "-" + lastName;
    }

    public String getDetails() {
        SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
        return "First Name: " + firstName + "\nLast Name: " + lastName + "\nBirth Date: " + sdf.format(birthDate) + "\nAddress: " + address;
    }
}
