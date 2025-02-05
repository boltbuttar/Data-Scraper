# 📝 NeurIPS Research Paper Scraper

This script scrapes research papers from [NeurIPS Papers](https://papers.nips.cc), downloads PDFs, and extracts metadata (title, authors). The extracted data is saved in **CSV (`output.csv`)** and **JSON (`output.json`)** formats.

## 🚀 Features
- Scrapes research papers for the last **5 years**.
- Downloads PDFs using **multithreading**.
- Extracts metadata (title, authors) **immediately after downloading**.
- Saves extracted metadata in **CSV (`output.csv`)** and **JSON (`output.json`)**.

## 🛠️ Installation
Before running the script, install the required Python libraries:

```bash
pip install requests beautifulsoup4 tqdm
