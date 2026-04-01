import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd

def train_model_enhanced(df):
    """Train model on enhanced balanced dataset"""
    
    features = [
        "Study_Hours",
        "Attendance",
        "Internal_Marks",
        "Assignment_Score"
    ]

    X = df[features]
    y = df["Final_Result"]

    print("Enhanced class distribution:")
    print(y.value_counts())
    print(f"Pass rate: {(y=='Pass').sum()/len(y)*100:.2f}%\n")

    # Split the data with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Train set distribution:")
    print(y_train.value_counts())
    print(f"\nTest set distribution:")
    print(y_test.value_counts())

    # Train balanced model
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=12,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        class_weight='balanced'
    )

    print("\nTraining RandomForest model on enhanced dataset...")
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{'='*70}")
    print("MODEL PERFORMANCE ON TEST SET")
    print(f"{'='*70}")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, target_names=['FAIL (0)', 'PASS (1)']))
    
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    print(f"          FAIL  PASS")
    print(f"FAIL:   [{cm[0,0]:4d} {cm[0,1]:4d}]")
    print(f"PASS:   [{cm[1,0]:4d} {cm[1,1]:4d}]")

    print("\nFeature Importance:")
    for feat, imp in zip(features, model.feature_importances_):
        print(f"  {feat:20s}: {imp:.4f}")

    return model

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"\nModel saved at: {path}")

def main():
    print("Loading enhanced dataset...")
    df = pd.read_csv("data/student_performance_enhanced.csv")
    
    # Convert Pass/Fail to numeric (if needed)
    if df['Final_Result'].dtype == 'object':
        df["Final_Result"] = df["Final_Result"].map({
            "Fail": 0,
            "Pass": 1
        })

    print("\nTraining improved model on enhanced dataset...")
    model = train_model_enhanced(df)

    print("\nSaving model...")
    save_model(model, "models/student_model.pkl")

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
