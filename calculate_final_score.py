import csv
from pathlib import Path

from mri.mri import detect_mri
from memory.memgem import memory_game_accuracy
from coordgame.performance_times import get_latest_performance_time, get_average_time
from parkinson.realspeech import predict_parkinsons

weights = {
    "mri": 0.30,
    "memory": 0.25,
    "coordination": 0.20,
    "speech": 0.25
}

def normalize_classification(result, positive_class="Demented"):
    return 1 if result == positive_class else 0

def normalize_accuracy(accuracy):
    return accuracy / 100

def main():
    mri_result = detect_mri()
    mri_score = normalize_classification(mri_result) * weights["mri"]

    memory_accuracy = memory_game_accuracy()
    memory_score = normalize_accuracy(memory_accuracy) * weights["memory"]

    coordination_time = get_latest_performance_time()
    avg_coordination_time = get_average_time()
    if avg_coordination_time > 0:
        coordination_accuracy = (avg_coordination_time - coordination_time) / avg_coordination_time * 100
        coordination_score = normalize_accuracy(coordination_accuracy) * weights["coordination"]
    else:
        coordination_score = 0

    speech_result = predict_parkinsons()
    speech_score = normalize_classification(speech_result) * weights["speech"]

    total_score = mri_score + memory_score + coordination_score + speech_score
    print(f"Total Score: {total_score:.2f}")

    if total_score > 0.7:
        concern_level = "Flag for further clinical diagnosis."
    else:
        concern_level = "No immediate concern."

    print(concern_level)

    data_to_save = {
        "MRI Score": mri_score,
        "Memory Score": memory_score,
        "Coordination Score": coordination_score,
        "Speech Score": speech_score,
        "Total Score": total_score,
        "Concern Level": concern_level
    }

    csv_file_path = Path("finalresult.csv")

    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_to_save.keys())
        writer.writeheader()
        writer.writerow(data_to_save)

if __name__ == "__main__":
    main()
