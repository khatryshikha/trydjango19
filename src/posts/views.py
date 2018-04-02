from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect('/posts')
	context = {
		"form":form,
	}

	return render(request,"post_form.html",context) 

def post_detail(request,id):
	instance=get_object_or_404(Post,id=id)
	context={
	"title":instance.title,
	"instance":instance,
	}

	return render(request,"post_details.html",context)

def post_list(request):
	queryset=Post.objects.all()
	context={
	"object_list":queryset,
	"title":"List"
	}
	return render(request,"index.html",context)


def post_delete(request):
	instance = get_object_or_404(Post , id=id)
	instance.delete()

	return redirect("posts:list")

def post_update(request,id=None):
	instance = get_object_or_404(Post , id=id)
	form = PostForm(request.POST or None , instance=instance)
	print "sasds"
	if form.is_valid():
		print "inform"
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url())
		return redirect('/posts/id')
	print "2mid"
	context = {
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	print "2adsd"
	return render(request,"post_form.html",context) 
						