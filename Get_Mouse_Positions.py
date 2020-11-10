# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:19:48 2020

@author: Riemann Lee
"""
import os, time
import numpy as np
import pyautogui as pag
Trajectory = []
try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  # get our screen size
        x, y = pag.position()  # Get the coordinates of moving mouse
        Trajectory.append([x,y])
        # Print the coordinate of mouse on the console
        print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y))  
 
        time.sleep(0.5)  # print the point of the screen every half second
        os.system('cls')  # clear the screen
except KeyboardInterrupt:
    print('end')
    
"""
Now we need to  further process the obtained data, namely,
calculation from mouse tragectory to the input data. I have:
    Screen Size: (1920, 1080)
    Upper Left Corner: [502, 193]
    Bottom Left Corner: [502, 917]
    Bottom Right Corner: [1467, 917]
    Upper Right Corner: [1467, 193]
    
The parameters list here is dependent on personal computer screen's
size, and I use these parameters to change test dataset.
"""
Screen_Size =  [1920, 1080]
Upper_Left_Corner = [502, 193]
Bottom_Right_Corner = [1467, 917]
Window_Size = [Bottom_Right_Corner[0] - Upper_Left_Corner[0], Bottom_Right_Corner[1] - Upper_Left_Corner[1]]

Scaling_Factor = [ 800 / Window_Size[0], 600 / Window_Size[1] ]
# np.save('Trajectory.npy', Trajectory)
# struggle with the dims of the Trajectory
