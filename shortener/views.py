from django.shortcuts import render, redirect, get_object_or_404
from .forms import Shortener
from .models import UrlShortcut
import string,random
from django.contrib.auth.decorators import login_required
# Create your views here.

def url_generator(chars=string.ascii_lowercase+string.digits, size=5):
    rand_string = ""
    for _ in range(size):
        rand_string += random.choice(chars)
    new_url = 'http://myshortn.er/'+rand_string
    return new_url, rand_string

def unique_url(short_url):
    if UrlShortcut.objects.filter(short_url=short_url).exists():
        new_url = unique_url(url_generator())
        return new_url
    return short_url
    
@login_required(login_url='accounts:login')
def shortener(request, slug=None):
    if request.method == 'POST':
        form = Shortener(request.POST)
        if form.is_valid():
            raw_url = form.cleaned_data['url']
            new_url, slug = url_generator()
            short_url = unique_url(new_url)
            url = UrlShortcut(short_url=short_url, raw_url=raw_url)
            url.save() 
            return redirect('shortener:result', slug)
    elif slug is not None:
        url = UrlShortcut.objects.filter(short_url__icontains=slug).first()
        form = Shortener()
        context = {
            'form': form,
            'url': url,
            'slug': slug,
        }            
        return render(request, 'shortener/shortener.html', context)
    else:
        form = Shortener()
        return render(request, 'shortener/shortener.html', {'form':form})

def redirect_view(request, slug):
    url = get_object_or_404(UrlShortcut, short_url__icontains=slug)
    return redirect(f'{url.raw_url}')
