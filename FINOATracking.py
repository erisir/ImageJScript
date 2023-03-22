from ij import IJ
from ij.measure import ResultsTable
from ij.gui import PointRoi  
from ij.gui import Roi  
from ij.plugin.frame import RoiManager
from ij.gui import Plot
#use GaussFit OnSpot to fit center of particles in frames and list
#in the table

startFrame = 1;


imp = IJ.getImage()  
stackSize = imp.getImageStackSize();
endFrame = stackSize;

stackSize =endFrame-startFrame+1;
       
prominence = 30;
pixelSize=47.5;
rectangle = 6;

imp = IJ.getImage()  
stackSize = imp.getImageStackSize();

imp.setSlice(startFrame);
IJ.run("GaussFit OnSpot", "shape=Circle fitmode=[Levenberg Marquard] rectangle="+str(rectangle)+" pixel="+str(pixelSize)+" max=1000 cpcf=1 base=100");
rsTable= ResultsTable.getResultsTable();

tempRs = rsTable.clone();
xc = rsTable.getValue(2, 0);
yc = rsTable.getValue(3, 0);



'rsTable [0,1,2,3,4] X,Y Xc, Yc,Sigma
for i in range(stackSize):  
	IJ.run("GaussFit OnSpot", "shape=Circle fitmode=[Levenberg Marquard] rectangle="+str(rectangle)+" pixel="+str(pixelSize)+" max=1000 cpcf=1 base=100");
	rsTable= ResultsTable.getResultsTable();
	if rsTable.columnExists(2):
    
		xc = rsTable.getValue(0,0);		 
		yc = rsTable.getValue(1,0);
		roi = PointRoi(xc, yc); 
        
		imp.setSlice(i)
		imp.setRoi(roi)
        
		tempRs.setValue(0,i,i);
		tempRs.setValue(1,i,rsTable.getValue(0,0));
		tempRs.setValue(2,i,rsTable.getValue(1,0));
		tempRs.setValue(3,i,rsTable.getValue(2,0));'X
		tempRs.setValue(4,i,rsTable.getValue(3,0));'Y
		tempRs.setValue(5,i,rsTable.getValue(4,0));        
        

plotx = Plot(imp.getTitle (),"frame","xPos (nm)");
ploty = Plot(imp.getTitle (),"frame","yPos (nm)");
x = tempRs.getColumnAsDoubles(3);'X
y = tempRs.getColumnAsDoubles(4);'Y
plotx.add("line",x);
ploty.add("line",y);
plotx.show();
ploty.show();
tempRs.show(imp.getTitle ());
		