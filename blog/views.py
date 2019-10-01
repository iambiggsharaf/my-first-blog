from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def stress(request):
    return render(request, 'blog/stress.html', {})

def binary(request):
    return render(request, 'blog/binary.html', {})

def form(request):
    return render(request, 'blog/form.html', {})

def generate(request):
    return render(request, 'blog/generate.html', {})

def typemaster(request):
    return render(request, 'blog/typemaster.html', {})

def geog(request):
    return render(request, 'blog/geog.html', {})
