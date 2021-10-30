from model import World
import sys
import subprocess
import os
from shutil import copyfile

"""
Takes in experiment and trial to generate a png of each video frame 
experiment = 'teleport' or '3ball'
trial = trial index (remember 0 indexing)
"""

experiment = sys.argv[1]
trial = int(sys.argv[2])

w = World()
w.simulate(experiment = experiment, trial = trial, animate = True, save = True)	

copyfile("figures/frames/animation000.png", "figures/start_pic/Case" + str(trial) + ".png")
copyfile("figures/frames/animation301.png", "figures/end_pic/Case" + str(trial) + "_last.png")

ffmpeg_call_mp4 = "ffmpeg -framerate 50 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p videos/Case" + str(trial) + "_Stim.mp4"
subprocess.run(ffmpeg_call_mp4, shell=True)