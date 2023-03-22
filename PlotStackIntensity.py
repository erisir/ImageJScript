from ij import IJ, ImagePlus  
from ij.plugin.filter import MaximumFinder 
from ij.gui import PointRoi  
from ij.gui import Roi  
from ij.plugin.frame import RoiManager
from ij.gui import Plot
from ij.plugin import ZAxisProfiler
from ij import WindowManager

# Grab the active image  
Roi_width = 6;
Roi_height=	6;
 
imp = IJ.getImage()  
imgWin = imp.getWindow();
IJ.run(imp,"Duplicate...", "duplicate range=1-50");
imp2 = IJ.getImage() ; 
IJ.run(imp2,"Grouped Z Project...", "projection=[Average Intensity] group=50");
imp2.close();
imp3 = IJ.getImage();
#IJ.run(imp3,"Find Maxima...", "prominence=150 strict exclude output=[Point Selection]");
IJ.run("Brightness/Contrast...");
IJ.run("Find Maxima...");
roi = imp3.getRoi();
imp3.close();
index = 0;
rm =  RoiManager.getRoiManager();
rm.reset();
for  p in roi:
	rm.add( Roi(p.x-Roi_width/2, p.y-Roi_height/2,Roi_width,Roi_height),index);
	index = index +1;
IJ.run("Plot Z-axis Profile");
plotWin = WindowManager.getActiveWindow();
plotWin.setBounds(0,0,plotWin.getWidth(),plotWin.getHeight());
imgWin.setBounds(plotWin.getWidth(),0,imgWin.getWidth(),imgWin.getHeight());
rm.setBounds(plotWin.getWidth()+imgWin.getWidth(),0,rm.getWidth(),rm.getHeight());
if	1==0:
	rstable = rm.multiMeasure(imp)
	plot = Plot("ROI1","frame","intensity");
	a = rstable.getColumnAsDoubles(0);
	b = rstable.getColumnAsDoubles(1);
	plot.add("line",b);
	plot.show();

 

