# 🧠 Multisense-AI

## A Multimodal AI Web Application (Text • Image • Audio)

Multisense-AI is a multimodal AI web application that accepts **text, image, and audio inputs**, processes each modality using specialized AI models, fuses the extracted information into a unified context, and generates a **single, coherent, context-aware response**. An optional **Text-to-Speech (TTS)** extension converts the final response into spoken audio.

---

## ✨ Features

- ✍️ **Text Input** – User-provided text queries
- 📷 **Image Understanding** – Automatic image captioning
- 🎤 **Audio Transcription** – Speech-to-text conversion
- 🧩 **Multimodal Fusion** – Combines all inputs into one prompt
- 🤖 **LLM Reasoning** – Generates intelligent, human-like responses
- 🔊 **Audio Output (Optional)** – Speaks the final response
- 🌐 **Web Interface** – Built using Streamlit

---

## 🏗️ System Architecture

```
User Inputs (Text / Image / Audio)
        ↓
Image Model (BLIP) → Image Caption
Audio Model (Whisper) → Transcription
        ↓
Multimodal Fusion (Prompt Builder)
        ↓
Large Language Model (DeepSeek via API)
        ↓
Final Text Response
        ↓
(Optional) Text-to-Speech (pyttsx3)
```

---

## 🧠 Technologies Used

| Component | Technology |
|-----------|-----------|
| Web UI | Streamlit |
| Image Processing | BLIP (transformers) |
| Audio Processing | Whisper |
| LLM | DeepSeek (via OpenRouter API) |
| TTS (Optional) | pyttsx3 (offline) |
| Language | Python |

---

## 📁 Project Structure

```
multisense-ai/
├── app.py
├── modules/
│   ├── image_module.py
│   ├── audio_module.py
│   ├── fusion_module.py
│   ├── llm_module.py
│   └── tts_module.py
├── evaluation_report.md
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10 – 3.12
- pip
- Internet connection (for LLM API)
- FFmpeg (required for Whisper)

---

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/pravallika-mutyala/multisense-ai.git
cd multisense-ai
```


### Step 2: Create & Activate Virtual Environment

```bash
python -m venv multisense-venv
```

**Windows (PowerShell / CMD):**
```bash
multisense-venv\Scripts\activate
```

**Git Bash / Linux / Mac:**
```bash
source multisense-venv/Scripts/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip 
or 
python -m pip install --upgrade pip

pip install streamlit transformers torch pillow openai-whisper pyttsx3 requests
```

### Step 4: Install FFmpeg

Download FFmpeg from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

1. Download **ffmpeg-release-essentials**
 or directly click on this link to download : [https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip]
2. Extract the folder
3. Add the `bin` folder to your system PATH

Verify installation:
```bash
ffmpeg -version
```

---

## 🔐 API Key Configuration

This project uses **DeepSeek via OpenRouter**.

### Get an API Key

Visit: [https://openrouter.ai/](https://openrouter.ai/)

### Set Environment Variable

**Windows (PowerShell):**
```powershell
setx OPENROUTER_API_KEY "your_api_key_here"
```
Restart your terminal after setting this.

**Linux / Mac / Git Bash:**
```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at:
```
http://localhost:8501
```

---

## 🧪 How to Use the App

1. ✍️ Enter **text** (optional)
2. 📷 Upload an **image** (JPG / PNG)
3. 🎤 Upload an **audio file** (MP3 / WAV)
4. Click **"Generate Response"**
5. View the results:
   - Image caption
   - Audio transcription
   - Fused multimodal context
   - 🤖 Final AI response
   - 🔊 Spoken audio output (optional)

### Test Different Combinations

- Text + Image
- Text + Audio
- Image + Audio
- Text + Image + Audio

---

## 🧩 How Multimodal Fusion Works

The system processes inputs in this order:

1. Converts **image → text** (using BLIP)
2. Converts **audio → text** (using Whisper)
3. Collects **user-provided text**
4. Fuses all information into a **structured prompt**
5. Sends to **DeepSeek LLM** via OpenRouter API
6. Generates a **single, coherent response**

---

## 🔊 Text-to-Speech (Optional)

The application includes an optional TTS feature:

- Converts final AI response into **spoken audio**
- Uses **pyttsx3** for offline processing
- No additional API calls needed
- Compatible with Python 3.10 – 3.12

---

## ✅ What This Project Covers

- ✔ Accepts text, image, and audio inputs
- ✔ Supports multiple modality combinations
- ✔ Accurately transcribes speech
- ✔ Correctly identifies image content
- ✔ Generates context-aware responses
- ✔ Handles errors gracefully
- ✔ Provides optional audio output

---
## 🏁 Conclusion

Multisense-AI demonstrates a **complete end-to-end multimodal AI pipeline**, integrating vision, speech, and language models into a single interactive web application. It meets all core requirements and includes an optional audio output extension, making it suitable for academic evaluation, demos, and further research.

---
