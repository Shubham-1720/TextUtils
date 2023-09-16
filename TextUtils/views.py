# i have created this file ---shubham
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1> this google </h1> <a href="https://www.w3schools.com/">Go to Google</a>''')


def index(request):
    # return HttpResponse("Home")
    # params = {'name':'harry', 'place':'mars'} can be pass in rendeer as third element and can be use in template in double curly barces
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    lower = request.POST.get('lower', 'off')
    charCount = request.POST.get('charCount', 'off')
   
   
    # Analyze the text 
    # CHECKING CHECK BOX VALUE
    if removepunc == "on":
        punctuation = '''!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        # analyzed = djtext
        analyzed = ''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    if capitalize=='on':
        analyzed = djtext.upper()
        params = {'purpose': 'All words in Upparcase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if lower=='on':
        analyzed = djtext.lower()
        params = {'purpose': 'All words in Lowercase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if charCount =='on':
       
        count=  0
        for index,char in enumerate(djtext):
            if djtext[index]!=' ':
                count +=1
        analyzed = count
        params = {'purpose': 'Number of character in text is', 'analyzed_text':analyzed}
      
    if (removepunc != "on" and capitalize!="on" and lower!="on" and charCount !="on"):
        return HttpResponse("Please select any Operation")
    
    return render(request, 'analyze.html', params)
        
    


def navigate(request):
    return render(request, "links.html")