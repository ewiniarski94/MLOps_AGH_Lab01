import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    return load_iris(return_X_y=True)


def train_model(X, y):
    return LogisticRegression(max_iter=200).fit(X, y)


def save_model(model, filename="model.joblib"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    X_train, y_train = load_data()
    trained_model = train_model(X_train, y_train)

    save_model(trained_model, "iris_model.joblib")
