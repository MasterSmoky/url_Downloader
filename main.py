from pytube import YouTube
from pytube import Playlist
import os
import shutil

path = '%USERPROFILE%\\Music'

print("Por favor responda com 1 = unica ou 2 = playlist \n\n")
escolha = int(input("Você quer fazer o download de uma musica única ou de uma playlist ? :"))

def trocar_extensao_pasta(path):
    for arquivo in os.listdir(path):
        if arquivo.endswith(".mp4"):
            nome_antigo = os.path.join(path, arquivo)
            nome_novo = os.path.join(path, arquivo.replace(".mp4", ".mp3"))
            shutil.move(nome_antigo, nome_novo)

if escolha == 1:
    print("Você escolheu o download único!\n")
    url_un = YouTube(input("Insíra sua URL aqui: \n"))
    print(f'Você está fazendo o Download da música {url_un.title}\n')
    stream_unico = url_un.streams.filter(only_audio=True).first().download(path)
    print("Download concluido!")
    trocar_extensao_pasta(path)
elif escolha == 2:
    print("Você escolheu o download de uma playlist")
    url_pl = Playlist(input("Insíra sua URL de playlist aqui: "))
    print(f'Você está fazendo o Download da playlist {url_pl.title}\n')
    for video in url_pl.videos:
        video.streams.filter(only_audio=True).first().download(path)
    print("Download concluido!") 
    trocar_extensao_pasta(path)
