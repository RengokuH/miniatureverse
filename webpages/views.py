from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import (
    LandingPage,
    CollectionsInfo,
    Collection,
    Journey,
    Roadmap,
    OurCollection,
    ComingSoon,
    MyContact,
    Contact,
)
from .forms import ContactForm


def home(request):
    landingPage = LandingPage.objects.all()
    collectionsInfo = CollectionsInfo.objects.all()
    collection = Collection.objects.all()
    journey = Journey.objects.all()
    roadmap = Roadmap.objects.all()
    ourCollection = OurCollection.objects.all()
    comingSoon = ComingSoon.objects.all()
    myContact = MyContact.objects.all()
    contact = Contact.objects.all()

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactForm()
    
    data = {
        "landingPage": landingPage,
        "collectionsInfo": collectionsInfo,
        "collection": collection,
        "journey": journey,
        "roadmap": roadmap,
        "ourCollection": ourCollection,
        "comingSoon": comingSoon,
        "myContact": myContact,
        "contact": contact,
        "form": form,
    }
    return render(request, "./portfolio/index.html", data)


def project_detail(request, id):
    detail = get_object_or_404(OurCollection, pk=id)
    data = {"detail": detail}
    return render(request, "./sections/portfolio-details.html", data)