// Indirection
class User {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class UserManager { //ta klasa działa na userze zamiast bezpośrednio z maina
    public void displayUserName(User user) {
        String name = user.getName();
        System.out.println("User name: " + name);
    }
}

public class zad1c {
    public static void main(String[] args) {
        User user = new User("John");
        UserManager userManager = new UserManager();
        userManager.displayUserName(user);
    }
}