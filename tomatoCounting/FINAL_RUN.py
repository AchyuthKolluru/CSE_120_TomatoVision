# -*- coding: utf-8 -*-
from object_tracker import TomatoCounting
import cv2

video = 'data/videos/PerfectVid.mp4' # Video's path
log_filename = 'Camera 1' # log_filename
line_position = 0.05 # location of line caculated by height of image
line_angle = 0
# initialize
VC = TomatoCounting(log_filename, video=video, info=False,
                      dont_show=False,
                      tiny=True,
                      detection_line=(line_position, line_angle),
                      score=0.45,)

# render video
VC.run()