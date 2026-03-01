import streamlit as st

from modules.image_module import generate_image_caption
from modules.audio_module import transcribe_audio
from modules.fusion_module import build_fusion_prompt
from modules.llm_module import generate_final_response
from modules.tts_module import text_to_speech



# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="Multisense-AI",
    layout="centered"
)

# ---------------- Title ---------------- #
st.title("🧠 Multisense-AI")
st.write("A Multimodal AI Web App (Text • Image • Audio)")
st.markdown("---")


# ---------------- Inputs ---------------- #
text_input = st.text_input("✍️ Enter text (optional)")

image_file = st.file_uploader(
    "📷 Upload Image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

audio_file = st.file_uploader(
    "🎤 Upload Audio (MP3 / WAV)",
    type=["mp3", "wav"]
)

st.markdown("---")


# ---------------- Generate Response ---------------- #
if st.button("🚀 Generate Response"):

    if not text_input and not image_file and not audio_file:
        st.error("❌ Please provide at least one input.")
    else:
        st.success("✅ Inputs received successfully!")

        image_caption = None
        audio_text = None

        # -------- Image Processing -------- #
        if image_file:
            st.subheader("🖼️ Image Analysis")
            st.image(image_file, caption="Uploaded Image", width=500)

            with st.spinner("Analyzing image..."):
                image_caption = generate_image_caption(image_file)

            st.write(f"**Image Description:** {image_caption}")

        # -------- Audio Processing -------- #
        if audio_file:
            st.subheader("🎤 Audio Analysis")
            st.audio(audio_file)

            with st.spinner("Transcribing audio..."):
                audio_text = transcribe_audio(audio_file)

            st.write(f"**Audio Transcription:** {audio_text}")

        # -------- Multimodal Fusion -------- #
        fusion_prompt = build_fusion_prompt(
            user_text=text_input,
            image_caption=image_caption,
            audio_text=audio_text
        )

        st.subheader("📄 Fused Multimodal Context")
        st.text(fusion_prompt)

        # -------- Final Response -------- #
        with st.spinner("Generating final response..."):
            final_response = generate_final_response(fusion_prompt)

        st.subheader("🤖 Final Multimodal Response")
        st.write(final_response)
        # 🔊 Optional TTS Output
        with st.spinner("Generating audio response..."):
            audio_path = text_to_speech(final_response)

        st.subheader("🔊 Audio Output (Optional)")

        audio_path = text_to_speech(final_response)

        if audio_path:
            st.audio(audio_path)
        else:
            st.info("Audio output skipped because the response was empty.")