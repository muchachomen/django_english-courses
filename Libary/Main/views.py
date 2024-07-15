from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import RegistrateForm, BookAddForm
from .models import Books, MyModel
# Create your views here.

def home(req):
    return render(req, 'layout.html')

def index(req):
    list = Books.objects.all()
    return render(req, 'layout.html', {'books': list})

class MyDetailView(DetailView):
    model = Books
    template_name = 'details.html'
    context_object_name = 'info'

def register(request):
     if request.method == 'POST':
            form = RegistrateForm(request.POST)

            if form.is_valid():
                 user = form.save()
                 return redirect('login')
     else:
            form = RegistrateForm()
     return render(request,  'registration/register.html', {'form': form})


def Formsss(req):
    if req.method == 'POST':
        feed = BookAddForm(req.POST)

        if feed.is_valid():
            feed.save()
            return redirect('prof')

    else:
        feed = BookAddForm()

    return render(req, 'form.html', {'feed': feed})
def my_view(request):
    my_queryset = Books.objects.all()
    paginator = Paginator(my_queryset, 2)
    page = request.GET.get('page')
    my_objects = paginator.get_page(page)
    return render(request, 'my_template.html', {'my_objects': my_objects})


def mediafiles(req):
    media = MyModel.objects.all()
    return render(req, 'MyModel.html', {'media': media})