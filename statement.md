# Patient Health Vital Sign Monitor & Alert System

## Problem Statement

Monitoring patient health manually can be time-consuming and may lead to delays in identifying critical health conditions. Healthcare staff need a simple system that can quickly analyze patient vital signs and alert them when any value falls outside the normal range.

The objective of this project is to develop a Python-based Patient Health Vital Sign Monitor that automatically checks patient vital signs, identifies abnormalities, generates alerts, and provides a health status report for better monitoring and decision-making.

---

## Scope of the Project

This project focuses on monitoring and analyzing basic patient vital signs, including:

* Pulse Rate
* Body Temperature
* Oxygen Saturation Level
* Blood Pressure

The system compares patient data with predefined normal ranges and classifies patients as Stable, Warning, or Critical. It also generates summary reports, stores report logs, and provides a patient search facility.

The project is intended for educational and demonstration purposes and does not replace professional medical diagnosis or treatment.

---

## Target Users

The primary users of this system are:

* Healthcare students and researchers
* Hospital staff for basic patient monitoring
* Clinic administrators
* Nursing staff
* Medical trainees
* Educational institutions for learning healthcare informatics concepts

---

## High-Level Features

### Patient Record Management

* Store and manage patient information.
* Generate unique patient IDs automatically.

### Vital Sign Monitoring

* Monitor pulse rate, temperature, oxygen level, and blood pressure.
* Compare values against predefined normal ranges.

### Alert Generation

* Detect abnormal vital signs.
* Generate warning and critical alerts.

### Health Status Classification

* Classify patients as:

  * STABLE
  * WARNING
  * CRITICAL

### Report Generation

* Create health reports with timestamps.
* Calculate average pulse rate.
* Display overall patient statistics.

### Log File Storage

* Save generated reports into text files for future reference.

### Patient Search

* Search patients by name.
* Display complete patient details instantly.

### Summary Analytics

* Show patients requiring attention.
* Display detected health issues.
* Calculate the percentage of patients in danger categories.

