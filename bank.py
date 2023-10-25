def update_and_count_locations(patients):
    location_count = {
        "Home": 0,
        "Hospital A": 0,
        "Hospital B": 0,
        "Hospital C": 0
    }

    for patient in patients:
        priest_probability = patients[patient]["PRIEST"]

        if priest_probability < 10:
            patients[patient]["hospital"] = "Home"
            patients[patient]["address"] = "Home"

        location = patients[patient]["hospital"]
        location_count[location] += 1

    return location_count

# Example usage:
patients = {
    "Patient1": {
        "hospital": "Hospital A",
        "address": "123 Main St",
        "PRIEST": 8.5
    },
    "Patient2": {
        "hospital": "Hospital B",
        "address": "456 Elm St",
        "PRIEST": 12.0
    },
    # Add more patients here
}

location_counts = update_and_count_locations(patients)
print(location_counts)
