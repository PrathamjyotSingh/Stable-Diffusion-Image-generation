import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

st.title("Stable Diffusion Image Generator")

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe.to("cuda")

prompt = st.text_input("Enter your prompt", "A futuristic cityscape")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = pipe(prompt).images[0]
        st.image(image, caption="Generated Image")
