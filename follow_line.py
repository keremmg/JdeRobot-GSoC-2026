import GUI
import HAL
import cv2
import numpy as np
last_error = 0
mevcut_hiz = 0.0  
while True:
    image = HAL.getImage()
    if image is None:
        continue
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    h, w, d = image.shape

    
    search_top = int(h * 0.50) 
    search_bot = int(h * 0.70) 
    image_roi = image[search_top:search_bot, 0:w]

    hsv = cv2.cvtColor(image_roi, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, np.array([0, 70, 50]), np.array([10, 255, 255]))
    mask2 = cv2.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
    mask = mask1 | mask2 

    M = cv2.moments(mask)

    if M['m00'] > 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        screen_center = w / 2
        error = screen_center - cx

        
        base_Kp = 0.008
        extra_Kp = abs(error) * 0.0004
        aktif_Kp = base_Kp + extra_Kp

        Kd = 0.060  

        error_diff = error - last_error

        
        angular_velocity = (error * aktif_Kp) + (error_diff * Kd)

       
        hedef_hiz = 5.0 - (abs(error) * 0.06)

        if hedef_hiz < 1.5:
            hedef_hiz = 1.5

       
        if hedef_hiz < mevcut_hiz:
            mevcut_hiz = mevcut_hiz + ((hedef_hiz - mevcut_hiz) * 0.8) 
        else:
            mevcut_hiz = mevcut_hiz + ((hedef_hiz - mevcut_hiz) * 0.1) 

        HAL.setV(mevcut_hiz) 
        HAL.setW(angular_velocity) 

        last_error = error

        cv2.circle(image, (cx, cy + search_top), 5, (0, 255, 0), -1)

        
        cv2.putText(image, f"Hiz: {mevcut_hiz:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        cv2.putText(image, f"Hata: {error:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        cv2.putText(image, f"Kp: {aktif_Kp:.4f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    else:
        mevcut_hiz = mevcut_hiz + ((0.0 - mevcut_hiz) * 0.8)
        HAL.setV(mevcut_hiz)
        HAL.setW(0.5)

        cv2.putText(image, f"Hiz: {mevcut_hiz:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.putText(image, "Cizgi Araniyor!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    GUI.showImage(image)