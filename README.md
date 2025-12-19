# AI & IoT Powered Intelligent System for Real-Time Elephant Movement Detection

## 🐘 Project Overview
This project proposes an **AI and IoT–powered intelligent system** to detect elephant movement in real time and prevent **Human–Elephant Conflict (HEC)** in Chhattisgarh, India.  
The solution combines **Edge AI, LoRa mesh networking, and GPS collar tracking** to provide early warnings, accurate detection, and automated deterrence.

> Developed as part of **Smart India Hackathon 2025**  
> **Problem Statement ID:** SIH25167  
> **Theme:** Smart Automation  
> **Category:** Hardware  
> **Team Name:** STROMBREAKERS

---

## 🎯 Problem Addressed
Human–Elephant Conflict leads to:
- Loss of human lives  
- Crop and property damage  
- Elephant casualties, especially near villages, railways, and roads  

Existing systems are **costly**, **internet-dependent**, and often generate **false alarms** due to single-sensor reliance.

---

## 💡 Solution Highlights
- **Dual Verification Detection**  
  - Geophone (ground vibration) + Camera (visual confirmation)
- **Edge AI Processing**  
  - Local inference → ultra-low latency & reduced false positives
- **LoRa Mesh Network**  
  - Reliable communication in dense forests  
  - GSM backup for failover
- **Elephant GPS Collars**  
  - Real-time herd and rogue elephant tracking
- **Automated Deterrents**
  - AI-generated repellent sounds  
  - Sirens  
  - Chili-smoke deterrent (non-harmful)

---

## 🧠 System Architecture
**Flow:**  
Detection → Verification → Transmission → Alert → Deterrence → Analytics

### Layers:
1. **Field Hardware Layer**
   - Camera
   - Geophone
   - ESP32
   - ADS1115
   - Solar + Battery
2. **Edge AI Layer**
   - Image Processing (YOLO / TensorFlow / OpenCV)
   - Signal Processing (SVM)
3. **Communication Layer**
   - LoRa Mesh (Primary)
   - GSM (Backup)
4. **Server & Dashboard**
   - Real-time alerts
   - Geofencing
   - Analytics & reports
5. **Mobile App**
   - Farmer & forest-department alerts

---

## 🧰 Technology Stack

### Software
- **Frontend:** Flutter, React.js
- **Backend:** Django
- **Database:** MongoDB
- **Data Pipeline:** Flask, MQTT
- **ML Tools:** TensorFlow, Ultralytics YOLO, OpenCV, Google Colab
- **Maps:** OpenStreetMap API

### Hardware
- Raspberry Pi
- ESP32
- Camera Module
- Geophone Sensor
- ADS1115 ADC
- GPS Module
- LoRaWAN
- GSM Module
- Solar Power System

---

## 📊 Dashboard
The dashboard provides:
- Live elephant location tracking
- Alert feed with severity levels
- Geofencing visualization
- Historical analytics & reports

### 🔗 Dashboard Link
🚧 **Not yet published**  
The SIH submission document references a dashboard prototype but does **not include a public URL**.

```text
Dashboard Prototype: https://dineshkarthick2007.github.io/elephant-dashboard/
