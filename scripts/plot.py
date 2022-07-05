import sys,os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sys.path.append('./')
from scripts.logger import Logger

class Plot:
    def __init__(self) -> None:
       
        try:
            self.logger = Logger("plot.log").get_app_logger()
            self.logger.info(
                'Successfully Instantiated Preprocessing Class Object')
        except Exception:
            self.logger.exception(
                'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)


    def histogram(data,x,title):
        plt.figure(figsize=(8, 6))
        sns.histplot(data=data, x=x)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def barplot(data,x,y,title):
        plt.figure(figsize=(8, 6))
        sns.barplot(data=data, x=x, y=y)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def boxplot(data,x,y,title):
        plt.figure(figsize=(10, 10))
        sns.boxplot(data=data, x=x, y=y)
        plt.title(title, size=20)
        plt.yticks(fontsize=14)
        plt.show()

    def lineplot(data,x,y,title):
        plt.figure(figsize=(8, 6))
        sns.lineplot(data=data, x=x, y=y)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def scatterplot(data,x,y,title):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x=x, y=y)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
    def countplot(x,label):
        plt.figure(figsize=(8,6))
        sns.countplot(x,label=label)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def violinplot(x, y, hue, data,split, inner):
        sns.violinplot(x=x, y=y, hue=hue, data=data,split=split, inner=inner)
        plt.xticks(rotation=75, fontsize=14)
        # plt.yticks(fontsize=14)
        plt.show()
    def heatmap(data, title: str, cbar=False) -> None:
        plt.figure(figsize=(12, 7))
        sns.heatmap(data, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        plt.show()