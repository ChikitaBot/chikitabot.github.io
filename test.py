import os
import json

def list_files_in_directory(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_list.append(os.path.join(root, filename))
    return file_list

# Klasörünüzün yolunu belirtin
directory_path = './archive/fumo/imgs/'

# Dosyaları listeye alın
files = list_files_in_directory(directory_path)

liste = []

for file in files:
    data = {
        "link": "https://raw.githubusercontent.com/ChikitaBot/chikitabot.github.io/main/archive/fumo/imgs/" + file.split('/')[-1]
    }
    liste.append(data)

with open('archivefumo.json', 'w') as json_file:
    json.dump(liste, json_file)
