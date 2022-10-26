from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from article.models import *
from django.core.paginator import Paginator
import re
import datetime
import os
import time

def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method =='POST':
        checkemail = request.POST.get('checkresult')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        if checkemail =='이상없음':
            User(email=email, name=name, pwd=pwd).save()
            return redirect('/home/')
        else:
            return redirect('/signup/')
    else:
        return render(request, 'signup.html')
def searchuserinfo(request):
    useremail = request.GET.get('email')
    pattern = re.compile('([\w]+)@([a-zA-Z]+)[.]([a-zA-Z]+)')
    search = User.objects.filter(email=useremail)
    checkemail=pattern.fullmatch(useremail)
    if checkemail==None:
        return HttpResponse('이메일형식에 맞지 않아요')
    else:
        if search:
            return HttpResponse('회원정보 존재')
        else:
            return HttpResponse('이상없음')
def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        try:
            checkuser = User.objects.get(email=email, pwd=pwd)
            request.session['email']=email
            request.session['name']=checkuser.name
            return redirect('/home/')
        except:
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')
def signout(request):
    request.session.flush()
    return redirect('/home/')
def list(request):
    article_list = Article.objects.all()
    context = {'article_list' : article_list}
    return render(request, 'list.html', context)
def map(request):
    return render(request, 'map.html')
def require(request):
    return render(request, 'require.html')
def write(request):
    if request.method == 'POST':
        title =request.POST.get('title')
        text =request.POST.get('text')
        useremail = request.session['email']
        time1 = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        user = User.objects.get(email = useremail)
        article_save = Article(title=title, content=text, user=user, time = time1)
        article_save.save()
        files = request.FILES.getlist('file')
        for file in files:
            file_name = file.name
            file_size = file.size
            save_name = file_name
            if os.path.isfile('c:/site/files/%s' %save_name):
                ext = save_name[save_name.rfind('.')+1:]
                n = save_name[:save_name.rfind('.')]
                save_name = '%s_%s.%s' %(n, time.time(), ext)
            with open('c:/site/files/%s' %save_name, 'wb') as file_upload:
                for chunk in file.chunks():
                    file_upload.write(chunk)
            FileAttach(o_filename = file_name, save_filename = save_name, filesize = file_size, article=article_save).save()

        return redirect('/article/list')
    return render(request, 'write.html')


def detail(request, id):
    article = Article.objects.get(id=id)
    files = article.fileattach_set.all()

    context = {
        'article' :article,
        'files' : files
    }     
    return render(request, 'detail.html', context)
def delete_article(request, id):

    article_ = Article.objects.get(id=id)
    article_.delete()
    return HttpResponse('delete on')
def modify_article(request, id):
    article = Article.objects.get(id=id)
    files = article.fileattach_set.all()
    context = {
        'article':article,
        'files':files
    }
    return render(request, 'modify_article.html', context)






















    # if request.method == 'POST':
    #     title= request.POST.get('title')
    #     text= request.POST.get('text')
    #     email =request.session['email']
    #     files = request.FILES.getlist('file')
    #     time = datetime.datetime.now()
    #     time = time.strftime('%Y/%m/%d %H:%M')
    #     user = User.objects.get(email=email)
    #     article_save = Article(title=title, content=text, user=user, time = time)
    #     article_save.save()
    #     for file in files:
    #         file_name = file.name
    #         file_size = file.size
    #         save_name = file_name
    #         if os.path.isfile('c:/site/files/%s' %save_name):
    #             ext = save_name[save_name.rfind('.')+1:]
    #             name = save_name[:save_name.rfind('.')]
    #             save_name = '%s_%s.%s' %(name, time.time(),ext)
    #         with open('c:/site/files/%s'%save_name, 'wb') as up_file:
    #             for chunk in file.chunks():
    #                 up_file.write(chunk)
    #             FileAttach(save_filename=save_name, o_filename = file_name, filesize=file_size, article=article_save).save()
    #     return redirect('/article/list/')
    # return render(request, 'write.html')