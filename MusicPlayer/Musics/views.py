import datetime
from django.shortcuts import render
from .models import Music  # Import the Music model from the appropriate module
from django.views.generic import TemplateView
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import shutil
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        for music_file in os.listdir('static'):
            if music_file.endswith('.mp3'):
                file_path = os.path.join('static', music_file)
                audio = MP3(file_path)
                id3_info = ID3(file_path)

                file_name = os.path.basename(file_path)

                # Obter a duração da música
                duration = audio.info.length

                # Obter o tipo de música
                genre = id3_info['TCON'].text[0] if 'TCON' in id3_info else None

                # Obter o álbum da música
                album = id3_info['TALB'].text[0] if 'TALB' in id3_info else None

                # Obter o artista da música
                artist = id3_info['TPE1'].text[0] if 'TPE1' in id3_info else None

                # Converter a duração para o formato 00:00:00
                duration_formatted = str(datetime.timedelta(seconds=int(duration)))

                # Copiar o arquivo de áudio para a pasta 'audios'
                new_file_path = os.path.join('media', 'audios', file_name)
                shutil.copy(file_path, new_file_path)

                music = Music(title=file_name, artist=artist, album=album, genre=genre, audio=new_file_path, duration=duration_formatted)
                music.save()
        musics = Music.objects.all()
        context = {'musics': musics}
        return render(request, self.template_name, context)

import os  # Import the os module to access file system operations

class musicView(TemplateView):
    template_name = 'music.html'

    def get(self, request, pk):
        
        musics = Music.objects.all()
        music = Music.objects.get(pk=pk)
        print(music.audio.url)
        context = {'music': music,
                   'musics': musics}
        return render(request, self.template_name, context)