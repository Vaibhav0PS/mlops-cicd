from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def train_model() -> float:
    """Return accuracy measured on a fixed stratified Iris holdout."""
    iris = load_iris()
    train_x, test_x, train_y, test_y = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    classifier = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
    classifier.fit(train_x, train_y)
    return float(accuracy_score(test_y, classifier.predict(test_x)))
