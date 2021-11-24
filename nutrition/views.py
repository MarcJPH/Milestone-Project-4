from django.shortcuts import render

# Create your views here.

def nutrition(request):
    """
    A view to return the pre and post workout nutrition page.
    """
    return render(request, 'nutrition/pre_post.html')