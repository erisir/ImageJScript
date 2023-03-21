from ij import IJ
from ij.measure import ResultsTable
from ij.gui import PointRoi  
from ij.gui import Roi  
from ij.plugin.frame import RoiManager
from ij.gui import Plot
#use Find Maxima to find local maxima to count particles in frames and list
#in the table
startFrame = 1;
endFrame = 2000;

imp = IJ.getImage()  
stackSize = imp.getImageStackSize();

stackSize =endFrame-startFrame;

imp.setSlice(startFrame);
IJ.run("GaussFit OnSpot", "shape=Circle fitmode=[Levenberg Marquard] rectangle=6 pixel=47.5 max=1000 cpcf=1 base=100");
rsTable= ResultsTable.getResultsTable();
	
tempRs = rsTable.clone();
xc = rsTable.getValue(2, 0);
yc = rsTable.getValue(3, 0);
for i in range(stackSize):  
	imp.setSlice(i+startFrame)
	
	IJ.run("GaussFit OnSpot", "shape=Circle fitmode=[Levenberg Marquard] rectangle=7 pixel=47.5 max=1000 cpcf=1 base=100");
	rsTable= ResultsTable.getResultsTable();
	tempRs.addRow();
	for col in range(10):
		if rsTable.columnExists(col):
			tempRs.addValue(col,rsTable.getValue(col, 0));
	if rsTable.columnExists(9) and rsTable.getValue(9, 0)>10000:		
		xcT = rsTable.getValue(2, 0);
		ycT = rsTable.getValue(3, 0);
		roi = PointRoi(xcT/47.5, ycT/47.5); 	
		imp.setRoi(roi);
		xc = xcT; 
		yc = ycT;
		


plot = Plot("ROI1","frame","intensity");
a = tempRs.getColumnAsDoubles(3);
plot.add("line",a);
plot.show();
tempRs.show("Tracking Result");
		