# 🌾 Intelligent Crop Yield Prediction & Agentic Farm Advisory

> From Agricultural Analytics to Autonomous Farming Advice

## 📖 Project Overview
This project involves the design and implementation of an AI-driven agricultural analytics system that predicts crop yield and evolves into an agentic AI farm advisory assistant. In Milestone 1, the system applies classical machine learning techniques to historical crop, soil, and weather data to predict yield and identify productivity factors.

### 🎯 Project Milestones
* **Milestone 1 (Mid-Sem):** Design and implement a machine learning-based crop yield prediction system using historical agricultural, soil, and weather data. The focus is on classical ML workflows without LLMs.

---

## 🏗 System Architecture & Flow

* **Inputs:** Farm data CSV containing crop, soil, and weather data. Features include Rainfall, Soil type, Fertilizer, and pH.
* **Preprocessing:** Handles missing values, feature scaling, and encoding.
* **Outputs:** Predicts crop yield or yield category. Displays predictions through a user interface and provides feature importance analysis.

---

## 💻 Technology Stack & Requirements

| Component | Technology / Metric |
| :--- | :--- |
| **ML Models** | Linear Regression, Decision Trees |
| **Evaluation Metrics** | MAE, RMSE, R-squared (Regression metrics) |
| **UI Framework** | Streamlit or Gradio (for local and hosted app) |
| **Deployment** | Accessible via a public URL |

---

## 🚀 Deliverables & Features

### Milestone 1: ML-Based Crop Yield Prediction
* **Objective:** Predict crop yield or yield category strictly using Traditional ML and Deep Learning; Agentic AI or GenAI-based methods are not used for this phase.
* **Key Outputs:**
    * Problem understanding & Agro-context.
    * Input–output specification.
    * System architecture diagram.
    * Working local application with UI.
    * Model performance evaluation report.

---

## ⚙️ Installation & Usage

### Setup Instructions
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sanath-2512/cropyeild_ml](https://github.com/sanath-2512/cropyeild_ml)
    cd cropyeild_ml
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application locally:**
    ```bash
    # Replace app.py with your main script name if using a different file
    streamlit run app.py
    # or python app.py if using Gradio
    ```

---

## 🌐 Deployment & Live Demo
The application has been successfully deployed and is accessible via a public URL. It is designed to work as intended during the demo with no crashes or timeouts under normal use.

* **Live Project Link:** [https://cropyield-pahp.onrender.com/](https://cropyield-pahp.onrender.com/)

---

## 📈 Evaluation Criteria

The project is evaluated on the following components:

| Component | Weight | Criteria |
| :--- | :--- | :--- |
| **Technical Implementation** | 0.30 | Correctness, Completeness, Depth & Complexity, Design Choices, and Performance. |
| **GitHub Repository & Code Quality** | 0.15 | Readability, Structure, History (meaningful commits), and Documentation (README.md). |
| **Project Report (LaTeX)** | 0.15 | Logical flow, clear technical explanations, inclusion of figures/results/citations, and professional LaTeX typesetting. |
| **Hosted Link / Live Demo** | 0.10 | Accessible via public URL, functionality, stability, and intuitive interface. |
| **Project Video (5 MINS)** | 0.10 | Clear problem statement, walkthrough of the working system, and good production quality. |
