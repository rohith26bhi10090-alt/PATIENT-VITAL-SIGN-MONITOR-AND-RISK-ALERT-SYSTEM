# PATIENT-VITAL-SIGN-MONITOR-AND-RISK-ALERT-SYSTEM

--- 
## Overview

The Patient Health Vital Sign Monitor & Alert System is a Python-based healthcare monitoring project designed to track and analyze patient vital signs. The system checks whether a patient's pulse rate, body temperature, oxygen level, and blood pressure are within normal ranges.

It automatically identifies abnormal values, generates health alerts, classifies patient status (Stable, Warning, or Critical), calculates summary statistics, stores reports in log files, and allows users to search for patient records.

This project demonstrates the use of Python data structures, file handling, modules, loops, conditional statements, and basic healthcare data analysis.

---

## Features

### 1. Patient Monitoring

* Stores multiple patient records.
* Assigns a unique patient ID automatically.
* Displays patient information.

### 2. Vital Sign Analysis

* Checks pulse rate against normal limits.
* Checks body temperature against normal limits.
* Checks oxygen saturation levels.
* Checks blood pressure values.

### 3. Alert Generation

* Detects low or high vital signs.
* Generates warning messages.
* Identifies critical patients.

### 4. Patient Status Classification

* STABLE – All vitals are normal.
* WARNING – One abnormal vital sign detected.
* CRITICAL – Multiple abnormal vitals or oxygen level below 90%.

### 5. Report Generation

* Creates a health report with timestamp.
* Calculates average pulse rate.
* Shows overall health statistics.
* Stores reports in text files.

### 6. Search Functionality

* Search patient details by name.
* Displays complete patient information.

---

## Technologies / Tools Used

* Python 3.x
* datetime module
* random module
* os module
* Text File Handling
* Command Line Interface (CLI)

---

## Project Structure

```text
PatientHealthMonitor/
│
├── main.py
├── logs/
│   ├── report_YYYYMMDD_HHMMSS.txt
│
└── README.md
```

---

## Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

### Step 2: Download the Project

Clone the repository:

```bash
git clone <repository-link>
```

Or download the source code manually.

---

### Step 3: Navigate to Project Folder

```bash
cd PatientHealthMonitor
```

---

## How to Run

Execute:

```bash
python main.py
```

The system will:

1. Generate patient IDs.
2. Analyze vital signs.
3. Display alerts.
4. Generate a health report.
5. Save the report in the logs folder.
6. Allow searching for patient records.

---

## Sample Output

```text
Patient Health Report
Generated on: 2026-09-25 10:30:20

Name: Ravi (ID: P4321)
pulse : 72 (Normal)
temp : 98.4 (Normal)
oxygen : 98 (Normal)
bp : 115 (Normal)
Status: STABLE

Summary
Total Patients: 4
Average Pulse: 80.5
Danger Percentage: 50.0 %
```

---

## Testing Instructions

### Test Case 1: Normal Patient

Input Data:

```python
{"name":"Ravi","pulse":72,"temp":98.4,"oxygen":98,"bp":115}
```

Expected Result:

```text
Status: STABLE
```

---

### Test Case 2: High Pulse and Temperature

Input Data:

```python
{"name":"Anjali","pulse":115,"temp":100.2,"oxygen":96,"bp":130}
```

Expected Result:

```text
Status: CRITICAL
```

---

### Test Case 3: Low Oxygen Level

Input Data:

```python
{"name":"Suresh","pulse":55,"temp":98.0,"oxygen":89,"bp":85}
```

Expected Result:

```text
Status: CRITICAL
```

---


## Author
Rohith S

Patient Health Vital Sign Monitor & Alert System
