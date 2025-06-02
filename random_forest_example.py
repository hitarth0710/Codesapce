from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# 1. Generate synthetic data
# Creates a dataset with 1000 samples, 20 features (informative + redundant + repeated),
# and 2 classes for classification.
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                           n_redundant=5, n_classes=2, random_state=42)

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize the Random Forest Classifier
# n_estimators=100 specifies that the forest should contain 100 decision trees.
# random_state ensures reproducibility.
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1) # n_jobs=-1 uses all available CPU cores

# 4. Train the model
print("Training the Random Forest model with 100 trees...")
rf_classifier.fit(X_train, y_train)
print("Training complete.")

# 5. Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# 6. Evaluate the model (optional)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on the test set: {accuracy:.4f}")

# You can access individual trees if needed, though it's less common:
# individual_tree = rf_classifier.estimators_[0]
# print(f"\nDetails of the first tree:\n{individual_tree}")
