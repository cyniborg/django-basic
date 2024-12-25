from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader

jobs = [
    "First job",
    "Second job"
]
job_descriptions = [
    "First job description",
    "Second job description"
]
def helloWorld(request):
    try:
        context = {
            "jobs": jobs,
        }
        return render (request, "app/jobs_list.html", context)
    except:
        return HttpResponse("Not Found")

def jobDetail(request, id):
    try:
        context = {
            "job_title": jobs[id],
            "job_description": job_descriptions[id],
            "link": reverse("home_page")
        }
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not found")
    
def helloTemplate(request):
    template = loader.get_template("app/hello.html");
    context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context);