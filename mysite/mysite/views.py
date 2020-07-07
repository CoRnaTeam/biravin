# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text', 'default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    cap=request.POST.get('cap','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')

    punctuations='''!@#$%^&*()_+=-/.,;'[]\?><:"{}|`~'''
    if djtext!='':
        if removepunc=='on':
            analyzed=""
            for i in djtext:
                if i not in punctuations:
                    analyzed+=i
                    djtext=analyzed
        
        if cap=='on':
            print("-----cap called-----")
            analyzed=""
            for i in djtext:    
                analyzed+=i.upper()
                djtext=analyzed

        if newlineremove=='on':
            analyzed=""
            for i in djtext:
                if i!="\n" and i!='\r':
                    analyzed+=i
                    djtext=analyzed

        if spaceremove=='on':
            analyzed=""
            for i in djtext:
                if i!=" ":
                    analyzed+=i
                    djtext=analyzed
        

        if removepunc=='off' and cap=='off' and newlineremove=='off' and spaceremove=='off':
            params={"purpose":'Error',"analyzed_text":"Please Select option before click on Button"}
            return render(request,'analyze.html',params)
         
        else:
            params={"purpose":'Your Analyzed Text',"analyzed_text":djtext}
            return render(request,'analyze.html',params)

    else:
        params={"purpose":'Error',"analyzed_text":"Please Enter Text In Text Area"}
        return render(request,'analyze.html',params)