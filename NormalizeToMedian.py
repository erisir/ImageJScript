from ij import IJ, ImagePlus  
from ij.plugin.filter import MaximumFinder 
from ij.gui import PointRoi  
from ij.gui import Roi  
from ij.plugin.frame import RoiManager
from ij.gui import Plot
from ij.plugin import ZAxisProfiler
from ij import WindowManager
from ij.measure import ResultsTable

 
imp = IJ.getImage()  
stackSize = imp.getImageStackSize();
for i in range(stackSize+1):    
	imp.setSlice(i)
	IJ.run("Measure");
	rsTable= ResultsTable.getResultsTable();
	maxGrayValue = rsTable.getValue("Median",i);
	IJ.run("Divide...", "value="+str(maxGrayValue)+" slice"); 
