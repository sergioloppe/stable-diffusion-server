from flask import request, jsonify, send_file
from src.main import app
from src.services.inference_service import run_inference
import io


@app.route('/api/inference', methods=['POST'])
def handleApiInference():
    if not request.is_json:
        return jsonify({"error": "Invalid input", "message": "MIME type not application/json"}), 415

    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Validation error", "message": "Prompt is required"}), 400

    negative_prompt = data.get("negative_prompt", None)
    width = data.get("width", 512)
    height = data.get("height", 512)
    guidance_scale = data.get("guidance_scale", 7)
    num_inference_steps = data.get("num_inference_steps", 20)
    seed = data.get("seed", 0)

    try:
        img_data = run_inference(prompt, negative_prompt, width, height, guidance_scale, num_inference_steps, seed)
        return send_file(img_data, mimetype='image/png')
    except Exception as e:
        app.logger.error(f"Failed to generate image: {str(e)}")
        return jsonify({"error": "Server error", "message": "Failed to generate image"}), 500


@app.route('/api/inference/test', methods=['GET'])
def handleApiInferenceTest():
    try:
        prompt = "A mysterious castle in the sky"
        img_data = run_inference(prompt)
        return send_file(img_data, mimetype='image/png')
    except Exception as e:
        app.logger.error(f"Failed to process test inference: {str(e)}")
        return jsonify({"error": "Server error", "message": "Failed to process test inference"}), 500

