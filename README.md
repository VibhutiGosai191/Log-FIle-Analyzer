# Log File Analyzer (Python Project)

## Overview

The **Log File Analyzer** is a Python-based cybersecurity tool that reads system or server log files and detects suspicious activities such as failed login attempts, invalid users, port scans, and SQL injection patterns.

This project is designed to demonstrate core Python concepts including:

* Object-Oriented Programming (OOP)
* Multithreading
* File Handling
* Regular Expressions (Regex)

---

## 🎯 Features

* 📂 Reads log files automatically
* 🔎 Detects suspicious activities using regex
* 🧵 Multithreaded processing for large logs
* 📊 Generates summary of detected events
* 💾 Saves detailed report
* 🖥️ Optional GUI for user interaction

---

## 🧠 How It Works

1. The system reads a log file line-by-line
2. Multiple threads process log lines concurrently
3. Regex patterns detect suspicious activities
4. Detected events are stored and categorized
5. A summary and report are generated

---

## 📁 Project Structure

```
log_analyzer/
│── analyzer/
│   ├── log_analyzer.py
│   ├── patterns.py
│   ├── utils.py
│── logs/
│   ├── sample.log
│── output/
│   ├── report.txt
│── main.py
│── ui.py (optional)
│── requirements.txt
│── README.md
```

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

If not using requirements file:

```bash
pip install colorama matplotlib
```

---

## How to Run

### 🔹 Run using CLI (recommended)

```bash
python main.py
```

---

### 🔹 Run GUI (optional)

```bash
python ui.py
```

---

## Input Log File

The program expects a log file containing entries like:

```
Failed password for root from 192.168.1.10
Invalid user admin from 10.0.0.5
SELECT * FROM users
DROP TABLE users;
```

---

## 📊 Output

### Console Output

* Summary of detected events
* Execution time

### File Output

* `output/report.txt` containing detailed logs

---

## 🧩 Python Concepts Used

### 🔹 Object-Oriented Programming

* `LogAnalyzer` class organizes the logic

### 🔹 Multithreading

* Multiple threads process logs simultaneously

### 🔹 File Handling

* Reads and writes log files

### 🔹 Regex

* Detects patterns like SQL injection and failed logins

---

## Limitations

* Detects only predefined patterns
* Not suitable for unknown threats
* Requires log file input

---

## Future Enhancements

* Real-time monitoring
* AI-based anomaly detection
* Web dashboard
* Email alerts

---

## Example Use Case

This tool can be used to:

* Analyze server logs
* Detect suspicious login attempts
* Identify potential cyber attacks

---

## 🗣️ Author

* Vibhuti, Bhavya, Shweta
* Course: Python Programming
* Project: Log File Analyzer

---
