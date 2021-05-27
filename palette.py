## Palette 생성
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

gg_raw = [
    (255,108,145),
    (222,140,0),
    (157,167,0),
    (0,186,56),
    (0,193,169),
    (0,180,240),
    (159,140,255),
    (245,100,227),
    (127,201,127),
    (190,174,212),
    (253,192,134),
    (255,255,153),
    (56,108,176)]

gg_palette = np.array(gg_raw)/255

raw_dark_palette = [
    (10, 132, 255), # Blue
    (255, 159, 10), # Orange
    (48, 209, 88),  # Green
    (255, 69, 58),  # Red
    (191, 90, 242), # Purple
    (94, 92, 230),  # Indigo
    (255, 55, 95),  # Pink
    (100, 210, 255),# Teal
    (255, 214, 10)  # Yellow
]

dark_palette = np.array(raw_dark_palette)/255

## 검은색 배경 생성
from cycler import cycler

gray_color = np.array((44, 44, 46))/255
mpl.rcParams['axes.prop_cycle'] = cycler('color',dark_palette)
mpl.rcParams['figure.facecolor']  = gray_color
mpl.rcParams['figure.edgecolor']  = gray_color
mpl.rcParams['axes.facecolor'] = gray_color

white_color = np.array((229, 229, 234))/255
mpl.rcParams['text.color'] = white_color
mpl.rcParams['axes.labelcolor'] = white_color
mpl.rcParams['axes.edgecolor'] = white_color
mpl.rcParams['xtick.color'] = white_color
mpl.rcParams['ytick.color'] = white_color

mpl.rcParams['figure.dpi'] = 150

mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
