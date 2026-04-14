import joblib

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(path="iris_model.joblib"):
    return joblib.load(path)


def predict(model, data):
    prediction = model.predict([data])[0]
    return str(CLASS_NAMES[prediction])


if __name__ == "__main__":
    m = load_model()
    sample_data = [5.1, 3.5, 1.4, 0.2]
    result = predict(m, sample_data)
    print(f"Result: {result}")
