from PIL import Image, ImageEnhance

def saturate_image(image: Image, process):
    # change the saturation of the image
	saturation = process["saturation"]

	enhancer = ImageEnhance.Color(image)
 
	return enhancer.enhance(saturation)