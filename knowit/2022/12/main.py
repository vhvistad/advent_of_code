from os.path import dirname, abspath, join
from os import listdir
from GPSPhoto import gpsphoto
import matplotlib.pyplot as plt

img_path = join(dirname(abspath(__file__)), 'img')

for img in listdir(img_path):
    data = gpsphoto.getGPSData(join(img_path, img))
    plt.scatter(x=data['Longitude'], y=data['Latitude'])

plt.show()