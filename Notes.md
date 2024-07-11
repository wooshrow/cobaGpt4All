## GPT4all Python in Podman container

Use case:

  * You want to use Python to programmatically interact with an LLM model using GPT4ALL as the framework to facilitate the interactions.
  * You want to run the LLM and your script locally inside a Podman container.
  * You want to use the Host GPUs as well.



#### The Host

This is the computer on which Podman containers will run. Obviously, Podman needs to be installed in the Host as well.

To allow a Podman container to also access the Host's GPUs, I think the Host will need to have the [NVIDIA Container Toolkit installed](https://docs.nvidia.com/ai-enterprise/deployment-guide-rhel-with-kvm/0.1.0/podman.html#single-gpu). I don't have experience with this as I don't configure the Host myself. It was provided :)


#### What you need in the Container

   * I use an Ubuntu image.
   * To support the use of the Host's GPUs, you will need the Nvidia toolkit and the Vulkan SKD installed in the Container. You can check the Github of [GPT4ALL](https://github.com/nomic-ai/gpt4all) for these requirements. Check in the [Python-binding part](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python).

   I find installing the Nvidia tool kit to be quite challenging. So in the what I did:

      * I use an image provided by Nvidia: ``podman pull docker.io/nvidia/cuda:12.5.0-devel-ubuntu22.04``
      This is Ubuntu 22.04, with pre-installed Nvidia toolkit 12. It is a bit large, 3+GB. Maybe you can try smaller image like `nvidia/cuda:12.5.0-base-ubuntu22.04`. TO DO.

      * `apt install` the following: `software-properties-common`, `wget`, `nano`. Do `apt update` as needed.

      * Then [install Vulkan SDK](https://vulkan.lunarg.com/sdk/home).

      * To check if you have Nvidia toolkit in your Container do: `nvcc --version`.

      * To check if you have Vulkan SDK in your Container do: `vulkaninfo`

* Install Python e.g. Python 3.12. Then install `pip` too.

* Now you can install GPT4All in Python. Something like `python3.12 -m pip install gpt4all`.

* You can commit the Container to make a new base image that contains GPT4All and the needed GPU support.

Let's call your new base image now `myGPT4AllImage`

##### Running your Container with Host's GPUs

To run the image (so, creating a Container) with the Host's GPUs attachted to it, do this in the Host:

```
> podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable --it myGPT4AllImage bash
 ```

From the bash in the Container, to check if you indeed have GPUs do: `nvidia-smi -L`. This should list GPUs available to the Container.

You can now copy your Python-script that uses GPT4all into the Container you just ran. You probably also need to copy the LLM model you want to use into the Container as well. Then you can run the Python script in the Container.
