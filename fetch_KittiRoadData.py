#!/usr/bin/env python3
import os.path

if not os.path.isdir("data/data_road"):
    print("KITTI road data need to be fetched...");

    url = "https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/advanced_deep_learning/data_road.zip"
    zipName = os.path.basename(url)
    os.chdir("data");
    os.system("curl -o " + zipName + " " + url)
    os.system("unzip -x " + zipName)
else:
    print("KITTI road data found.");
