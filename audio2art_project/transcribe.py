import whisper

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio file
result = model.transcribe("audio.mp3")
text = result["text"]

print("Transcribed Text:", text)

# Save transcription to a file
with open("transcription.txt", "w") as f:
    f.write(text)
