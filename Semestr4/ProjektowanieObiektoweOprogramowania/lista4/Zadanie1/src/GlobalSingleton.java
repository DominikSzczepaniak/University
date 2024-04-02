public class GlobalSingleton {
    private static GlobalSingleton instance;

    private GlobalSingleton() {}

    public static synchronized GlobalSingleton getInstance() {
        if (instance == null) {
            instance = new GlobalSingleton();
        }
        return instance;
    }
}
