from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    comments = Comment.objects.all().values()
    context = {'comments' : comments}

    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        if request.method == "POST":
            return HttpResponseRedirect("/infovaksin")

    context['form'] = form

    return render(request,'infovaksin.html',context)

@csrf_exempt
def AddCommentFlutter(request):
    if request.method == 'POST':
        newComment = json.loads(request.body)

        new_comment = Comment(
            name = newComment['name'],
            content = newComment['content'],
            date = newComment['date']
        )

        new_comment.save()
        return JsonResponse(new_comment, safe=False)
# def show_json(request):
#     return JsonResponse()

# def add_komen(request):
#     context = {}

#     form = CommentForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         if request.method == "POST":
#             return redirect('infovaksin:index')
    
#     context['form'] = form
#     return render(request, 'infovaksin.html', context)

def vaksindata(request) :
    data = [
    {
      "name": "Sinovac",
      "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
      "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
      "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Astrazeneca",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Sinopharm",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Moderna",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Pfizer",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Novavax",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    }
  ]
    return JsonResponse({'datas' : data})

# def post_comment(request, post):
#     comments = post.comments.filter(status=True)

#     user_comment = None

#     if request.method == 'POST':
#         comment_form = NewCommentForm(request.POST)
#         if comment_form.is_valid():
#             user_comment = comment_form.save(commit=False)
#             # user_comment.post = post
#             user_comment.save()
#             return HttpResponseRedirect('/infovaksin')
#     else:
#         comment_form = NewCommentForm()

#     return render(request, 'infovaksin.html', 
#         {
#         'user_comment' : user_comment, 
#         'comments' : comments, 
#         'comment_form' : comment_form,
#         },
#         )

# def comment_gan(request):
#     context = {}

#     form = NewCommentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/")
    
#     context['form'] = form
#     return render(request, 'infovaksin.html', context)