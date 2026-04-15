from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    data = {"header" : "Homepage", "message" : "Welcome to My Site!"}
    return render(request, "homepage.html", context = data)


def about(request):
    header = "About us"
    staff = ["John Nichols", "John Rogers", 'Timothy Smith']
    director = {"name" : "David Lee", "img" : "/director.jpg"}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header" : header, "staff" : staff, "director" : director, "address" : address}
    return render(request, "about.html", data)