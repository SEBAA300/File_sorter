import os
import shutil

# Get username
username = os.getlogin()

# Directory
home_dir = "/home/{}".format(username)
sort_dir = "/home/{}/Downloads".format(username)

# Categorize files
img_ext = [".jpg",".png",".gif"]
doc_ext = [".txt",".pdf",".doc",".docx",".odt"]
music_ext = [".mp3"]
viedo_ext = [".mp4"]

# Create directory if not exist
if not os.path.exists("/home/{}".format(username) + "/Pictures"):
    os.makedirs(sort_dir + "/Image")
if not os.path.exists("/home/{}".format(username) + "/Documents"):
    os.makedirs(sort_dir + "/Docs")
if not os.path.exists("/home/{}".format(username) + "/Music"):
    os.makedirs(sort_dir + "/Music")
if not os.path.exists("/home/{}".format(username) + "/Videos"):
    os.makedirs(sort_dir + "/Videos")

for file in os.listdir(sort_dir):
    ext = os.path.splitext(file)[1].lower()

    if ext in img_ext:
        shutil.move(sort_dir + "/" + file, home_dir + "/Pictures")
    elif ext in doc_ext:
        shutil.move(sort_dir + "/" + file, home_dir + "/Documents")
    elif ext in music_ext:
        shutil.move(sort_dir + "/" + file, home_dir + "/Music")
    elif ext in viedo_ext:
        shutil.move(sort_dir + "/" + file, home_dir + "/Videos")