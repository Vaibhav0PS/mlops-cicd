from src.model import train_model


def main() -> None:
    print(f"Model Accuracy: {train_model():.4f}")


if __name__ == "__main__":
    main()
