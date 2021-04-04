# CovidGer
A small python script able to read PDF-files provided by LAGuS MV. Will return the incidence for each provided file. 


The three Python-Files are able to download and read pdf-Files from LAGuS MV and plot the difference between the incidence provided by LAGuS and the RKI.
A huge thank to @dammhannes for providing the plotting.py! 

Please put every PDF into the "pdf"-Folder if adding them manually. The "numbers"-Folder is just there for template matching and has to be copied.
The program takes round about 1.5 seconds per PDF so you might want to get yourself a cup of tea when converting great amounts.
scraping.py, plotting.py and pdfRead.py have to be in the same folder for it to work. Run scraping.py first and wait for it to finish if done manually.
When starting plotting.py you will be asked whether you just want the program to plot based on the current data of "Inzidenz.txt" or get all incidence-values from January first of 2021 until today. 

So far the only district that can be read is Vorpommern-Greifswald. Just crop the image with different values and test with cv2.imshow() until you get fitting values for other districts. Feel free to add your cropping-values. 

Hope you enjoy, have a nice day guys!





Hallo!
Der einzige Nutzen dieses Repository besteht darin, aus den PDF-Dateien des LaGuS txt-Dateien zu erstellen, die anschließend weiterverarbeitet werden können.

Derzeit gibt es ja einigen Trubel zu den Inzidenzwerten in Vorpommern-Greifswald und ich wollte meinen Teil dazu beitragen, dass viele Menschen einfach ihre eigenen Rechnungen anstellen können. Durch ein Starten der Datei "plotting.py" werden sämtliche PDFs des LAGuS MV ab dem 1. Januar 2021 heruntergeladen und die Inzidenz von Vorpommern-Greifswald daraus ermittelt. Abschließend wird diese mit der berechneten RKI-Inzidenz inklusive Nachmeldungen graphisch verglichen.
Die Ordnerstruktur muss beibehalten werden. Bitte einfach den gesamten Ordner "Covid-Zahlen" kopieren und die "plotting.py"-Datei ausführen.

Für jede PDF benötigt das Programm rund 1.5 Sekunden, folglich besteht bei großen Datenmengen die Zeit, einfach einmal eine Tasse Tee zu kochen.
Egal, welches Problem besteht, Tee hilft immer.

Aus der ersten Seite der PDFs wird ein Bild erstellt, dieses wird zugeschnitten und die einzelnen Zahlen danach über Template Matching zugeordnet. Um weitere Kreise hinzuzufügen, müssen die Cropping-Variablen angepasst werden. Diese können dann im Dictionary vermerkt werden. Ich freue mich, falls etwaige Schneide-Werte an mich herangetragen werden. 

Nun ist auch ein PDF-Downloader vorhanden, welcher automatisch sämtliche verfügbaren Covid-Lageberichte herunterlädt, die nicht in Zip-Archiven abgespeichert sind. Bitte diesen zuerst ausführen und dann die pdfRead-Datei starten. Damit es reibungslos funktioniert, müssen beide Python-Dateien im gleichen Ordner liegen.



Viel Spaß mit dem Skript, ich hoffe, dass es die Arbeit etwas erleichtert.
Frohes Schaffen!
