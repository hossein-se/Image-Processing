### Image Filtering And Recovery
To create the HighBoost filter,
 first, according to the formula, we create a Gaussian noise with the desired size on the original image, 
then we subtract it from the original image to actually reduce the low-pass filter to obtain the high-pass filter,
 and finally, we combine this obtained image with a We add the coefficient that must be greater than one to the original image.