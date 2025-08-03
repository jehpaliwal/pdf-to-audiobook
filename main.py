import pyttsx3
import PyPDF2

def read_pdf(file_path):
    try:
        # Open the PDF file in read-binary mode
        with open(file_path, 'rb') as book:
            pdf_reader = PyPDF2.PdfReader(book)
            print(f"✅ PDF has {len(pdf_reader.pages)} pages.")

            full_text = ""
            for page_num in range(len(pdf_reader.pages)):
                text = pdf_reader.pages[page_num].extract_text()
                if text:
                    full_text += text + "\n"
            return full_text
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return ""
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    print("🎧 Starting audio playback...")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    path = input("📄 Enter the path to your PDF file: ").strip()

    pdf_text = read_pdf(path)
    if pdf_text:
        speak_text(pdf_text)
    else:
        print("❌ No readable text found in the PDF.")