from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import car as araba
from .postform import PostForm

def home_view(request):
    vals = araba.objects.all()

    if request.method == "POST":
            for b in vals:
                if b.plaka in request.POST and request.POST[b.plaka]:
                    b.tehlikede = 0
                    b.save()
                    return redirect('/success/')

    else:
        return render(request, 'home.html', locals())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect ('/success/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def search_form(request):
    return render(request,'searchform.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        arac = araba.objects.filter(plaka__icontains=q)
        for e in arac:
            if e.plaka == q:
                plate=e.plaka
                request.session['pilaka'] = plate
        return render(request, 'search_results.html',
                      {'arabalar': arac, 'query': q})

    elif 'b' in request.POST and request.POST['b']:
        plaka= request.session['pilaka']
        ar=araba.objects.filter(plaka__icontains=plaka).update(tehlikede = 1)

        return redirect('/success/')
    else:
        return HttpResponse('Please submit a search term.')

def success (request):
    return render(request,'success.html')

def arac_create (request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            print('x')
            am = form.save(commit=False)
            am.sahip = request.user
            am.save()
            return HttpResponse('işlem başarılı')
    else:
        form = PostForm
    context = {
        'form': form,
    }
    return render(request,'aracform.html',context)