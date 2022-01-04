from django.shortcuts import render,redirect,get_object_or_404
from aye.models import EmployeeDetails
from aye.forms import Detalis
from django.views.generic import UpdateView, DetailView
from django.http import HttpResponse


# Create your views here.







def index(request):
   # resultsdisplay=EmployeeDetails.objects.all()

   ayf = EmployeeDetails.objects.all()
   return render(request, "aye/index.html",{'EmployeeDetails':ayf})


def input(request):
    eror = ''
    if request.method == 'POST':
        form = Detalis(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            eror = 'чото поломалось иди чины'
    form = Detalis()
    data = {
        'form': form,
        'eror': eror
    }
    return render(request, "aye/input.html",  data)




class name_user(DetailView):

    model = EmployeeDetails
    template_name= 'templates/aye/name.html'
    context_object_name= 'gachi'














