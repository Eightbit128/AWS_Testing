from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .form import InputForm

def hello(request):
    url_data = [
        {"url": "https://github.com/Eightbit128/AWS_Testing", "tag": "Github repo"},
        {"url": "http://34.201.155.23:8080/", "tag": "Jenkins Login"},
        {"url": "http://34.201.155.23:8000/input/", "tag": "basic input with forms"},
    ]

    return render(request, 'urls.html', {'url_data': url_data})

def home_view(request):
    if request.method == 'GET':
        name = request.GET.get('Text_to_reverse', '')
        format_text = request.GET.get('Text_to_format', '')
        if name:
            return HttpResponseRedirect(f'/result/?input={name}')
        if format_text:
            return HttpResponseRedirect(f'/format/?input={format_text}')
    context = {'form': InputForm()}
    return render(request, "home.html", context)


def return_result(request):
    input_text = request.GET.get('input', '')
    reversed_text = input_text[::-1]
    print (reversed_text)
    return HttpResponse(f"Reversed Text: {reversed_text}")

def format_result(request):
    input_text = request.GET.get('input', '')
    result = ""
    for i, char in enumerate(input_text):
        if i % 2 ==1:
            result += char.upper()
        else:
            result += char
    return HttpResponse(f"Formatted Text: {result}")


@csrf_exempt #testing
def format_result_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('input', '')
            result = ""
            for i, char in enumerate(input_text):
                if i % 2 == 1:
                    result += char.upper()
                else:
                    result += char
            response_data = {"formatted_text": result}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


