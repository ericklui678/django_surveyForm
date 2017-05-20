from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveyForm_app/index.html')

def survey_process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/result')

def result(request):
    return render(request, 'surveyForm_app/result.html')
