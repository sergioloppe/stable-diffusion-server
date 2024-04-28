import uuid as uuid_module
from flask import request, request, send_file, jsonify, render_template, send_from_directory
from src.main import app
from src.services.inference_service import run_inference


@app.route('/')
def myapp():
    if "prompt" not in request.args:
        return "Please specify a prompt parameter", 400
    prompt = request.args["prompt"]
    img_data = run_inference(prompt)
    return send_file(img_data, mimetype='image/png')


@app.route('/app', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

