from PIL import Image, ExifTags
img = Image.open("knowit/2022/12/img/abomasnow.jpg")
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

print(exif["GPSInfo"])