//

//Show all ROIs and count the number of ROIs
roiManager("Show All");
numROIs=roiManager("count");

//Ask user pixel size and frame interval
Dialog.create("Info");
Dialog.addNumber("Pixel Size (nm)",73);
Dialog.addNumber("Frame Interval (ms)",200);
Dialog.show()
//Get pixel size in nm
p=Dialog.getNumber();
//Get frame interval in seconds
dt=Dialog.getNumber()/1000;
tracks=newArray(0);
segs=newArray(0);
distance=newArray(0);
time=newArray(0);
speed=newArray(0);
dis_tot=newArray(numROIs);
time_tot=newArray(numROIs);
v_ave=newArray(numROIs);
n_seg=newArray(numROIs);
track_tot=Array.getSequence(numROIs+1);
track_tot=Array.deleteIndex(track_tot,0);

newImage("K.tif", "8-bit black", 400, 400, 1);

//Loop the following code for the number of ROIs
for(r=0;r<numROIs;r++){
	
	//Select the ROI designated by the current value of r. ROIs start from 0
	roiManager("Select",r);
	Roi.getCoordinates(xpoints,ypoints);
	n=lengthOf(xpoints);
	//Segment analysis
	trackID=newArray(n-1);
	Array.fill(trackID,r+1);
	segID=Array.getSequence(n);
	segID=Array.deleteIndex(segID,0);
	L=newArray(n-1);
	T=newArray(n-1);
	v=newArray(n-1);
	for(i=0;i<n-1;i++){
		L[i]=p*(xpoints[i+1]-xpoints[i]);
		T[i]=dt*(ypoints[i+1]-ypoints[i]);
		v[i]=L[i]/T[i];
		}
	tracks=Array.concat(tracks,trackID);
	segs=Array.concat(segs,segID);
	distance=Array.concat(distance,L);
	time=Array.concat(time,T);
	speed=Array.concat(speed,v);
	//Average entire trace
	n_seg[r]=n-1;
	dis_tot[r]=p*(xpoints[n-1]-xpoints[0]);
	time_tot[r]=dt*(ypoints[n-1]-ypoints[0]);
	v_ave[r]=dis_tot[r]/time_tot[r];
	}
Table.create("Segmented Velocity");
Table.setColumn("Track",tracks);
Table.setColumn("Segment",segs);
Table.setColumn("Distance(nm)",distance);
Table.setColumn("Duration(s)",time);
Table.setColumn("Velocity(nm/s)",speed);

Table.create("Averaged Velocity");
Table.setColumn("Track",track_tot);
Table.setColumn("Segments",n_seg);
Table.setColumn("Total Distance(nm)",dis_tot);
Table.setColumn("Total Duration(s)",time_tot);
Table.setColumn("Average Velocity(nm/s)",v_ave);

selectWindow("K.tif");
close();