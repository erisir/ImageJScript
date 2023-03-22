from ij import IJ


imp = IJ.getImage()  
stackSize = imp.getImageStackSize();
for i in range(stackSize-1):     
	imp.setSlice(i)
	IJ.run("Find Maxima...", "prominence=20 output=Count");
	