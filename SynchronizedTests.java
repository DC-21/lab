public class SynchronizedTests {
    private int sharedCounter = 0;
    public synchronized void synchronizedMethod() {
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getName() + " - Counter: " + sharedCounter++);
        }
    }
    public static void main(String[] args) {
        SynchronizedTests synchronizedTests = new SynchronizedTests();
        Thread thread1 = new Thread(() -> synchronizedTests.synchronizedMethod());
        Thread thread2 = new Thread(() -> synchronizedTests.synchronizedMethod());
        thread1.start();
        thread2.start();
    }
}
