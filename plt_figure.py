'''
plt.figure是用来创建一个图形对象的函数。在Matplotlib中，每当我们想要绘制一张图表时，
首先需要创建一个图形（Figure），你可以将它理解为一个空白的画布，用于后续的绘图操作。
'''
#figsize,dpi,facecolor 和 edgecolor,linewidth
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5), dpi=120, facecolor='lightgray', edgecolor='blue', linewidth=10, frameon=True)

plt.show()