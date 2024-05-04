## inference_service.py
import io
from torch import autocast, manual_seed

from src.main import pipe, app


def run_inference(prompt, negative_prompt=None, width=512, height=512, guidance_scale=7, num_inference_steps=20, seed=0):
    with autocast(app.config['TORCH_AUTOCAST']):
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=1,
            generator=manual_seed(seed)
        ).images[0]

    img_data = io.BytesIO()
    image.save(img_data, "JPEG", quality=80)
    img_data.seek(0)
    return img_data
