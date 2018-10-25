from django.http import Http404
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post, Comment


def post_list(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/post_list.html', context)


def post_single(request, post_id: int):
    try:
        # Prefetch the comments and retrieve the given post
        post = Post.objects.prefetch_related('comments').get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404(f'Post #{post_id} not found.')

    # create a base empty comment to put user input into;
    # this base comment will have has parent post the current viewing post.
    comment_instance = Comment(post=post)

    # we create the form from the HTTP POST data or pass None if no POST data;
    # and we pass our empty comment instance to be populated.
    comment_form = CommentForm(request.POST or None, instance=comment_instance)

    # check if the form is valid
    if comment_form.is_valid():
        # commit the changes if the form is valid
        comment_form.save(True)

        # and redirect the user back to the single post view
        return redirect('post-single', post_id=post_id)

    # pass the form to render
    context = {'post': post, 'comment_form': comment_form}
    return render(request, 'blog/post_single.html', context)
