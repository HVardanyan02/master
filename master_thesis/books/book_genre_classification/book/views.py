from django.shortcuts import redirect, render
from .forms import FileUploadForm
from django.http import HttpResponse
from django.template import loader
from .ru_genres import ru_genres
from .Prediction import predict

def index(request):
    context = {'range_18': range(18)}
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def logReg(request):
    return render(request, 'register.html', {})

def handle_uploaded_file(f):
    with open(f"./uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
            return redirect('result')  # սա եմ ավելացրել, որ աշխատի
    else:
        form = FileUploadForm()
    return render(request, 'check_genre.html', {'form': form})

def predict_view(request):
    pred = predict()
    template = loader.get_template('result.html')
    # context = {"pred": ru_genres.get(pred[0])}
    context = {"pred": ru_genres.get(pred)} # սա մի հատ ուսումնասիրել
    # print(f"Predicted key:::::::::::::", context)
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)