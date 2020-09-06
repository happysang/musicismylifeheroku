from django.shortcuts import render, get_object_or_404, redirect
from recommendation.models  import RecommendInformation
from user.models import CustomUser

def r_create(request) :
    if request.method == 'POST' and request.session.get('user', False) :
        post_title = request.POST['post_title']
        title = request.POST['title']
        artist = request.POST['artist']
        genre = request.POST['genre']
        reason = request.POST['reason']
        user = get_object_or_404(CustomUser, username=request.session['user'])

        recommend = RecommendInformation(
            post_title = post_title,
            title = title,
            artist = artist,
            genre = genre,
            user = user,
            reason = reason
            )
        recommend.save()
        return redirect('r_read')
    else:
        return render(request, 'recommendation/create.html')

def r_read(request) :
    recommends = RecommendInformation.objects.all()
    context = {'recommends': recommends}
    return render(request,'recommendation/read.html',context)

def r_read_one(request, pk) :
    recommend = get_object_or_404(RecommendInformation, pk = pk)
    context = { 'recommend': recommend }
    return render(request, 'recommendation/read_one.html',context)

def r_update(request, pk) :
    if  request.method == 'POST':
        post_title = request.POST['post_title']
        title = request.POST['title']
        artist = request.POST['artist']
        genre = request.POST['genre']
        reason = request.POST['reason']

        recommend = RecommendInformation.objects.get(pk=pk)

        recommend.post_title = post_title
        recommend.title = title
        recommend.artist = artist
        recommend.genre = genre
        recommend.reason = reason
        recommend.save()
        return redirect('r_read')
    else:
        recommend = get_object_or_404(RecommendInformation, pk = pk)
        context = {"recommend" : recommend}
        return render(request, 'recommendation/update.html', context)

def r_delete(request,pk):
    recommend = RecommendInformation.objects.get(pk=pk)
    recommend.delete()
    return redirect('r_read')