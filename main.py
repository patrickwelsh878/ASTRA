import json
import math

# Load in JSON telemetry file
with open("telemetry/telemetry.json", "r") as file:
    telemetry_data = json.load(file)

satellite_ids = ["HZN-001", "HZN-002", "HZN-003", "HZN-004"]
required_fields = ["temperature", "timestamp", "voltage", "position"]

# Min and max constraints for temp, voltage and orbital position data
# Includes the unit of measurement
MIN_TEMP_C = -20
MAX_TEMP_C = 50
MIN_VOLT_V = 20
MAX_VOLT_V = 35
EARTH_RADIUS_KM = 6371
MAX_ORBIT_KM = 50000

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
                # Temperature anomaly check
                if field == "temperature":
                    temperature = telemetry_data[satellite_id][field]
                    if temperature < MIN_TEMP_C:
                        print(f"{satellite_id} {field} below threshold")
                    elif temperature > MAX_TEMP_C:
                        print(f"{satellite_id} {field} above threshold")
                # Voltage anomaly check
                elif field == "voltage":
                    voltage = telemetry_data[satellite_id][field]
                    if voltage < MIN_VOLT_V:
                        print(f"{satellite_id} {field} below threshold")
                    elif voltage > MAX_VOLT_V:
                        print(f"{satellite_id} {field} above threshold")
                # Check nested positioning data
                elif field == "position":
                    all_present = True
                    for nested_key in ["x_km", "y_km", "z_km"]:
                        if nested_key in telemetry_data[satellite_id]["position"]:
                            print(f"{satellite_id} {nested_key} inside {field} field present")
                        else:
                            print(f"{satellite_id} {nested_key} inside {field} field missing")
                            all_present = False
                    # Positional anomaly check
                    #  Do this if all nested fields (x,y,z) are present
                    if all_present:
                        position_data = telemetry_data[satellite_id]["position"]
                        x = position_data["x_km"]
                        y = position_data["y_km"]
                        z = position_data["z_km"]
                        orbital_radius = math.sqrt(x**2 + y**2 + z**2)

                        if orbital_radius < EARTH_RADIUS_KM:
                            print(f"Error, {satellite_id} {field} inside Earth radius")
                        elif orbital_radius > MAX_ORBIT_KM:
                            print(f"Error, {satellite_id} {field} exceeds safe orbit radius")
                        else:
                            print(f"{satellite_id} {field} nominal")

            else:
                print(satellite_id, field, "field absent")
    else:
        print(satellite_id, " absent")