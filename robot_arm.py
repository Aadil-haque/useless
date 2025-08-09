import time

def dunk_biscuit(predicted_mct):
    wait_time = predicted_mct + 2  # Intentionally too long
    print(f"[Robot Arm] Dunking for {wait_time:.2f} seconds (MCT: {predicted_mct:.2f})...")
    time.sleep(1)  # Simulate time delay
    print("[Robot Arm] Lifted... oh no, it crumbled! 😭")
