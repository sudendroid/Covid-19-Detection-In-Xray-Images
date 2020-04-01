# This script is from pyimagesearch blog
# https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/

# This script is used to extract covid xray images from collection of xray images by Dr. Joseph Cohen
# https://github.com/ieee8023/covid-chestxray-dataset


import pandas as pd
import shutil
import os

df = pd.read_csv('covid-chestxray-dataset-master/metadata.csv')

for (i, row) in df.iterrows():
	if row["finding"] != "COVID-19" or row["view"] != "PA":
		continue

	imagePath = os.path.sep.join(["covid-chestxray-dataset-master","images",
		row["filename"]])

	if not os.path.exists(imagePath):
		continue

	filename = row["filename"].split(os.path.sep)[-1]
	outputPath = os.path.sep.join(["dataset", "covid", filename])

	shutil.copy2(imagePath, outputPath)

