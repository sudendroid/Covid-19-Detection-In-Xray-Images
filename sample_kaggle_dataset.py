# this script is from pyimagesearch blog
# https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/
# This script is used to extract normal xray images from kaggle dataset
# https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

from imutils import paths
import random
import shutil
import os

basePath = os.path.sep.join(['chest_xray', "train", "NORMAL"])
imagePaths = list(paths.list_images(basePath))

random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:89]

for (i, imagePath) in enumerate(imagePaths):
	filename = imagePath.split(os.path.sep)[-1]
	outputPath = os.path.sep.join(['dataset', 'normal', filename])
	shutil.copy2(imagePath, outputPath)







