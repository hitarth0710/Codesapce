import smile.classification.RandomForest;
import smile.validation.metric.Accuracy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Properties;
import java.util.Random;

public class RandomForestExample {

    public static void main(String[] args) {
        // 1. Generate synthetic data
        int nSamples = 1000;
        int nFeatures = 20;
        double[][] x = new double[nSamples][nFeatures];
        int[] y = new int[nSamples];
        generateSimpleData(x, y, nSamples, nFeatures, 42); // Use seed 42

        // 2. Split data into training and testing sets
        double testSplitRatio = 0.3;
        int trainSize = (int) (nSamples * (1.0 - testSplitRatio));
        int testSize = nSamples - trainSize;

        double[][] xTrain = new double[trainSize][nFeatures];
        int[] yTrain = new int[trainSize];
        double[][] xTest = new double[testSize][nFeatures];
        int[] yTest = new int[testSize];
        splitData(x, y, xTrain, yTrain, xTest, yTest, trainSize, 42); // Use seed 42

        // 3. Initialize and Train the Random Forest Classifier
        System.out.println("Training the Random Forest model with 100 trees...");
        Properties params = new Properties();
        // Set number of trees (ntrees)
        params.setProperty("smile.random.forest.ntrees", "100");
        // You can set other parameters like mtry (number of features per node), max nodes, node size etc.
        // params.setProperty("smile.random.forest.mtry", String.valueOf((int)Math.sqrt(nFeatures)));
        // params.setProperty("smile.random.forest.max.nodes", "500");
        // params.setProperty("smile.random.forest.node.size", "5");

        // Use RandomForest.fit for training
        // Note: Smile's RandomForest constructor/fit might vary slightly between versions.
        // This example uses a common pattern. Check documentation for your specific Smile version.
        RandomForest forest = RandomForest.fit(xTrain, yTrain, params);
        System.out.println("Training complete.");

        // 4. Make predictions on the test set
        int[] yPred = new int[testSize];
        for (int i = 0; i < testSize; i++) {
            yPred[i] = forest.predict(xTest[i]);
        }

        // 5. Evaluate the model
        double accuracy = Accuracy.of(yTest, yPred);
        System.out.format("\nModel Accuracy on the test set: %.4f%n", accuracy);
    }

    /**
     * Generates simple random data for classification.
     * Assigns class 0 or 1 based on a simple threshold of the sum of the first few features.
     */
    private static void generateSimpleData(double[][] x, int[] y, int nSamples, int nFeatures, long seed) {
        Random rand = new Random(seed);
        int featuresForClassRule = Math.min(5, nFeatures); // Use first 5 features for class rule
        double threshold = featuresForClassRule * 0.5 * 10.0; // Midpoint threshold based on range [0, 10)

        for (int i = 0; i < nSamples; i++) {
            double featureSum = 0;
            for (int j = 0; j < nFeatures; j++) {
                x[i][j] = rand.nextDouble() * 10.0; // Features in range [0, 10)
                if (j < featuresForClassRule) {
                    featureSum += x[i][j];
                }
            }
            y[i] = (featureSum > threshold) ? 1 : 0; // Assign class based on threshold
        }
    }

    /**
     * Splits the data into training and testing sets after shuffling.
     */
    private static void splitData(double[][] x, int[] y, double[][] xTrain, int[] yTrain, double[][] xTest, int[] yTest, int trainSize, long seed) {
        int nSamples = x.length;
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < nSamples; i++) indices.add(i);
        Collections.shuffle(indices, new Random(seed)); // Shuffle indices for random split

        for (int i = 0; i < trainSize; i++) {
            int originalIndex = indices.get(i);
            xTrain[i] = x[originalIndex];
            yTrain[i] = y[originalIndex];
        }
        for (int i = 0; i < yTest.length; i++) {
            int originalIndex = indices.get(trainSize + i);
            xTest[i] = x[originalIndex];
            yTest[i] = y[originalIndex];
        }
    }
}
