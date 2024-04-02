public class BetterReusable {
    private Reusable _reusable;
    private boolean isReleased = false;

    // Konstruktor
    public BetterReusable(ObjectPool objectPool) {
        _reusable = objectPool.acquireReusable();
    }

    // Metoda uwalniająca zasób
    public void Release(ObjectPool objectPool) {
        if (!isReleased) {
            objectPool.releaseReusable(_reusable);
            isReleased = true;
            _reusable = null;
        }
    }

    // Metoda delegująca operacje do Reusable
    public void DoWork() {
        if (isReleased) {
            throw new IllegalStateException("Próba użycia zwolnionego zasobu");
        }
        _reusable.DoWork();
    }
}
