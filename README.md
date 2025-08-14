# 📊 Sales Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

## 📌 Overview
**Sales Analysis Dashboard** is an interactive data analytics tool built with **Python, Pandas, Matplotlib, Seaborn, and Streamlit**.  
It allows you to:
- Clean and preprocess sales datasets
- Explore trends, top products, and revenue breakdowns
- Visualize results with interactive charts
- Run in **Google Colab** for EDA or as a **Streamlit Web App**

---

## 📂 Project Structure
📂 sales-analysis-dashboard/
│
├── 📁 data/ # Raw and processed data
│ └── train.csv
│
├── 📁 notebooks/ # Jupyter/Colab notebooks for full EDA
│ └── sales_analysis.ipynb
│
├── 📁 scripts/ # Python scripts for modular code
│ ├── preprocess.py # Data loading & cleaning
│ ├── visualizations.py # All matplotlib/seaborn plots
│ └── save_plots.py # Code to save plots as PNG
│
├── 📁 app/ # Streamlit app folder
│ ├── app.py # Streamlit dashboard code
│ └── 📁 images/ # Saved visualizations for Streamlit
│
├── 📁 screenshots/ # Screenshots of your app for README
│ └── dashboard_preview.png
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore venv, cache, etc.


---

## ⚙️ Installation

# Clone repository
git clone https://github.com/your-username/sales-analysis-dashboard.git
cd sales-analysis-dashboard

# Install dependencies
pip install -r requirements.txt

🚀 Usage

Run EDA in Google Colab

Open notebooks/sales_analysis.ipynb in Colab.

Upload train.csv inside data/ folder or mount Google Drive.

Run all cells to:

Clean data

Generate charts

Save plots as PNG & ZIP

Run Streamlit Dashboard Locally

cd app

streamlit run app.py

Then open the link shown in your terminal (usually http://localhost:8501).

📸 Preview

Dashboard Example:

📊 Features
Preprocessing: Missing value handling, type conversion, and outlier removal.

EDA: Monthly sales trends, product performance, region-wise analysis.

Visualization: Matplotlib/Seaborn charts for deep insights.

Export: Save all plots as PNG and download as ZIP.

Streamlit App: Clean UI for non-technical users.

🛠️ Tech Stack
Python

Pandas, NumPy

Matplotlib, Seaborn

Streamlit

Google Colab

📜 License
This project is licensed under the MIT License.