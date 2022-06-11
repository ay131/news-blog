from django.shortcuts import render,redirect
from .models import post
from django.http import HttpResponse
from django.conf import settings
from .forms import post_form

# Create your views here.
def all_posts(request):
    all_posts=post.objects.all()

    context={
        'all_posts':all_posts,
        'BASE_DIR':settings.BASE_DIR,
    }

    return render(request,'all_posts.html',context)




def posts(request,id):
    re_posts=post.objects.get(id=id)
    context={
        're_posts':re_posts,
    }
    return render(request,'detail.html',context)



def create_post(request):
    if request.method=='POST':
        form=post_form(request.POST)
        if form.is_valid() :
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')

    else:
        form=post_form()

    context={
        'form':form,
    }
    return render(request,'create.html',context)


def edit_post(request,id):
    post_value=post.objects.get(id=id)
    if request.method=='POST':
        form=post_form(request.POST,instance=post_value)
        if form.is_valid() :
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')

    else:
        form=post_form(instance=post_value)

    context={
        'form':form,
    }
    return render(request,'edit.html',context)
