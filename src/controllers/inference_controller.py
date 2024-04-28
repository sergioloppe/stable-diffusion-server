import uuid as uuid_module
from flask import request, send_file
from src.main import app
from src.services.inference_service import run_inference


@app.route('/api/inference', methods=['POST'])
def handleApiInference():
    data = request.get_json()
    prompt = data.get("prompt")
    negative_prompt = data.get("negative_prompt", None)
    width = data.get("width", 512)
    height = data.get("height", 512)
    guidance_scale = data.get("guidance_scale", 7)
    num_inference_steps = data.get("num_inference_steps", 20)
    seed = data.get("seed", 0)

    if not prompt:
        return {"error": "Prompt is required"}, 400

    img_data = run_inference(prompt, negative_prompt, width, height, guidance_scale, num_inference_steps, seed)
    return send_file(img_data, mimetype='image/png')


@app.route('/api/inference/test', methods=['GET'])
def handleApiInferenceTest():
    prompt = "A happy dog in a field of flow"
    img_data = run_inference(prompt)
    return send_file(img_data, mimetype='image/png')
