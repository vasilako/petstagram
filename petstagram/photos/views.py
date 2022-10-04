from django.shortcuts import render

def add_photo(request):
    return render(request, 'photos/photo-add-page.html')

def show_details_photo(request, pk):
    return render(request, 'photos/photo-details-page.html')

def edit_details_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')

# Create your views here.
