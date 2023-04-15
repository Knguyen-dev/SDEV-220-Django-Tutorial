from django.shortcuts import render

# Create your views here.
def post_list(request):
    
	# Render an html file, empty dict. so no variables accessed in html
	# django file 
    return render(request, "blog/post_list.html", {})