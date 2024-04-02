import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;

import static org.junit.jupiter.api.Assertions.*;

class BetterReusableTest{
    private ObjectPool pool;
    @BeforeEach
    void setUp(){
        pool = new ObjectPool(1);
    }

    @Test
    void doWorkValidUse(){
        BetterReusable betterReusable = new BetterReusable(pool);
        assertDoesNotThrow(betterReusable::DoWork);
    }

    @Test
    void doWorkAfterReleaseThrowsException() {
        BetterReusable betterReusable = new BetterReusable(pool);
        betterReusable.Release(pool);
        assertThrows(IllegalStateException.class, betterReusable::DoWork);
    }

    @Test
    void acquireAfterRelease() {
        BetterReusable firstInstance = new BetterReusable(pool);
        firstInstance.Release(pool);
        BetterReusable secondInstance = new BetterReusable(pool);
        assertDoesNotThrow(secondInstance::DoWork);
    }

    @Test
    void releaseWithoutAcquireThrowsNoException() {
        BetterReusable betterReusable = new BetterReusable(pool);
        assertDoesNotThrow(() -> betterReusable.Release(pool));
    }

    @Test
    void multipleReleasesOnlyFirstHasEffect() {
        BetterReusable betterReusable = new BetterReusable(pool);
        betterReusable.Release(pool);
        assertThrows(IllegalStateException.class, betterReusable::DoWork, "First release should make this object unusable");
        assertDoesNotThrow(() -> betterReusable.Release(pool), "Subsequent releases should not throw exception");
    }

    @Test
    public void invalidSize() {
        IllegalArgumentException thrown = assertThrows(IllegalArgumentException.class, () -> {
            var pool = new ObjectPool(0);
        });
        assertTrue(thrown.getMessage().contains("Rozmiar puli musi być większy od 0."));
    }

    @Test
    void capacityDepleted(){
        BetterReusable betterReusable1 = new BetterReusable(pool);
        assertThrows(IllegalArgumentException.class, () -> {
            BetterReusable betterReusable2 = new BetterReusable(pool);
        });
    }

    @Test
    public void reusedInstance() { //nie wiem jak
//        BetterReusable betterReusable = new BetterReusable(pool);
//        betterReusable.Release(pool);
        //TODO dodac hash, a pozniej porownac hashe
//        BetterReusable betterReusable2 = new BetterReusable(pool);
//        assertEquals(betterReusable2, betterReusable);
    }

}

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}