import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Step 1: Load Dataset
df = pd.read_csv("./data/Crop_recommendation.csv")

# Step 2: Feature & Target
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Model (tuned)
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=25,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Model Accuracy: {accuracy * 100:.2f}%\n")
# print("📊 Classification Report:")
# print(classification_report(y_test, y_pred))

# Step 6: Save Model
os.makedirs("models", exist_ok=True)
with open("models/crop_recommendation.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved to 'models/crop_recommendation.pkl'")
