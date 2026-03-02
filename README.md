# 🌾 Intelligent Crop Yield Prediction & Farm Advisory

> A comprehensive machine learning toolkit for predicting agricultural productivity using historical crop, soil, and weather data. 

## Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project serves as **Milestone-1** in developing an AI-driven agricultural analytics system. It focuses exclusively on traditional Machine Learning pipelines to predict crop yields and identify key productivity factors without relying on Large Language Models (LLMs) or Agentic AI. 

By analyzing critical inputs like rainfall, soil type, and fertilizer usage, this classical ML approach provides a robust, interpretable baseline. This foundation motivates the transition toward an autonomous, agent-based farm advisory system in future milestones.

## Live Demo

* **Deployed Web Application:** [Crop Yield Predictor on Render](https://cropyield-pahp.onrender.com/)
* **GitHub Repository:** [sanath-2512/cropyeild_ml](https://github.com/sanath-2512/cropyeild_ml)

## Features

### Core Capabilities

- **Data Processing**: Accepts and processes raw agricultural CSV data (Soil, Weather, Crop).
- **Automated Preprocessing**: Handles missing values, performs feature scaling (Standardization/Normalization), and applies categorical encoding (One-Hot/Label Encoding).
- **Yield Prediction**: Generates numerical or categorical crop yield predictions based on environmental inputs.
- **Feature Importance**: Analyzes and extracts the most significant factors driving crop growth (e.g., pH, Rainfall).
- **Evaluation Metrics**: Calculates and displays Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared ($R^2$) scores.

### Interactive Web Interface

Built with Streamlit/Gradio, the interface provides:
- Simple input forms for farmers or agricultural analysts to enter soil and weather parameters.
- Real-time yield predictions based on the trained models.
- Visual breakdowns of which features impacted the prediction the most.
- Clean, intuitive, and accessible UI design.

## Tech Stack

### Core Libraries

- **Python 3.8+**: Primary programming language
- **Streamlit / Gradio**: Web application and UI framework
- **scikit-learn**: Machine learning algorithms and preprocessing utilities
- **pandas**: Data manipulation, cleaning, and CSV parsing
- **numpy**: Numerical computations and matrix operations

### Supporting Libraries

- **matplotlib / seaborn**: Plotting and data visualization (Feature importance charts)
- **joblib / pickle**: Model saving and loading

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Setup Steps

1. **Clone the repository**

```bash
git clone [https://github.com/sanath-2512/cropyeild_ml.git](https://github.com/sanath-2512/cropyeild_ml.git)
cd cropyeild_ml
