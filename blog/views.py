from django.shortcuts import render

from blog.models import Entry

def home(request):
    
    entries = Entry.objects.all().order_by('-created')
    
    context = { 'entries':entries }

    return render(request, 'home.html', context)
    
def entrydetail(request, entry_slug):
    
    entrydetail = Entry.objects.get(entrySlug=entry_slug)
    
    context = { 'entrydetail':entrydetail }
    
    return render(request, 'entrydetail.html', context)
