# Stable Diffusion Image Generator

## Description
This is a simple Streamlit-based web application that uses Stable Diffusion to generate images from text prompts. The application utilizes the `diffusers` library and runs on a GPU using PyTorch.

## Requirements
Make sure you have the following dependencies installed before running the application:

- `streamlit`
- `diffusers`
- `torch`
- `Pillow`

You can install them using:
```bash
pip install streamlit diffusers torch Pillow
```


## Usage
1. Run the application using:
```bash
streamlit run app.py
```

2. Enter a text prompt in the input field.
3. Click the "Generate Image" button.
4. The generated image will be displayed on the screen.

## Notes
- This application requires a GPU for efficient image generation. Ensure you have CUDA installed and a compatible GPU.
- The model used is `Stable Diffusion v1.5` from `runwayml`.

## Acknowledgments
This project uses Stable Diffusion from Hugging Face Diffusers: https://huggingface.co/runwayml/stable-diffusion-v1-5
