# app.py
import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image

# Configure Tesseract (update path for your system)
pytesseract.pytesseract.tesseract_cmd = st.sidebar.text_input(
    "Tesseract Path",
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Default for Windows
)

st.title("📄 Document Scanner with Word Grouping")
st.sidebar.markdown("## Settings")

def process_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    processed_img = img.copy()
    
    # Image processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    text_groups = []
    total_words = 0

    with st.status("Analyzing document...", expanded=True) as status:
        for i, cnt in enumerate(contours):
            x, y, w, h = cv2.boundingRect(cnt)
            if w * h > 1000:  # Minimum area threshold
                # Draw bounding box
                cv2.rectangle(processed_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # OCR processing
                roi = img[y:y+h, x:x+w]
                text = pytesseract.image_to_string(roi).strip()
                
                if text:
                    words = text.split()
                    word_count = len(words)
                    total_words += word_count
                    
                    text_groups.append({
                        "id": i+1,
                        "word_count": word_count,
                        "text": text,
                        "coordinates": (x, y, w, h)
                    })

        status.update(label="Analysis complete!", state="complete")
    
    return processed_img, text_groups, total_words

uploaded_file = st.file_uploader("Upload Document Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    if st.button("Analyze Document"):
        # Store results in session state
        st.session_state.processed_img, st.session_state.text_groups, st.session_state.total_words = process_image(uploaded_file)
    
    if 'text_groups' in st.session_state:
        # Display processed image
        st.image(cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB), 
                caption="Processed Document", 
                use_column_width=True)
        
        # Summary stats
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Text Groups", len(st.session_state.text_groups))
        with col2:
            st.metric("Total Words Found", st.session_state.total_words)
        
        # Grouped text display
        st.subheader("Text Group Details")
        for group in st.session_state.text_groups:
            with st.expander(f"Group {group['id']} ({group['word_count']} words)"):
                col_a, col_b = st.columns([1, 4])
                with col_a:
                        st.write(f"**Location:**\nX: {group['coordinates'][0]}\nY: {group['coordinates'][1]}")
                        st.write(f"**Size:**\n{group['coordinates'][2]}x{group['coordinates'][3]}")  # Fixed here
                with col_b:
                    st.write(group['text'])
        
        # Data export
        st.download_button(
            label="Download Results as TXT",
            data="\n\n".join([f"Group {g['id']} ({g['word_count']} words):\n{g['text']}" 
                            for g in st.session_state.text_groups]),
            file_name="document_analysis.txt"
        )

# Sidebar help
st.sidebar.markdown("### Installation Help")
st.sidebar.write("**Windows:** Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)")
st.sidebar.write("**macOS:** `brew install tesseract`")
st.sidebar.write("**Linux:** `sudo apt install tesseract-ocr`")