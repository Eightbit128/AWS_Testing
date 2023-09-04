from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from .form import InputForm

def hello(request):
    return HttpResponse("Hello, World!")


# def home_view(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['Text_to_reverse']
#             return HttpResponseRedirect(f'/result/{name}')
#     else:
#         context = {'form': InputForm()}
#         return render(request, "home.html", context)

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




# def return_result(request, input):
#     input = input[::-1]
#     return HttpResponse(f"{input}")
