from django.shortcuts import render

def home_page_view(request):
    return render(request, template_name='common/home-page.html')

