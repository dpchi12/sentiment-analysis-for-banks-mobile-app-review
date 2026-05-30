# Sentiment Analysis of Mobile Banking App Reviews


This repository contains the code, data, and report for a reproducible research project on sentiment analysis of mobile banking app reviews. The project replicates an existing R-based analysis in Python, extends it with newly scraped data, and compares lexicon-based methods to a transformer (BERT) model.

---

## 1. Project Overview

The goal of this project is to perform a fully reproducible empirical study that:

- Reproduces an original R Markdown analysis of mobile banking app reviews in Python.
- Extends the analysis with a new, independently scraped dataset.
- Compares classic lexicon-based sentiment analysis with a transformer-based classifier.

---

## 2. Repository Structure

```text
sentiment-analysis-for-banks-mobile-app-review/
│
├── Dataset/
│   ├── data_old_approach/
│   │   ├── bank_of_america__combined_us.csv
│   │   ├── chase__combined_us.csv
│   │   ├── citi__combined_us.csv
│   │   ├── marcus_by_goldman_sachs__combined_us.csv
│   │   ├── wells_fargo__combined_us.csv
│   │   └── processed_data/ 
│   │       ├── old_preprocessed_lexicon.csv
│   │       ├── old_preprocessed_transformer.csv          
│   │
│   ├── data_new_approach/
│   │   ├── bank_of_america__combined_us.csv
│   │   ├── chase__combined_us.csv
│   │   ├── citi__combined_us.csv
│   │   ├── marcus_by_goldman_sachs__combined_us.csv
│   │   ├── wells_fargo__combined_us.csv
│   │   ├── new_preprocessed_transformer.csv
│   │   └── processed_data/
│   │       ├── new_preprocessed_lexicon.csv
│   │       ├── new_preprocessed_transformer.csv               
│   │
│   ├── nrc_lexicon/
│   │   └── NRC-Emotion-Lexicon-Wordlevel-v0.92.txt
│   │
│   └── scraper.ipynb                 # scraper used to collect the new dataset
│
├── Model (old data)/
│   ├── old_preprocessing.ipynb       # Python preprocessing for the original dataset
│   └── old_approach_sentiment_analysis.ipynb
│       # Lexicon + transformer analysis on old data
│
├── Model (new data)/
│   ├── new_preprocessing.ipynb       # Preprocessing for the new dataset 
│   └── new_data_sentiment_analysis.ipynb
│       # Lexicon + transformer analysis on new data
│
├── report.qmd                        
├── requirements.txt                  # Python dependencies 
└── README.md                         
```
---

## 3. How to reproduce  

### 3.1 Clone the Repository

```bash
git clone https://github.com/dpchi12/sentiment-analysis-for-banks-mobile-app-review.git
cd sentiment-analysis-for-banks-mobile-app-review
```

### 3.2 Set Up Python Environment

Create and activate a virtual environment (example for Unix/macOS):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
The `requirements.txt` file captures all packages used in the notebooks (data handling, NLP, plotting, transformers, scraping)

### 3.3 Reproduce Old-Data Analysis (Python)

1. Open `Model (old data)/old_preprocessing.ipynb`.
2. Run all cells to produce the preprocessed old-data CSVs.
3. Open `Model (old data)/old_approach_sentiment_analysis.ipynb`.
4. Run all cells to:
   - apply lexicon methods to the old dataset
   - train and evaluate the transformer model

### 3.4 Run New-Data Analysis

1. Open `Model (new data)/new_preprocessing.ipynb`.
2. Run all cells to generate preprocessed new-data outputs for both
   lexicon and transformer.
3. Open `Model (new data)/new_data_sentiment_analysis.ipynb`.
4. Run all cells to:
   - apply lexicon methods to the new dataset
   - train and evaluate the transformer model


---

## 4. Generative AI & Academic Integrity

In accordance with the Reproducible Research 2026 course rules, generative AI
(Claude AI) was used only to assist with coding and documentation.

All research questions, modelling choices, interpretation of results, and
write-up were carried out by our team. 

---

## 5. Team member

- Chi Dao 
- I Putu Agastya Harta Pratama
- Si Tang Lin
- Zuzanna Uljasz

Each team member contributed to data collection, preprocessing, modelling,
analysis, and reporting, in line with the project description discussed with
the professor.
