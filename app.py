import streamlit as st
import whisper
import torch
from diffusers import StableDiffusionPipeline
import os

# Set page title
st.title("🎤 Audio2Art - Convert Speech to AI-Generated Art 🎨")

# Upload an audio file
uploaded_file = st.file_uploader("audio.mp3", type=["mp3"])

if uploaded_file:
    # Save the uploaded file
    audio_path = "audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Audio file uploaded successfully!")

    # Load Whisper model
    st.write("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    text = result["text"]
    st.write("**Transcribed Text:**", text)

    # Refine text to create a detailed prompt
    refined_text = f"Highly detailed scene: {text}. Imagine a vivid and artistic representation."
    st.write("**Refined Prompt for AI:**", refined_text)

    # Load Stable Diffusion Model
    st.write("Generating image...")
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available

    # Generate the image
    image = pipe(refined_text).images[0]

    # Save and display the image
    image_path = "generated_image.png"
    image.save(image_path)

    st.image(image_path, caption="Generated Artwork", use_column_width=True)
