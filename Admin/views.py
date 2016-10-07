from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    return render(request, 'static/index.html', context)

def index2(request):
    context = {}
    return render(request, 'static/index2.html', context)    

def widget(request):
    context = {}
    return render(request, 'static/pages/widgets.html', context)        

def chartjs(request):
    context = {}
    return render(request, 'static/pages/charts/chartjs.html', context)        

def morris(request):
    context = {}
    return render(request, 'static/pages/charts/morris.html', context)        

def flot(request):
    context = {}
    return render(request, 'static/pages/charts/flot.html', context)        

def inline(request):
    context = {}
    return render(request, 'static/pages/charts/inline.html', context)        

def general(request):
    context = {}
    return render(request, 'static/pages/UI/general.html', context)        


def icons(request):
    context = {}
    return render(request, 'static/pages/UI/icons.html', context)        

def buttons(request):
    context = {}
    return render(request, 'static/pages/UI/buttons.html', context)        


def sliders(request):
    context = {}
    return render(request, 'static/pages/UI/sliders.html', context)        


def timeline(request):
    context = {}
    return render(request, 'static/pages/UI/timeline.html', context)            


def modals(request):
    context = {}
    return render(request, 'static/pages/UI/modals.html', context)            

def timeline(request):
    context = {}
    return render(request, 'static/pages/UI/timeline.html', context)            

def form_general(request):
    context = {}
    return render(request, 'static/pages/forms/general.html', context)            

def advanced(request):
    context = {}
    return render(request, 'static/pages/forms/advanced.html', context)            

def editors(request):
    context = {}
    return render(request, 'static/pages/forms/editors.html', context)            

def simple(request):
    context = {}
    return render(request, 'static/pages/tables/simple.html', context)            


def data(request):
    context = {}
    return render(request, 'static/pages/tables/data.html', context)            

def invoice(request):
    context = {}
    return render(request, 'static/pages/examples/invoice.html', context)            

def invoice_print(request):
    context = {}
    return render(request, 'static/pages/examples/invoice-print.html', context)                

def profile(request):
    context = {}
    return render(request, 'static/pages/examples/profile.html', context)            

def login(request):
    context = {}
    return render(request, 'static/pages/examples/login.html', context)            

def register(request):
    context = {}
    return render(request, 'static/pages/examples/register.html', context)            

def lockscreen(request):
    context = {}
    return render(request, 'static/pages/examples/lockscreen.html', context)            

def four04(request):
    context = {}
    return render(request, 'static/pages/examples/404.html', context)            

def five00(request):
    context = {}
    return render(request, 'static/pages/examples/500.html', context)            

def blank(request):
    context = {}
    return render(request, 'static/pages/examples/blank.html', context)            

def place(request):
    context = {}
    return render(request, 'static/pages/examples/pace.html', context)            

def top_nav(request):
    context = {}
    return render(request, 'static/pages/layout/top-nav.html', context)            


def boxed(request):
    context = {}
    return render(request, 'static/pages/layout/boxed.html', context)            


def fixed(request):
    context = {}
    return render(request, 'static/pages/layout/fixed.html', context)            


def collapsed_sidebar(request):
    context = {}
    return render(request, 'static/pages/layout/collapsed-sidebar.html', context)            

def calendar(request):
    context = {}
    return render(request, 'static/pages/calendar.html', context)            

def mailbox(request):
    context = {}
    return render(request, 'static/pages/mailbox/mailbox.html', context)            
