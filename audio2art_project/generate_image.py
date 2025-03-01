from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available

# Read refined text
with open("refined_text.txt", "r") as f:
    refined_text = f.read()

# Generate image
image = pipe(refined_text).images[0]

# Save the generated image
image_path = "generated_image1.png"
image.save(image_path)

print("Image saved as:", image_path)
