from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'False')
    removespace = request.GET.get('removespace', 'False')


    if (removepunc == 'on'):                                        #djtext = ankit :is   ankit  is
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'ANALYZED TEXT', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removespace == 'on'):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'ANALYZED TEXT', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)



    # params = {'purpose': 'ANALYZED TEXT', 'analyzed_text': analyzed}
    # return render(request, 'analyze.html', params)
