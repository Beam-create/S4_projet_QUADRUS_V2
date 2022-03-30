#!/usr/bin/env python3
import sys
import cv2
import numpy as np
import time
import imutils

def find_circles(frame, mask):

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    # Si au moins un contour a ete trouve
    if len(contours) > 0:
        #Trouve le contour le plus large, trouve son centroide et le plus petit cercle pouvant l'encercler
       
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)       #Finds center point
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Si son rayon est plus grand que 10 pixels
        if radius > 2:
            # Dessiner lecentroide et le cercle et MAJ de la liste
            cv2.circle(frame, (int(x), int(y)), int(radius),(255, 255, 0), 3)
            # cv2.circle(frame, center, 5, (0, 0, 0), -1)
            # cv2.putText(frame, str(center), )
            # cv2.putText(frame, f"%s, %s"%(center[0], center[1]), (center[0], center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)


    return center
