from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blogpost, Comment
# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogpost(request, id):
    post = get_object_or_404(Blogpost, post_id=id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")

        if name and text:
            Comment.objects.create(
                post=post,
                name=name,
                text=text
            )
            return redirect(f"/blog/blogpost/{id}")

    return render(request, 'blog/blogpost.html', {
        'post': post,
        'comments': comments
    })

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.post_id
    if request.method == "POST":
        comment.delete()
        return redirect(f"/blog/blogpost/{post_id}")
    return render(request, "blog/confirm_delete.html", {"comment": comment})

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()
    return redirect(request.META.get('HTTP_REFERER'))