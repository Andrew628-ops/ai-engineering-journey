# Lesson 07: Docker for AI

Date: 2026-10-24
Quiz: first attempt **1/3**; retake **3/3**.

## Session scope

I continued with a Dockerfile walkthrough because my student account could not access the Docker engine. No image build or container run was completed.

The lesson folder contains [Dockerfile](Dockerfile) and [app.py](app.py). Their build and runtime behavior remains untested.

## Why Docker is useful

A Python virtual environment isolates Python packages. A Docker image can also package the application's Python runtime and user-space system libraries.

Containers share the host kernel. An image does not include its own host kernel or guarantee that every machine has compatible hardware and drivers.

| Term | Meaning |
|------|---------|
| Dockerfile | Instructions for building an image |
| Image | Packaged application, runtime, and dependencies |
| Container | An instance created from an image, with its own processes and writable filesystem layer |
| Bind mount | A host path exposed at a path inside a container |
| Named volume | Persistent storage managed by Docker |
| Docker Compose | A tool for defining and coordinating multiple services |

One image can be used to create multiple containers.

## Docker access on this machine

I reported Docker client version **28.2.2**. `docker info` failed with permission denied for `/var/run/docker.sock`.

The checks showed:

```text
User groups: student user
Socket: srw-rw---- root docker /var/run/docker.sock
```

My account is not in the `docker` group and cannot use sudo. Docker access therefore requires an administrator's help or a different authorized environment. Docker-group membership grants effectively root-level access and is an administrator's decision.

A Dockerfile is an ordinary text file; editing it does not require access to the engine. Building an image and running containers require an available engine.

## The Dockerfile example we traced

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

- `FROM` selects the base image, which provides Python and minimal Linux user-space tools and libraries.
- `WORKDIR` sets `/app` as the working directory for subsequent instructions and the default runtime working directory.
- `COPY` copies `app.py` from the build context into `/app` during the build. It does not execute the Python file.
- `CMD` sets the default command used when a container starts. It does not run the application during the image build.

The example application prints a greeting and its Python version.

## Building and running: traced, not executed

From the lesson directory, these would build and run the example once engine access is available:

```bash
docker build -t lesson07-demo .
docker run --rm lesson07-demo
```

- `-t lesson07-demo` names the image.
- The final `.` supplies the current directory as the build context. `COPY` gets its source file from that context.
- `docker run` creates and starts a container from the image.
- `--rm` removes the container when its process exits; it does not remove the image.

Expected greeting:

```text
Hello from my container!
```

If I edit the local `app.py` after building, the old image still contains the old copy. I must rebuild to include the edit, unless I deliberately use a mount to supply the code at runtime.

## Container files and persistent storage

| Storage location | Stop and restart the same container | Remove the container |
|------------------|-------------------------------------|----------------------|
| Container writable layer | Files remain | Files are lost |
| Bind-mounted host folder | Files remain | Host files remain |
| Named volume | Files remain | Volume remains unless separately removed |

Stopping a container alone does not delete its writable layer. A container started with `--rm` is removed when it exits.

Persistent storage is useful for large models and datasets that should survive container removal or replacement.

Example bind mount, traced only:

```bash
docker run --rm -v "$PWD/models:/models" lesson07-demo
```

- `$PWD/models` is a folder on the host computer.
- `/models` is where it appears inside the container.
- A file written as `/models/weights.bin` is stored in the host folder and remains after the container is removed.

Similarly, if a host datasets folder is mounted at `/data`, writing `/data/results.csv` preserves that file on the host.

## Port mapping

Port mappings use **host port:container port**.

```bash
docker run --rm -p 8080:5000 my-web-app
```

This example assumes an image named `my-web-app` exists and runs a server listening on container port 5000. It was not built or run in this lesson.

The host browser uses `http://localhost:8080`; Docker forwards traffic to container port 5000. With `-p 9000:8888`, the host browser uses port **9000**.

For access through a published port, the server normally needs to listen on `0.0.0.0` inside the container rather than only the container's loopback interface.

## NVIDIA GPU access

The **NVIDIA Container Toolkit** exposes host NVIDIA GPUs to containers, typically through `--gpus all`.

The GPU driver remains on the host. A container can contain CUDA user-space libraries, but it still needs compatible host hardware and a compatible driver. The toolkit does not turn AMD hardware into an NVIDIA GPU.

No GPU-container setup was performed in this session.

## Docker Compose networking

A Dockerfile describes how to build an image. Compose describes services and how they run together, including their images, mounts, ports, and networks.

For example, an AI application can use an inference service plus a vector database service.

On Compose's default shared network, services can reach each other by service name. An `ai-dev` service can reach a database service named `qdrant` at:

```text
http://qdrant:6333
```

This is container-to-container communication. A host browser uses an appropriate published host port instead. Sharing a volume does not itself establish a network connection.

## What I corrected

- A bind-mounted file remains on the host after container removal.
- In a port mapping, the number on the left is the host port.
- NVIDIA Container Toolkit exposes the host GPU; it does not install the host driver inside the container.
- Compose services on a shared network use service names as hostnames.

## Quiz results and follow-up

First attempt: **1/3**. Persistent mounts were correct; GPU access and Compose networking needed review.

Retake: **3/3**. I correctly recalled all three concepts. The original attempt remains in the learning log.

Practical follow-up when authorized engine access is available:

1. Build the example image and run the Python application.
2. Test file persistence with a bind mount.
3. Practise publishing a web server's port.
4. Build and test an appropriate AI image and Compose services.

Next lesson: **Editor Setup**.
