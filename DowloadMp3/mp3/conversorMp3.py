from pytube import YouTube
import moviepy.editor as mp
import re
import os


#digite o link do video e o local que deseja salvar o mp3#
print ("****************************************************")
print("Bem vindo ao convertor Mp3")
print("atençao ao colocar o caminho do diretorio")
print ("****************************************************")
link = input("Digite o link do video que deseja baixar:  ")
print ("****************************************************")
print ("link do donwload")
print(link)
print ("****************************************************")
path = input("Digite o diretorio que deseja salvar o video :")
print ("caminho do donwload")
print(path)
print ("****************************************************")


yt = YouTube(link)

# começa o Download #

print ("****************************************************")
print("Baixando......")
print('Convertendo arquivo.....')
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo!!!")
print("Finalizando............")
print ("****************************************************")
print('Sucesso')


# convertendo arquivo #

print('Convertendo arquivo.....')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)






