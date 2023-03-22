from ij import IJ
#use Find Maxima to find local maxima to count particles in frames and list
#in the table

prominence = 30;

imp = IJ.getImage()  
stackSize = imp.getImageStackSize();
for i in range(stackSize-1):     
	imp.setSlice(i)
	IJ.run("Find Maxima...", "prominence="+str(prominence)+" output=Count");	