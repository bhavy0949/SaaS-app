import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

# .resolve() -> gives /Users/bhavygupta/Documents/saas-app/src/SaaS/home.html   (absolute path)
this_dir = pathlib.Path(__file__).resolve().parent

# def home_page_view(request, *args, **kwargs):
#     return about_view(request, *args, **kwargs)

def home_page_view(request, *args, **kwargs):
    return HttpResponse("OK")

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    path = request.path
    page_qs = PageVisit.objects.filter(path = path)
    try:
        percenatge = page_qs.count() * 100/qs.count()
    except:
        percenatge = 0
    my_title = "My First Django Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percentage": percenatge,
    }
    PageVisit.objects.create(path = path)
    return render(request, "home.html", my_context)

def old_home_page_view(request, *args, **kwargs):
    my_title = "My First Django Page"
    my_context = {
        "page_title": my_title,
    }
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Hello World {page_title}</h1>
    </body>
    </html>
    """.format(**my_context)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
