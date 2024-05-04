from diffusers import StableDiffusionPipeline

from src.utils.hardware import detected_apple_silicon


def initialize_model(app_config):
    """Load and configure the Stable Diffusion model based on app config."""
    device = str(app_config.get("TORCH_DEVICE_NAME").type)
    use_hf_auth_token = app_config.get("HF_TOKEN") is not None
    stable_diffusion_model = app_config.get("HF_MODEL", "CompVis/stable-diffusion-v1-4")

    print(f'Device: {device}')
    print(f'Detecting Apple Silicon: {detected_apple_silicon()}')
    print(f'Diffusion model: {stable_diffusion_model}')
    print(f'Using token: {use_hf_auth_token}')

    return StableDiffusionPipeline.from_pretrained(
        stable_diffusion_model,
        use_auth_token=use_hf_auth_token,
        safety_checker=None
    ).to(device)
