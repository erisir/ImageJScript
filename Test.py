from ij import IJ
from ij.measure import ResultsTable
from ij.gui import PointRoi  
from ij.gui import Roi  
from ij.plugin.frame import RoiManager
IJ.run("GaussFit OnSpot", "shape=Circle fitmode=NelderMead rectangle=4 pixel=207 max=500 cpcf=1 base=100");   
rsTable= ResultsTable.getResultsTable();
col = rsTable.getColumn(0);
xc = col[0];
col = rsTable.getColumn(1);
yc = col[0];
roi = PointRoi(xc, yc); 
print(roi)
 