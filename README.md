# stable-diffusion-server
Stable Diffusion Server (for Civitai Models)

Roadmap
[X] Basic API to run stable-diffusion from a browser
[X] Support for CUDA and CPU (CPU is not a good idea for this kind of models)
[X] Dockerize application
[ ] Add Example for Civitai models

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

## Build frontend with docker
```shell
docker build -f Dockerfile.frontend -t sd-frontend .
docker run --gpus all -p 8080:8080  -v ~/.cache/huggingface:/root/.cache/huggingface sd-frontend
```

