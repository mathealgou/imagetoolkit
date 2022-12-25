from .helpers import crop_image, saturate_image, vignette

def process_image(image, processess):
    unprocessed_image = image
    
    for process in processess:
        if process["action"] == "crop":
            image = crop_image(image, process)
        elif process["action"] == "saturate":
            image = saturate_image(image, process)
        elif process["action"] == "vignette":
            image = vignette(image, process)

    return image