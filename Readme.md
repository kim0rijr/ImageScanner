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

---------------------------------------------------------------------------------------------------------------

**Linux:**
```bash
# Required libraries
sudo apt install libopencv-dev python3-dev libgl1
```

### 3. Python Virtual Environment (All OS)
```bash
python -m venv docenv
source docenv/bin/activate  # Linux/macOS
docenv\Scripts\activate     # Windows
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
git clone [here](https://github.com/chankjen/Coffee-n-Code.git)
cd Coffee-n-Code

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

| OS | Issue | Solution |
|----|-------|----------|
| **macOS** | `Error: Failed building wheel for opencv-python` | `brew install cmake pkg-config` |
| **Linux** | `ImportError: libGL.so.1` | `sudo apt install libgl1-mesa-glx` |
| **All** | `TesseractNotFoundError` | Verify path with `which tesseract` (Linux/macOS) |

---

## 📜 License
MIT License - Free for academic and commercial use. Tesseract OCR is Apache 2.0 licensed.
```

Key additions:
1. Separate system requirements for each OS
2. Platform-specific installation tables
3. Apple Silicon (M1/M2) optimization notes
4. Linux headless server configuration
5. OS-specific troubleshooting table
6. Universal commands marked clearly
7. Visual badges showing cross-platform support

