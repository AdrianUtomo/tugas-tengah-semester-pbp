from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Faq,Qs
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
import json

from .forms import QsForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    faq = Faq.objects.all()
    page = Paginator(faq, 6)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)

    if request.method == "POST":
        query_name = request.POST.get('question', None)
        if query_name:
            results = Faq.objects.filter(question__icontains=query_name)
            return render(request, 'index_faq.html', {"results":results})
    
    return render(request, 'index_faq.html', {'faq':page_obj})

@login_required(login_url="login") 
def qs(request):
    form = QsForm(request.POST or None, request.FILES or None)
    data= {}

    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['qs'] = form.cleaned_data.get('qs')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {'form':form,
    }
    
    return render(request, 'index_faq.html',context)

def jsonFlutter(request):
    data = [serializers.serialize('json', Faq.objects.all())]
    return HttpResponse(json.dumps(data), content_type="application/json")

# @csrf_exempt
# def QuestionBox(request):
#     if request.method == 'POST':
#         question = json.loads(request.qs)

#         new_question = Qs(
#             qs = question['question'],
        
#        )

#         new_question.save()
#         return JsonResponse({"instance": "Pertanyaan berhasil dikirim!"}, status=200)
