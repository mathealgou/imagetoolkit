from .helpers import crop_image

def process_image(image, processess):
    unprocessed_image = image
    
    for process in processess:
        if process["action"] == "crop":
            image = crop_image(image, process)

    return image