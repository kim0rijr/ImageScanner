# Document Intelligence with OpenCV & Tesseract OCR

![Platforms](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-blue) 
![Demo](https://img.shields.io/badge/Demo-Streamlit-important) 
![License](https://img.shields.io/badge/License-MIT-success)

A cross-platform guide for document text extraction using **OpenCV** and **Tesseract OCR**. Complete with OS-specific setup instructions.

---

## 🖥️ System Requirements
### All Platforms
- Python 3.8+
- 4GB RAM (minimum)
- 500MB disk space

### macOS Specific
- macOS 10.15 (Catalina) or newer
- Xcode Command Line Tools

### Linux Specific
- Ubuntu 20.04/Debian 10 or equivalent
- GTK+ 3.x libraries

---

## 🛠️ Platform-Specific Setup

### 1. Tesseract OCR Installation

| OS | Command | Additional Notes |
|----|---------|------------------|
| **Windows** | [Download installer](https://github.com/UB-Mannheim/tesseract/wiki) | Check "Add to PATH" during install |
| **macOS** | `brew install tesseract` | Requires [Homebrew](https://brew.sh) |
| **Linux** | `sudo apt install tesseract-ocr libtesseract-dev` | For Debian/Ubuntu |

### 2. System Dependencies

**macOS:**
```bash
# Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install image libs
brew install leptonica
