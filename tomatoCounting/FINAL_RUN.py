# -*- coding: utf-8 -*-
from object_tracker import TomatoCounting
import cv2

video = 'data/videos/video2.mp4' # Video's path
log_filename = 'Camera 1' # log_filename
line_position = 0.05 # location of line caculated by height of image
line_angle = 0

# initialize
VC = TomatoCounting(log_filename, video=video, info=False,
                      dont_show=False,
                      tiny=True,
                      output='./result1.mp4',
                      detection_line=(line_position, line_angle),
                      score=0.4)

# render video
VC.run()