def crop_image(image, process):

    width, height = image.size
    
    final_width = process["width"]
    final_height = process["height"]
    
    x = 0
    y = 0
    
    # Middle school geometry goes brrrrrrrrrrrrrrrrr
    if process["origin"] == "top-left" or process["origin"] == None:
        x = final_width/2
        y = final_height/2
    elif process["origin"] == "top-right":
        x = width - final_width/2
        y = final_height/2
    elif process["origin"] == "bottom-left":
        x = final_width/2
        y = height - final_height/2
    elif process["origin"] == "bottom-right":
        x = width - final_width/2
        y = height - final_height/2
    elif process["origin"] == "center":
        x = width/2
        y = height/2
    else:        
        x = process[origin][x]
        y = process[origin][y]
    
    # Setting the points for cropped image
    left = x - final_width/2
    right = x + final_width/2
    top = y - final_height/2
    bottom = y + final_height/2
    
    # Cropped image of above dimension
    # (It will not change original image)
    cropped_image = image.crop((left, top, right, bottom))
    
    return cropped_image