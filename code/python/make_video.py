import model as m
from model import World
import subprocess
import os
from shutil import copyfile


experiment = "3ball"
trials = m.load_trials("3ball_trials.json")


for i in range(len(trials)):
	trial = trials[i]
	w = World()
	w.simulate(experiment = experiment, trial = trial, animate = True, save = True)	
	# copyfile("figures/frames/animation000.png", "figures/start_pic/exp1/Case" + str(i) + ".png")
	# copyfile("figures/frames/animation061.png", "figures/end_pic/exp1/Case" + str(i) + "_last.png")

	# copyfile("figures/frames/animation000.png", "figures/start_pic/exp1/Case" + str(i) + "h.png")
	# copyfile("figures/frames/animation061.png", "figures/end_pic/exp1/Case" + str(i) + "_last.png")
	# copyfile("figures/frames/animation051.png", "figures/end_pic/" + "inst_last.png")
	copyfile("figures/frames/animation000.png", "figures/start_pic/exp1/Case" + str(i) + ".png")
	copyfile("figures/frames/animation300.png", "figures/end_pic/exp1/Case" + str(i) + "_last.png")

	# # ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p Casetest" + ".mp4"

	# ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p video/Case" + str(i) + "_h.mp4"

	# copyfile("figures/frames/animation000.png", "figures/end_pic/Case2h" + ".png")
	# copyfile("figures/frames/animation051.png", "figures/end_pic/Case2h" + "_last.png")

	# ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p exp1/Case"+ str(i) + ".mp4"
	# ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p exp1/Case"+ str(i) + "h.mp4"

	# ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p video/Case" + str(i) + ".mp4"

	# ffmpeg_call_webm = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png  -c:v libvpx-vp9 -b:v 2M -crf 10 -pix_fmt yuv420p video/Case11" + str(i) + ".webm"

	ffmpeg_call_mp4 = "ffmpeg -framerate 20 -i figures/frames/animation%3d.png -c:v libx264 -profile:v high -crf 10 -pix_fmt yuv420p videos/Case" + str(i) + "_Stim.mp4"

	subprocess.run(ffmpeg_call_mp4, shell=True)
	# subprocess.run(ffmpeg_call_webm, shell=True)

	# subprocess.run("rm figures/frames/*", shell=True)

	# frames = os.listdir("figures/frames")
	# for fr in frames:
	# 	os.remove("figures/frames/" + fr)





