from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='Cricket')
    LTO=Topic.objects.exclude(topic_name='Cricket')
    LTO=Topic.objects.all()[: : -1]
    LTO=Topic.objects.order_by('topic_name')
    LTO=Topic.objects.order_by('-topic_name')
    LTO=Topic.objects.order_by(Length('topic_name'))
    LTO=Topic.objects.order_by(Length('topic_name').desc())
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    WTO=Webpage.objects.all()
    WTO=Webpage.objects.filter(topic_name='Cricket')
    WTO=Webpage.objects.exclude(topic_name='Cricket')
    WTO=Webpage.objects.all()[::-1]
    WTO=Webpage.objects.order_by('topic_name')
    WTO=Webpage.objects.order_by('-topic_name')
    WTO=Webpage.objects.order_by(Length('topic_name'))
    WTO=Webpage.objects.order_by(Length('topic_name').desc())
    d={'WTO':WTO}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    ATO=AccessRecords.objects.all()
    ATO=AccessRecords.objects.filter(author='Virat Kholi')
    ATO=AccessRecords.objects.exclude(author='Virat Kholi')
    ATO=AccessRecords.objects.all()[1:3:]
    ATO=AccessRecords.objects.all()[: : -1]
    ATO=AccessRecords.objects.order_by('author')
    ATO=AccessRecords.objects.order_by('-author')
    ATO=AccessRecords.objects.order_by(Length('author'))
    ATO=AccessRecords.objects.order_by(Length('author').desc())


    
    d={'ATO':ATO}
    return render(request,'display_accessrecords.html',d)