# Base_App/views.py
from django.shortcuts import render
from django.apps import apps

def msg(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            app_config = apps.get_app_config('MYAPP')  
            transformed_text = app_config.vector.transform([text])
            prediction = app_config.model.predict(transformed_text)
            return render(request, 'index.html', {"prediction": prediction[0]})
        else:
            return render(request, 'index.html', {"error": "No text provided."})
    return render(request, 'index.html', {"error": "Invalid request method."})
