import datetime
import random
import os

# Normal ranges for vitals
limits = {
    "pulse": [60, 100],
    "temp": [97.0, 99.0],
    "oxygen": [95, 100],
    "bp": [90, 120]
}

patients = [
    {"name": "Ravi", "pulse": 72, "temp": 98.4, "oxygen": 98, "bp": 115},
    {"name": "Anjali", "pulse": 115, "temp": 100.2, "oxygen": 96, "bp": 130},
    {"name": "Suresh", "pulse": 55, "temp": 98.0, "oxygen": 89, "bp": 85},
    {"name": "Meera", "pulse": 80, "temp": 98.6, "oxygen": 97, "bp": 118}
]

# Assign each patient a random ID (random module)
for patient in patients:
    patient["id"] = "P" + str(random.randint(1000, 9999))

danger = set()
issues_found = set()

total_pulse = 0
count = 0

# Timestamp for this report (datetime module)
report_time = datetime.datetime.now()
report_str = report_time.strftime("%Y-%m-%d %H:%M:%S")

report_lines = []

def log(text=""):
    print(text)
    report_lines.append(text)

log("Patient Health Report")
log("Generated on: " + report_str)

for patient in patients:
    log("\nName: " + patient["name"] + " (ID: " + patient["id"] + ")")

    issues = []

    for vital in limits:
        value = patient[vital]
        low = limits[vital][0]
        high = limits[vital][1]

        if value < low:
            issues.append(vital + " is low (" + str(value) + ")")
            issues_found.add(vital + " low")

        elif value > high:
            issues.append(vital + " is high (" + str(value) + ")")
            issues_found.add(vital + " high")

        else:
            log(vital + " : " + str(value) + " (Normal)")

    if len(issues) > 0:
        log("Alerts:")
        for item in issues:
            log("- " + item)

    if patient["oxygen"] < 90 or len(issues) >= 2:
        status = "CRITICAL"
    elif len(issues) == 1:
        status = "WARNING"
    else:
        status = "STABLE"

    log("Status: " + status)

    if status != "STABLE":
        danger.add(patient["name"])

    total_pulse += patient["pulse"]
    count += 1

avg_pulse = total_pulse / count
danger_percent = (len(danger) / count) * 100

log("\nSummary")
log("Total Patients: " + str(count))
log("Average Pulse: " + str(round(avg_pulse, 1)))
log("Patients Needing Attention: " + str(danger))
log("Issues Found: " + str(issues_found))
log("Danger Percentage: " + str(round(danger_percent, 1)) + " %")

# Save the report to a log file using the os module
logs_folder = "logs"
if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

filename = "report_" + report_time.strftime("%Y%m%d_%H%M%S") + ".txt"
filepath = os.path.join(logs_folder, filename)

with open(filepath, "w") as f:
    f.write("\n".join(report_lines))

print("\nReport saved to:", filepath)

# Search patient details
while True:
    name = input("\nEnter patient name (or type exit): ")

    if name.lower() == "exit":
        print("Exiting...")
        break

    found = False

    for patient in patients:
        if patient["name"].lower() == name.lower():
            print("\nPatient Details")
            print("ID:", patient["id"])
            print("Pulse:", patient["pulse"])
            print("Temperature:", patient["temp"])
            print("Oxygen:", patient["oxygen"])
            print("Blood Pressure:", patient["bp"])
            found = True
            break

    if not found:
        print("Patient not found.")
