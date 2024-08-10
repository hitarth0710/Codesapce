import java.util.Arrays;
import java.util.Random;

public class memory {
    private static final int SIZE = 100000;

    public static void main(String[] args) {
        Random rand = new Random();
        int[] arr = new int[SIZE];
        for(int i = 0; i < SIZE; i++) {
            arr[i] = rand.nextInt(10001);
        }

        long start = System.currentTimeMillis();
        Arrays.sort(arr);
        long end = System.currentTimeMillis();

        System.out.println("Time taken to sort 100 elements: " + (end - start) / 1000.0 + " seconds");
    }
}