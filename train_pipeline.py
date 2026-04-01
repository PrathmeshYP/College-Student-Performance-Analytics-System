from scripts.data_cleaning import load_data, clean_data
from scripts.feature_engineering import create_features, add_risk_feature
from scripts.model_training import train_model, save_model


def main():

    print("Loading data...")
    df = load_data("data/student_performance_1000.csv")

    print("Cleaning data...")
    df = clean_data(df)

    print("Creating features...")
    df = create_features(df)

    print("Adding risk level...")
    df = add_risk_feature(df)

    print("Training model...")
    model = train_model(df)

    print("Saving model...")
    save_model(model, "models/student_model.pkl")

    print("Pipeline executed successfully!")


if __name__ == "__main__":
    main()