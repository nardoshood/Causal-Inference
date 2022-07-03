import matplotlib.pyplot as plt
import seaborn as sns

from scripts.logger import Logger


class Visualize:
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
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=data, x=x, y=y)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
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
