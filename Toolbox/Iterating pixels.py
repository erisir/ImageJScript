from ij import IJ  
from sys.float_info import max as MAX_FLOAT  
  
# Grab the active image  
imp = IJ.getImage()  
  
# Grab the image processor converted to float values  
# to avoid problems with bytes  
ip = imp.getProcessor().convertToFloat() # as a copy  
# The pixels points to an array of floats  
pixels = ip.getPixels()  
  
print "Image is", imp.title, "of type", imp.type  
  
# Obtain the minimum pixel value  
  
# Method 1: the for loop, C style  
minimum = MAX_FLOAT  
for i in xrange(len(pixels)):  
  if pixels[i] < minimum:  
    minimum = pixels[i]  
  
print "1. Minimum is:", minimum  
  
# Method 2: iterate pixels as a list  
minimum = MAX_FLOAT  
for pix in pixels:  
  if pix < minimum:  
    minimum = pix  
  
print "2. Minimum is:", minimum  
  
# Method 3: apply the built-in min function  
# to the first pair of pixels,  
# and then to the result of that and the next pixel, etc.  
minimum = reduce(min, pixels)  
  
print "3. Minimum is:", minimum  