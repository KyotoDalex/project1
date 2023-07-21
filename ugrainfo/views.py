from django.shortcuts import render



# Create your views here.
def sass_page_handler(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'account.html')


def tyumen(request):
    return  render(request,'tyumen.html')
def hmao(request):
    return render(request,'ugra.html')
def yanao(request):
    return render(request,'yamal.html')