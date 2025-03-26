# Document Intelligence with OpenCV & Tesseract OCR

![Platforms](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-blue) 
![Demo](https://img.shields.io/badge/Demo-Streamlit-important) 
![License](https://img.shields.io/badge/License-MIT-success)

A cross-platform guide for document text extraction using **OpenCV** and **Tesseract OCR**. Complete with OS-specific setup instructions.

---
## 🙌 Intro
A beginner-friendly guide to extracting text from documents using **OpenCV** for image processing and **Tesseract OCR** for text recognition. Designed for AI/Engineering students to understand foundational document intelligence concepts.

---

## 📖 Purpose
This project demonstrates how to:
- Detect text regions in images using basic computer vision techniques
- Extract machine-readable text with Tesseract OCR
- Build interactive document scanners with Streamlit/Jupyter
- **No deep learning or complex libraries** (like LayoutParser) required!

---

## 🔑 Key Takeaways
1. **OCR Workflow**: Preprocessing → Text Localization → OCR → Postprocessing  
2. **Tool Roles**:  
   - `OpenCV`: Image thresholding, contour detection, ROI extraction  
   - `Tesseract`: Optical Character Recognition (OCR) engine  
3. **Real-World Challenges**: Handling low contrast, complex layouts, multi-language text  
4. **Limitations**: Simpler but less accurate than deep learning approaches (e.g., LayoutParser)
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

| OS         | Command                                                                 | Additional Notes                          |
|------------|-------------------------------------------------------------------------|-------------------------------------------|
| **Windows**| [Download installer](https://github.com/UB-Mannheim/tesseract/wiki)     | Check "Add to PATH" during install        |
| **macOS**  | `brew install tesseract`                                                | Requires [Homebrew](https://brew.sh)      |
| **Linux**  | `sudo apt install tesseract-ocr libtesseract-dev`                       | For Debian/Ubuntu                         |

### 2. System Dependencies

**macOS:**
```bash
# Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install image libs
brew install leptonica
```

---

## ⚙️ Configuration Guide

### Tesseract Path Setup
Add this to your Python code:
```python
import pytesseract

# Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# macOS (Homebrew install)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Linux
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
```

---

## 🐧 Linux-Specific Notes

1. **Window Manager Conflicts**:  
   If using headless Linux server:
   ```bash
   sudo apt install xvfb
   export DISPLAY=:0
   ```
   
2. **Font Issues**: Install additional fonts
   ```bash
   sudo apt install tesseract-ocr-eng tesseract-ocr-fra  # etc.
   ```

---

##  macOS-Specific Notes

1. **M1/M2 Chip Optimization**:  
   Use native ARM Homebrew in Terminal:
   ```bash
   arch -arm64 brew install tesseract
   ```
   
2. **Gatekeeper Issues**: If blocked by macOS security:
   ```bash
   xattr -d com.apple.quarantine /path/to/tesseract
   ```

---

## 🚀 Universal Installation

```bash
# Clone repo
git clone https://github.com/yourusername/document-intelligence-demo.git
cd document-intelligence-demo

# Install requirements (in virtual env)
pip install -r requirements.txt
```

---

## ▶️ Running the Project

**All OS:**
```bash
streamlit run app.py  # Web app
jupyter notebook      # Jupyter version
```

![Cross-Platform Demo](demo_all_os.png)

---

## 🚨 Troubleshooting

| OS         | Issue                                      | Solution                                  |
|------------|--------------------------------------------|-------------------------------------------|
| **macOS**  | `Error: Failed building wheel for opencv` | `brew install cmake pkg-config`           |
| **Linux**  | `ImportError: libGL.so.1`                  | `sudo apt install libgl1-mesa-glx`        |
| **All**    | `TesseractNotFoundError`                   | Verify path with `which tesseract`        |

---

## 📜 License
MIT License - Free for academic and commercial use. Tesseract OCR is Apache 2.0 licensed.
```
