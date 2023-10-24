from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts':posts})


def post(request, pk):
    # if request.method == "POST":
        # title = request.POST['title']
        # content = request.POST['content']
        # author = request.user
        # new_post = Posts(title=title, content=content, author=author)
        # new_post.save()
    
    posts = Posts.objects.get(id=pk)
    return render(request,'post.html', {'posts':posts})
    