from biscuit_classifier import classify_biscuit
from dunk_predictor import DunkPredictor
from robot_arm import dunk_biscuit

def main():
    print("🫖 Welcome to DunkNet: Biscuit Crumble Predictor")

    image_path = input("📷 Enter biscuit image path (just type anything for now): ")
    tea_temp = float(input("🌡️ Enter tea temperature (°C): "))

    biscuit_type = classify_biscuit(image_path)
    print(f"🔍 Detected biscuit type: {biscuit_type}")

    predictor = DunkPredictor()
    mct = predictor.predict(biscuit_type, tea_temp)
    print(f"🧠 Predicted Max Crumble Time: {mct:.2f} seconds")

    dunk_biscuit(mct)

if __name__ == "__main__":
    main()
