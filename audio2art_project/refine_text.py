import re

def refine_prompt(text):
    """
    Refines the given text by cleaning it up and making it more descriptive.
    """
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Capitalize the first letter of each sentence
    sentences = re.split(r'(?<=[.!?]) +', text)
    refined_text = ' '.join(sentence.capitalize() for sentence in sentences)
    
    # Add additional descriptive elements (if needed)
    refined_text = f"Highly detailed scene: {refined_text}. Imagine a vivid and artistic representation."

    return refined_text

# Read transcribed text
with open("transcription.txt", "r") as f:
    user_text = f.read()

# Refine text
refined_text = refine_prompt(user_text)
print("Refined Prompt:", refined_text)

# Save refined text
with open("refined_text.txt", "w") as f:
    f.write(refined_text)
import re

def refine_prompt(text):
    """
    Refines the given text by cleaning it up and making it more descriptive.
    """
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Capitalize the first letter of each sentence
    sentences = re.split(r'(?<=[.!?]) +', text)
    refined_text = ' '.join(sentence.capitalize() for sentence in sentences)
    
    # Add additional descriptive elements (if needed)
    refined_text = f"Highly detailed scene: {refined_text}. Imagine a vivid and artistic representation."

    return refined_text

# Read transcribed text
with open("transcription.txt", "r") as f:
    user_text = f.read()

# Refine text
refined_text = refine_prompt(user_text)
print("Refined Prompt:", refined_text)

# Save refined text
with open("refined_text.txt", "w") as f:
    f.write(refined_text)
