from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render, redirect  
from projects.forms import ProjectsForm  
from projects.models import Projects  
 
def project(request):  
    if request.method == "POST":  
        form = ProjectsForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProjectsForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    projects = Projects.objects.all()  
    return render(request,"show.html",{'projects':projects})  
def edit(request, id):  
    project = Projects.objects.get(id=id)  
    return render(request,'edit.html', {'project':project})  
def update(request, id):  
    project = Projects.objects.get(id=id)  
    form = ProjectsForm(request.POST, instance = project)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'project': project})  
def destroy(request, id):  
    project = Projects.objects.get(id=id)  
    project.delete()  
    return redirect("/show")
