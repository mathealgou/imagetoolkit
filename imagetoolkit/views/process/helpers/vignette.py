import cv2	
import numpy 
from PIL import Image

def vignette(image, process):
    image = numpy.array(image)
    
    height, width = image.shape[:2]
    
    level = 4
    
    x_resultant_kernel = cv2.getGaussianKernel(width, width/level)
    y_resultant_kernel = cv2.getGaussianKernel(height, height/level)

    kernel = y_resultant_kernel * x_resultant_kernel.T
    mask = kernel / kernel.max()

    image_vignette = numpy.copy(image)

    for i in range(3):
        image_vignette[:,:,i] = image_vignette[:,:,i] * mask

    return Image.fromarray(image_vignette)