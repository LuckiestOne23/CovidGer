# Programm meant to turn the PDFs available on LaGuS-MV into readable csv-Data.
# Please add below what incidence you are looking for.
# Author: Simon
# Edited: 02.04.2021
from pathlib import Path
import fitz
from os import remove as rem
import cv2
import numpy as np


def getFilename():
    pfad = Path('.')
    # Creating the PDF-Folder so no unwanted exception will be thrown
    Path(str(pfad) + '/pdf').mkdir(exist_ok=True)
    filepath = list(pfad.glob('pdf/*.pdf'))
    if len(filepath) == 0:
        raise RuntimeError("Keine PDF vorhanden.")
    for i in range(len(filepath)):
        filepath[i] = filepath[i].absolute()
    return filepath


def adequateCropping(kreis):
    dictionary = {"VG": ([2585, 2640], [2100, 2470])}
    tupel = dictionary[kreis]
    return tupel[0], tupel[1]


def getDateFromFilename(name):
    name = str(name).replace(".bericht.pdf", "")
    date = ""
    date += name[-2] + name[-1] + "." + name[-5] + name[-4] + "." + name[-10] + name[-9] + name[-8] + name[-7]
    return date


files = getFilename()
result = open("Inzidenz.txt", 'w')
result.write("Datum, Inzidenz\n")
# Allowed entries: VG (feel free to add more) ->MV won't work currently since the background is red
incidence = "VG"

for file in files:
    pdf_file = fitz.open(file)
    path = str(Path().absolute())
    Path(path + '/images').mkdir(exist_ok=True)
    try:
        rem('images/image.png')
    except FileNotFoundError:
        pass

    # Reading the location where to save the file
    location = path + '/images'

    # Getting image of first page
    for img_index, img in enumerate(pdf_file.getPageImageList(0)):
        xref = img[0]
        image = fitz.Pixmap(pdf_file, xref)
        image.writePNG("images/image.png")
    pdf_file.close()

    image = cv2.imread("images/image.png")
    cropping1, cropping2 = adequateCropping(incidence)
    cropped = image[cropping1[0]: cropping1[1], cropping2[0]: cropping2[1]]

    # To save the positions of found numbers
    positions = []

    # Since there can be 10 different numbers and it just compares one at a time
    for i in range(10):
        filename = "numbers/num" + str(i) + ".png"
        template = cv2.imread(filename)
        w, h = template.shape[:-1]
        res = cv2.matchTemplate(cropped, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            same = False
            for x in positions:
                if (abs(x[0][0] - pt[0]) <= 10 or abs(x[0][1] - pt[1]) <= 10) and x[1] == i:
                    same = True
                    break
            if not same:
                positions.append((pt, i))

    # Sorting so that first number is at position 1
    positions.sort()
    inzidenz = ""
    for i in positions:
        if i == positions[-1]:
            inzidenz = inzidenz + "." + str(i[1])
        else:
            inzidenz = inzidenz + str(i[1])

    result.write(getDateFromFilename(file) + "," + inzidenz + "\n")

result.close()
