def shapeVerification (contour) :
    perimeter = cv2.arcLength(contour,True)
    area = cv2.contourArea(contour)
    sides = len(countour)

    if sides == 4:
        # for rectangles, the aspect ratio is important. Get rid of thin lines
        x,y,w,h = cv.boundingRect(cnt)
        aspect_ratio = float(w)/h
        if aspect_ratio < 0.6 :
            return False
        else :
            return True 
    elif ( sides == 5 or sides(countour) == 6 ):
        # for pentagon compute area of a regular pentagon
        ideal_area = perimeter**2 / (4*math.tan( math.pi / sides) )
        area_Ratio = ideal_area / area
        if (area_Ratio <= 1.2 and area_Ratio >= 0.8 ) :
            return True
        else :
            return False
    elif (sides > 6) :
        ideal_area = perimeter **2 / (math.pi * 4)
        if (area_Ratio <= 1.2 and area_Ratio >= 0.8 ) :
            return True
        else :
            return False
    else :
        return False
