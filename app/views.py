from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube

def downloader(request):
    if request.method == 'POST':
        video_url = request.POST['link']

        print(video_url)

        if video_url:
            try:
                yt = YouTube(video_url)
                yt.streams.get_highest_resolution().download()
                return render(request, 'index.html')
            except Exception as e:
                return HttpResponse("Error: " + str(e))
        else:
            return render(request, 'index.html')

    return render(request, 'index.html')
