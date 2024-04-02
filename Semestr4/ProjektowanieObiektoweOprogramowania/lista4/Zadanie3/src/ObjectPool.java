import java.util.ArrayList;
import java.util.List;


public class ObjectPool {
    private int poolSize;
    private List<Reusable> pool = new ArrayList<>();
    private List<Reusable> acquired = new ArrayList<>();

    public ObjectPool(int poolSize) {
        if (poolSize <= 0) {
            throw new IllegalArgumentException("Rozmiar puli musi być większy od 0.");
        }
        this.poolSize = poolSize;
    }

    public Reusable acquireReusable() {
        if (acquired.size() == this.poolSize) {
            throw new IllegalArgumentException("Osiągnięto maksymalny rozmiar puli.");
        }
        if (pool.isEmpty()) {
            Reusable reusable = new Reusable();
            pool.add(reusable);
        }
        Reusable element = pool.remove(0);
        acquired.add(element);
        return element;
    }

    public void releaseReusable(Reusable reusable) {
        if (!acquired.contains(reusable)) {
            throw new IllegalArgumentException("Próba zwolnienia obiektu, który nie został uzyskany z tej puli.");
        }
        acquired.remove(reusable);
        pool.add(reusable);
    }
}
