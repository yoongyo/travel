from django.shortcuts import render



def main(request):
    return render(request, 'travel/_main.html')