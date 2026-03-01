# 📊 Customer Churn Prediction & Agentic Retention Strategy

> From Predictive Analytics to Intelligent Intervention

## 📖 Project Overview
This project involves the design and implementation of an **AI-driven customer analytics system**. The application is built in two distinct phases: it first predicts customer churn using historical data, and then evolves into an agentic AI retention strategist that recommends actionable interventions.

### 🎯 Project Milestones
* **Milestone 1 (Mid-Sem):** Classical machine learning techniques are applied to historical customer behavior data to predict churn risk and identify key drivers of disengagement.
* **Milestone 2 (End-Sem):** The system is extended into an agent-based AI application that autonomously reasons about churn risk, retrieves retention best practices via RAG, and plans intervention strategies.

---

## 🏗 System Architecture


* **Phase 1 (Predictive Analytics):** Focuses on classical ML pipelines, feature engineering, and predictive modeling without the use of LLMs.
* **Phase 2 (Agentic Strategist):** Built using LangGraph, this phase involves state and node management, querying vector databases for retrieval-augmented generation (RAG), and using LLMs to format structured recommendations.

---

## 💻 Technology Stack

| Component | Technology |
| :--- | :--- |
| **ML Models (M1)** | Logistic Regression, Decision Trees, Scikit-Learn |
| **Agent Framework (M2)** | LangGraph, Chroma/FAISS (RAG) |
| **UI Framework** | Streamlit or Gradio |
| **LLMs (M2)** | Open-source models or Free-tier APIs |

---

## 🚀 Deliverables & Features

### Milestone 1: ML-Based Churn Prediction
* **Objective:** Identify customers at risk using historical behavioral data.
* **Key Outputs:**
    * Documentation of problem understanding and business context.
    * System architecture diagram.
    * Working local application with a Streamlit or Gradio UI.
    * Model performance evaluation report detailing metrics like Accuracy and F1 score.

### Milestone 2: Agentic AI Retention Assistant
* **Objective:** Extend the system to reason about risk, retrieve best practices, and generate structured recommendations.
* **Key Outputs:**
    * Publicly deployed application with a shared link.
    * Agent workflow documentation detailing States & Nodes.
    * Structured retention report generation.
    * Complete codebase hosted in this GitHub Repository.
    * A demonstration video (Max 5 mins).

---

## ⚙️ Installation & Usage

### Prerequisites
* Python 3.8+
* Git

### Setup Instructions
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application locally:**
    ```bash
    streamlit run app.py
    # or python app.py if using Gradio
    ```

---

## 🌐 Deployment
> **⚠️ WARNING:** Localhost-only demonstrations will **not** be accepted for final submission. The project must be hosted.

The final application must be publicly accessible. Supported hosting platforms include:
* Hugging Face Spaces
* Streamlit Cloud
* Render

---

## 👥 Project Guidelines & Constraints
* **Team Size:** 3–4 Students.
* **API Budget:** Strictly Free Tier Only (utilizing Open-source models and Free APIs).

## 📈 Evaluation Criteria
* **Mid-Sem (25%):** Evaluated on ML technique application, Feature Engineering, UI Usability, and Evaluation Metrics.
* **End-Sem (30%):** Evaluated on Reasoning quality, RAG & State management implementation, Output clarity, and Deployment success.
