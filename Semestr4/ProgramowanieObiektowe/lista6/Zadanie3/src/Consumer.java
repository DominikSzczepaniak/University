public class Consumer implements Runnable {
    private final Buffer<String> buffer;

    public Consumer(Buffer<String> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            while (true) {
                String message = buffer.get();
                System.out.println("Consumed: " + message);
                if (message.equals("END")) {
                    break;
                }
                Thread.sleep(1000); // symulacja czasu konsumpcji
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
