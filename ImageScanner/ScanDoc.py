# app.py
import streamlit as st
import cv2
import pytesseract
import numpy as np

# Configure Tesseract (update path for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("📄 Simple Document OCR")
uploaded_file = st.file_uploader("Upload Document Image", type=["jpg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Basic layout detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes and extract text
    processed_img = img.copy()
    all_text = []
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 1000:
            cv2.rectangle(processed_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi = img[y:y+h, x:x+w]
            text = pytesseract.image_to_string(roi)
            all_text.append(text)
    
    # Display results
    st.image(processed_img, caption="Processed Image", use_column_width=True)
    st.subheader("Extracted Text")
    st.code("\n".join(all_text))