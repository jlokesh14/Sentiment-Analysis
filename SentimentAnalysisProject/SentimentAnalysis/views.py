from django.shortcuts import render
from textblob import TextBlob
from django.http import HttpResponse
from django.template import loader


def function(request):
    result = None
    prediction = "Neutral"
    if request.method == 'POST':
        text = request.POST.get('text', '')
        obj = TextBlob(text)
        sentiment = obj.sentiment

        result = f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity} "

        if sentiment.polarity > 0:
            prediction = "Positive"
        elif sentiment.polarity < 0:
            prediction = "Negative"

    return render(request, 'index.html', {'result': result, 'sentiment': prediction})