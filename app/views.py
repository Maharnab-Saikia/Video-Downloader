from django.http import HttpResponse
from django.shortcuts import render, redirect
import youtube_dl


def downloader(request):

    if request.method == 'POST':
        video_url = request.POST['link']

        if video_url:
            ydl_opts = {'outtmp1': 'D:/'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')
			
    return render(request, 'index.html')