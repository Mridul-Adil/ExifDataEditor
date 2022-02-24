import subprocess
import pyautogui
import os

stream = os.popen('exiftool.exe bird.jpeg')

out = stream.read()
pyautogui.alert(out)

input_user_request ="y"

while input_user_request=='y':

    longitudeRef = input("enter longitude Ref(E/W): ")
    _GPSLongitudeRef="-GPSLongitudeRef="+longitudeRef

    lang = input("enter longitude: ")
    longitude = str(lang)
    _GPSLongitude="-GPSLongitude="+longitude

    latitudeRef = input("enter latitude Ref(N/S): ")
    _GPSLatitudeRef="-GPSLatitudeRef="+latitudeRef

    lang = input("enter latitude: ")
    latitude = str(lang)
    _GPSLatitude="-GPSLatitude="+latitude


    subprocess.run(['exiftool.exe', '-overwrite_original', _GPSLatitudeRef, _GPSLatitude, _GPSLongitudeRef, _GPSLongitude, 'bird.jpeg'])

    stream = os.popen('exiftool.exe bird.jpeg')
    out = stream.read()
    pyautogui.alert(out)

    input_user_request = input("Edit Again?:(y/n)")






