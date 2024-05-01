# stable-diffusion-server
Stable Diffusion Server (for Civitai Models)

![example.png](images%2Fexample.png)

### Disclaimer
This is a personal project, and it is not related to Civitai or Huggingface. The code is provided without any warranty. 
I don't recommend using no CUDA or MPS (Apple M1 or higher) for this kind of models. The inference time will be very slow.

### Roadmap
- [X] Basic API to run stable-diffusion from a browser
- [X] Support for CUDA and CPU (CPU is not a good idea for this kind of models)
- [X] Dockerize application
- [ ] Add Example for Civitai models
- [ ] Manage different models (backend/frontend)
- [ ] Ansible scripts for the backend API without frontend

# Build and Run
## Build with docker-compose
```shell
docker-compose up --build
```
If your model is private you have to set the Huggingface token in the environment variable before running the docker-compose command.
```shell
export HF_TOKEN=your_token
```
Be aware that you have to open the port 3000 in your firewall.
```shell
sudo ufw allow 3000
```
If you want just to build and expose the backend for a simple API integration open the port 8080
```shell
sudo ufw allow 8080
```
and check the next section to build the backend.

## Build backend server with docker
The first time the server runs it will download the model from huggingface and save it in the cache folder. This will take some time.
```shell
docker build -f Dockerfile.backend -t sd-backend .
docker run --gpus all -p 8080:8080  -v ~/.cache/huggingface:/root/.cache/huggingface sd-backend
```

### Huggingface token
If your model is private you have to set the Huggingface token in the environment variable `HF_TOKEN`
```shell
export HF_TOKEN=your_token
docker build --rm -f Dockerfile.backend -t sd-backend --build-arg HF_TOKEN=${HF_TOKEN} .
```

If you don't know how to set up your personal server with docker check my gist
- [How to install Docker with NVIDIA CUDA support in Ubuntu 20.04 or Ubuntu 22.04](https://gist.github.com/sergioloppe/a4d036095100b4e711d9d2502cdae886)


## Build frontend with docker
```shell
docker build -f Dockerfile.frontend -t sd-frontend .
docker run --gpus all -p 8080:8080  -v ~/.cache/huggingface:/root/.cache/huggingface sd-frontend
```

# Inference examples via API
### Example 1
Default parameters:
- width: 512
- height: 512
- guidance_scale: 7
- num_inference_steps: 20
- seed: 0
- 
```shell
curl -X POST http://your_server_ip:8080/api/inference --output castle-in-the-sky.png  \
-H "Content-Type: application/json" \
-d '{
    "prompt": "A mysterious castle in the sky"
}'
```
![example.png](images%2Fexample.png)

### Example 2
```shell
curl -X POST http://your_server_ip:3000/api/inference --output futuristic-city.png  \
-H "Content-Type: application/json" \
-d '{
    "prompt": "A futuristic city at sunset",
    "negative_prompt": "no people",
    "width": 720,
    "height": 480,
    "guidance_scale": 10,
    "num_inference_steps": 50,
    "seed": 42
}'
```
![futuristic-city.png](images%2Ffuturistic-city.png)