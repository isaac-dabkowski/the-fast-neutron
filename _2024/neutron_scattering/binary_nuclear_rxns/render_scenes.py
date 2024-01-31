from manim import *

import os
import subprocess
import argparse

from _2024.neutron_scattering import video_intro

OUTPUT_DIRECTORY = r"C:\Users\isaac\Documents\TheFastNeutron\videos\5_neutron_scattering\scenes"
SCENES_IN_ORDER = [
    # ("video_intro", "TitleCard"),
    # ("video_intro", "TableOfContents"),
    # ("binary_rxns", "BNRTitleCard"),
    ("binary_rxns", "BNR"),
    # ("binary_rxns", "ConservationEqns"),
    # ("binary_rxns", "ExothermicRxns"),
    # ("binary_rxns", "EndothermicRxns"),
    # ("binary_rxns", "KinematicThreshold"),
    # ("binary_rxns", "CoulombThreshold")
    # ("video_outro", "OutroCard")
]

# Argparse to allow for variable quality of render
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--quality', choices=["l", "m", "h", "k"])
parser.add_argument("-i", "--starting-index", type=int, default=0)
args = parser.parse_args()
qual = args.quality
if qual == "l":
    quality = "480p"
elif qual == "m":
    quality = "720p"
elif qual == "h":
    quality = "1080p"
elif qual == "k":
    quality = "2160p"

# Make directory if it hasnt been created yet
output_path = os.path.join(OUTPUT_DIRECTORY, quality)
command = f"mkdir -p {output_path}"
subprocess.run(command, shell=True)

# Render scenes in order and save to mp4 files in desired directory
for i, scene_tuple in enumerate(SCENES_IN_ORDER):
    filename = scene_tuple[0]
    scene_class = scene_tuple[1]
    output_file = f"{i + args.starting_index}_{scene_class}.mp4"
    output_path = os.path.join(OUTPUT_DIRECTORY, quality, output_file)
    command = f"manim -q{qual} -o {output_path} {filename}.py {scene_class}"
    subprocess.run(command, shell=True)
