"""This Script is setup to run on a smaller GPU than the Stable Diffusion 10GB requirements
thus there is some commented code that might be helpful for others running larger GPU's over 10GB
Just wanted a way to quickly run some prompts via CMD
"""
import dataclasses
from random import seed
import string
from diffusers import StableDiffusionPipeline
import torch
from torch import autocast
import os
from PIL import Image
from dataclasses import dataclass
import json
import nvidia_smi

## To Store the Run Data for if we want to revisit it

@dataclass
class StableData:
    stPrompt:string
    stSeed:int
    iteration:int
    guideScale:int
    imageCount:int
    xDim:int
    yDim:int
    modelID:string
    imgName:string
    imgPath:string

## Help with serialization of json and dataclasses
class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            return super().default(o)

#class for image grid
def image_grid(imgs,rows,cols):
    assert len(imgs) == rows*cols
    w,h=imgs[0].size
    grid = Image.new('RGB',size=(cols*w,rows*h))
    grid_w, grid_h = grid.size
    for i,img in enumerate(imgs):
        grid.paste(img,box=(i%cols*w,i//cols*h))
    return grid

#check if you have a GPU over 10GB
def BIGGPU():
    nvidia_smi.nvmlInit()
    handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
    info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
    #print(info.used)
    #print(info.total)
    #print(info.free)
    #print(info.used/info.total)
    if(info.free > 1000000000):
        return True
    else:
        return False

## file Setup Stuff
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path,"Images")
model_id = "CompVis/stable-diffusion-v1-4"
device ="cuda"

## https://huggingface.co/docs/hub/security-tokens
YOUR_TOKEN = "GET_YOUR_TOKEN_AT_HUGGING_FACE"

TenGB=BIGGPU()

## Set this to keep me from going overboard feel free to change!
numImages = int(input("Enter the number of images you want to generate: "))
if(numImages>20 or numImages<1):
    print("You can generate up to 20 images at a time, resetting to 4")
    numImages = 4

## for images larger than 512 you will have to do some additional work

#pixelWidth = int (input("Enter the width of the image in pixels: "))
#if(pixelWidth>1920 or pixelWidth<512):
#    print("You can generate images up to 1920x1080 pixels, resetting to 512")
pixelWidth = 512
prompt = input("Enter your diffusion prompt: ")
#multiplePrompt = [prompt]*numImages
numRuns = int(input("Enter the number of iterations:"))
if(numRuns < 1):
    print("Need to be greater than 1:fixed this for you... idiot! 51")
    numRuns = 51
guideScale = float(input("Guidance Scale, suggested between 5-20:"))
if(guideScale < 5):
    guideScale = 5
    print("Guide scale was too low, set it to 5")

seedNumber = 1024
seedNumber = int(input("Enter the seed number:"))

print("...Running Stable Diffusion... just a few seconds...")

# Here's where I drop down to meet the smaller GPU according to the Blog
#pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=YOUR_TOKEN)
generatorT = torch.Generator(device).manual_seed(seedNumber)
if(TenGB):
    pipe = StableDiffusionPipeline.from_pretrained(model_id,use_auth_token=YOUR_TOKEN)
else:
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16",use_auth_token=YOUR_TOKEN)

pipe.to(device)


## Crimes from: https://www.programcreek.com/python/?CodeExample=clean+filename

def cleanFilename(sourcestring,  removestring =" %:/,.\\[]<>*?"):
    """Clean a string by removing selected characters.

    Creates a legal and 'clean' source string from a string by removing some 
    clutter and  characters not allowed in filenames.
    A default set is given but the user can override the default string.

    Args:
        | sourcestring (string): the string to be cleaned.
        | removestring (string): remove all these characters from the string (optional).

    Returns:
        | (string): A cleaned-up string.

    Raises:
        | No exception is raised.
    """
    #remove the undesireable characters
    return ''.join([c for c in sourcestring if c not in removestring])

##Loop code to process individual images by stepping up the random number by 1 iteration each time.
##Was working on the multiple images back but didn't have enough GPU memory on this laptop to run it
for x in range(0,numImages):
    print("Starting loop number: " + str(x))
    cut_imageName = cleanFilename(prompt)[:24]
    imageName = cut_imageName+str(x)+str(".png")
    textName = cut_imageName+str(".txt")
    fullImagePath = os.path.join(image_path, imageName)
    fullTextPath = os.path.join(image_path,textName)
    dataP = StableData(prompt, seedNumber+x, numRuns, guideScale, numImages,pixelWidth, 512,model_id, cut_imageName, fullImagePath)

    with autocast(device):
#    image = pipe(prompt, guidance_scale=guideScale, num_inference_steps=numRuns,generator=generatorT)["sample"][0]
        image = pipe(prompt, height=512,width=pixelWidth,guidance_scale=guideScale, num_inference_steps=numRuns, generator=generatorT)["sample"][0]

#grid = image_grid(image,rows=1,cols=numImages)
#grid.save(fullImagePath)

    image.save(fullImagePath)

    img=Image.open(fullImagePath)
    img.show()
    print(image)

json_content = json.dumps(dataP, cls=EnhancedJSONEncoder)
file = open(fullTextPath,"w")
file.write(json_content)
file.close()