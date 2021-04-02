# CovidGer
A small python script able to read PDF-files provided by LaGuS MV. Will return the incidence for each provided file. 


Hey guys, this is the first repository I've done so far. 

Its only purpose is to speed up the process of gathering data to map incidences of LaGuS MV. 


Right now it simply converts the PDF to an image, crops it and uses template matching to recognize the digits. 

Please put every PDF into the "pdf"-Folder. The "numbers"-Folder is just there for template matching and has to be copied.
The program takes round about 1.5 seconds per PDF so you might want to get yourself a cup of tea when converting great amounts.

So far the only district available is Vorpommern-Greifswald. Just crop the image with different values and test with cv2.imshow() until you get fitting values for other districts. Feel free to add your cropping-values. 

Hope you enjoy, have a nice day guys!





Hallo!
Der einzige Nutzen dieses Repository besteht darin, aus den PDF-Dateien des LaGuS txt-Dateien zu erstellen, die anschließend weiterverarbeitet werden können.

Derzeit gibt es ja einigen Trubel zu den Inzidenzwerten in Vorpommern-Greifswald und ich wollte meinen Teil dazu beitragen, dass viele Menschen einfach ihre eigenen 
Rechnungen anstellen können. 

Für jede PDF benötigt das Programm rund 1.5 Sekunden, folglich besteht bei großen Datenmengen die Zeit, einfach einmal eine Tasse Tee zu kochen.
Egal, welches Problem besteht, Tee hilft immer.

Aus der ersten Seite der PDFs wird ein Bild erstellt, dieses wird zugeschnitten und die einzelnen Zahlen danach über Template Matching zugeordnet. Um weitere Kreise hinzuzufügen, müssen die Cropping-Variablen angepasst werden. Diese können dann im Dictionary vermerkt werden. Ich freue mich, falls etwaige Schneide-Werte an mich herangetragen werden. 
Ich selbst sah für mich leider nicht die Notwendigkeit, diese einzufügen.
Viel Spaß mit dem Skript, ich hoffe, dass es die Arbeit etwas erleichtert.
Frohes Schaffen!
