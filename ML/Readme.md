# Stable Diffusion

To run this and to understand what you're getting into: You need to be familiar with the [licensing](https://huggingface.co/spaces/CompVis/stable-diffusion-license) and use cases. I won't be in charge of you violating their licensing by using some code I slapped together :)

## Background Information

* [Hugging Face Blog](https://huggingface.co/blog/stable_diffusion) about Running Stable Diffusion and setting it up
* [Token Information from Hugging Face](https://huggingface.co/docs/hub/security-tokens)

## General Setup with NVidia and PyTorch

* Recent version of Python (3.10.5 is my current)
  * [Windows Setup Instructions](https://www.python.org/downloads/)
* [Cuda Install Version 11.6](https://developer.nvidia.com/cuda-11-6-2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
  * I had issues getting 11.7 running - suggest sticking with 11.6
* [PyTorch Setup](https://pytorch.org/)
  * Follow the PyTorch instructions to get the right version for your machine and for your version of Cuda
* Following the [Hugging Face Blog](#background-information) you also need to install some additional libraries
  * ``pip install diffusers==0.2.4 transformers scipy ftfy``
  * Also have to setup your token and get access to the model - read the blog post as once you have your environment setup getting access is just following those directions - specifically make sure you're looking at the v1.4 model as there are previous models beforehand
