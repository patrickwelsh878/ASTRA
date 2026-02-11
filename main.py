import json

# Load in JSON telemetry file
with open("telemetry/telemetry.json", "r") as file:
    telemetry_data = json.load(file)

# Assign variables to key names in JSON
HZN_001 = "HZN-001"
HZN_002 = "HZN-002"
HZN_003 = "HZN-003"
temperature = "temperature"
voltage = "voltage"
timestamp = "timestamp"

# HZN_001 check
if HZN_001 in telemetry_data:
    print(f"\n{HZN_001} present in telemetry_data")
    if temperature in telemetry_data[HZN_001]:
        print(f"Temperature present in {HZN_001}")
    else:
        print(f"Temperature not present in {HZN_001}")
    if voltage in telemetry_data[HZN_001]:
        print(f"Voltage present in {HZN_001}")
    else:
        print(f"Voltage not present in {HZN_001}")
    if timestamp in telemetry_data[HZN_001]:
        print(f"Timestamp present in {HZN_001}")
    else:
        print(f"Timestamp not present in {HZN_001}")
else:
    print(f"Failed to retrieve data for {HZN_001}")

# HZN_002 check
if HZN_002 in telemetry_data:
    print(f"\n{HZN_002} present in telemetry_data")
    if temperature in telemetry_data[HZN_002]:
        print(f"Temperature present in {HZN_002}")
    else:
        print(f"Temperature not present in {HZN_002}")
    if voltage in telemetry_data[HZN_002]:
        print(f"Voltage present in {HZN_002}")
    else:
        print(f"Voltage not present in {HZN_002}")
    if timestamp in telemetry_data[HZN_002]:
        print(f"Timestamp present in {HZN_002}")
    else:
        print(f"Timestamp not present in {HZN_002}")
else:
    print(f"Failed to retrieve data for {HZN_002}")


# HZN_003 check
if HZN_003 in telemetry_data:
    print(f"\n{HZN_003} present in telemetry_data")
    if temperature in telemetry_data[HZN_003]:
        print(f"Temperature present in {HZN_003}")
    else:
        print(f"Temperature not present in {HZN_003}")
    if voltage in telemetry_data[HZN_003]:
        print(f"Voltage present in {HZN_003}")
    else:
        print(f"Voltage not present in {HZN_003}")
    if timestamp in telemetry_data[HZN_003]:
        print(f"Timestamp present in {HZN_003}")
    else:
        print(f"Timestamp not present in {HZN_003}")
else:
    print(f"Failed to retrieve data for {HZN_003}")