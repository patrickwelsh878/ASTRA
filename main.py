import json

# Load in JSON telemetry file
with open("telemetry/telemetry.json", "r") as file:
    telemetry_data = json.load(file)

satellite_ids = ["HZN-001", "HZN-002", "HZN-003", "HZN-004"]
required_fields = ["temperature", "timestamp", "voltage", "position"]

# Check that the satellite is present in the telemetry data
# If it is, print that it is present, if not, print absent
# If it is present, check what fields are present for that particular satellite, print these
# If one isn't present, print that the field in question is absent
for satellite_id in satellite_ids:
    if satellite_id in telemetry_data:
        print("\n", satellite_id, "present")
        for field in required_fields:
            if field in telemetry_data[satellite_id]:
                print(satellite_id, field, "field present")
                # Check nested positioning data
                if field == "position":
                    for nested_key in ["x_km", "y_km", "z_km"]:
                        if nested_key in telemetry_data[satellite_id]["position"]:
                            print(f"{satellite_id} {nested_key} inside {field} field present")
                        else:
                            print(f"{satellite_id} {nested_key} inside {field} field missing")
            # Add logic here for anomaly checks?
            else:
                print(satellite_id, field, "field absent")
    else:
        print(satellite_id, " absent")