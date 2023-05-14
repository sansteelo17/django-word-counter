from django.shortcuts import render

# Create your views here.

def index(request):
    name = 'Patrick'
    return render(request, 'index.html', {'name': name})

def counter(request):
    words = request.POST['words']
    word_count = len(words.split())
    return render(request, 'counter.html', {'count': word_count})
