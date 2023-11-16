from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Song
from functions.serializers import SongSerializer
from functions.forms import SongForm

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_list')  # 上传成功后重定向到音乐列表页面
    else:
        form = SongForm()
    return render(request, 'musicapp/upload_song.html', {'form': form})






def music_list(request):
    songs = Song.objects.all()
    return render(request, 'musicapp/music_list.html', {'songs': songs})
