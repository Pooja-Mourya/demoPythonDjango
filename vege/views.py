from django.shortcuts import render, redirect
from .models import Receipe  # Import the Receipe model

# Create your views here.
def receipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')  # Use get() to safely retrieve the file

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

    return redirect('/receipe')
    return render(request, 'receipe/receipe.html')
