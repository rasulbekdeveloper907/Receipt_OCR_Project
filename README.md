# 🧾 Receipt OCR Project

A production-ready **Receipt OCR (Optical Character Recognition)** system built with Python and the **SROIE 2019** dataset.

This project extracts key information from receipt images using modern Computer Vision, OCR, and Information Extraction techniques. The long-term goal is to build an end-to-end Receipt OCR pipeline that can be deployed as a REST API and web application.

---

# 🚀 Project Goals

- Extract text from receipt images
- Automatically identify important receipt information
- Build a modular and scalable OCR pipeline
- Deploy the model using FastAPI
- Create a user-friendly interface with Streamlit
- Follow production-level software engineering practices

---

# 📌 Features

- Receipt Image Processing
- Image Preprocessing using OpenCV
- OCR Pipeline
- Key Information Extraction
- Structured JSON Output
- FastAPI REST API
- Streamlit Web Application
- Docker Deployment
- Modular Project Architecture
- Unit Testing

---

# 🏗️ Project Structure

```text
Receipt_OCR_Project/
│
├── app/                    # API and Streamlit application
│
├── data/
│   ├── raw/                # Original dataset
│   ├── processed/          # Processed images
│   └── external/           # External resources
│
├── docs/                   # Documentation
│
├── models/                 # Trained models
│
├── notebooks/              # Experiments and analysis
│
├── outputs/                # Predictions and exported files
│
├── src/
│   ├── preprocessing/      # Image preprocessing
│   ├── ocr/                # OCR engine
│   ├── extraction/         # Information extraction
│   ├── utils/              # Utility functions
│   └── config/             # Configuration files
│
├── tests/                  # Unit tests
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📊 Dataset

Dataset used:

**SROIE 2019 - Scanned Receipts OCR and Information Extraction**

The dataset contains:

- Receipt Images
- OCR Annotations
- Key Information Labels

Target fields:

- Company
- Address
- Date
- Total Amount

---

# 🔄 Project Workflow

```text
Receipt Image
        │
        ▼
Image Preprocessing
        │
        ▼
OCR Engine
        │
        ▼
Raw Text
        │
        ▼
Information Extraction
        │
        ▼
JSON Output
        │
        ▼
REST API / Streamlit
```

---

# 🛠️ Technology Stack

## Programming Language

- Python 3.x

## Computer Vision

- OpenCV
- Pillow
- NumPy

## OCR

- PaddleOCR
- EasyOCR
- Tesseract OCR

## Data Processing

- Pandas
- Regular Expressions

## Deep Learning (Future)

- PyTorch
- Hugging Face Transformers
- LayoutLMv3
- Donut
- TrOCR

## Backend

- FastAPI
- Pydantic

## Frontend

- Streamlit

## Deployment

- Docker

---

# 📈 Development Roadmap

## Phase 1

- [ ] Project Initialization
- [ ] Dataset Validation
- [ ] Dataset Loader

## Phase 2

- [ ] Image Preprocessing
- [ ] Image Enhancement
- [ ] Noise Removal
- [ ] Thresholding
- [ ] Perspective Correction

## Phase 3

- [ ] OCR Pipeline
- [ ] PaddleOCR Integration
- [ ] OCR Evaluation

## Phase 4

- [ ] Receipt Information Extraction
- [ ] Company Extraction
- [ ] Address Extraction
- [ ] Date Extraction
- [ ] Total Amount Extraction

## Phase 5

- [ ] JSON Generator
- [ ] Validation Rules

## Phase 6

- [ ] FastAPI Integration
- [ ] REST API

## Phase 7

- [ ] Streamlit Web Application

## Phase 8

- [ ] Docker Deployment

---

# 📄 Example Output

```json
{
    "company": "STARBUCKS",
    "address": "KUALA LUMPUR",
    "date": "2018-11-02",
    "total": "18.90"
}
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/rasulbekdeveloper907/Receipt_OCR_Project.git
```

Go to project

```bash
cd Receipt_OCR_Project
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

The project modules can be executed independently during development.

Future versions will include:

- FastAPI Server
- Streamlit Application

---

# 📌 Current Status

🚧 Under Active Development

This repository is being developed incrementally following production-level software engineering practices.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Rasulbek Ruzmetov**

GitHub:
https://github.com/rasulbekdeveloper907

---

⭐ If you find this project useful, consider giving it a Star.