# CovidGer
A small python script able to read PDF-files provided by LaGuS MV. Will return the incidence for each provided file. 


Hey guys, this is the first repository I've done so far. 

Its only purpose is to speed up the process of gathering data to map incidences of LaGuS MV. 


Right now it simply converts the PDF to an image, crops it and uses template matching to recognize the digits. 

Please put every PDF into the "pdfs" Folder. The "numbers"-Folder is just there for template matching and has to be copied.
The program takes round about 1.5 seconds per PDF so you might want to get yourself a cup of tea when converting great amounts.

So far the only district available is Vorpommern-Greifswald. Just crop the image with different values and test with cv2.imshow() until you get fitting values for other districts. Feel free to add your cropping-values. 

Hope you enjoy, have a nice day guys!
