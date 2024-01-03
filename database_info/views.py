from django.shortcuts import render
from .models import Cat


def show_db_info(request):
    all_cats = Cat.objects.all()
    return render(request, "show_db.html", {"all_cats": all_cats})
