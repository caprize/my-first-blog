from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import Post,Order
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,OrderForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import telebot
from telebot.types import Message
import requests
from telebot import types
BASE_URL='https://api.telegram.org/bot/731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4'
TOKEN = '731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4o'
tb = telebot.TeleBot(TOKEN)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
def my_view ( request ):
    username = request . POST [ 'username' ]
    password = request . POST [ 'password' ]
    user = authenticate ( request , username = username , password = password )
    if user is not None :
        login ( request , user )
        return redirect('post_list')
    else :
        return redirect('post_list')
@login_required
def logout_view ( request ):
    logout ( request )
    return redirect('post_list')
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/books/")
    else:
        data, errors = {}, {}

    return render_to_response("registration/register.html", {
        # 'form' : forms.FormWrapper(form, data, errors)
    })

# def send_bot(request):
#     # post = get_object_or_404(Post, pk=pk)
#     # post.delete()
#     tb.send_message(419887691,'hi')
#     # return HttpResponseRedirect(request.GET.get('post_list'))
#     return redirect('post_list')

# def send_bot ( request ):
#     # if this is a POST request we need to process the form data
#     if request . method == 'POST' :
#         # create a form instance and populate it with data from the request:
#         form = OrderForm ( request . POST )
#                 # check whether it's valid:
#         if form . is_valid ():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:


#             return HttpResponseRedirect ( '/' )

#     # if a GET (or any other method) we'll create a blank form
#     else :
#         form = OrderForm()

#     return render(request, 'blog/post_edit.html', {'form': form})
def send_bot(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            user=''
            post = form.save(commit=False)

            post.save()
            user+='Заказ:'+' \n'
            user+='Айди пользователя: '
            user+= post.tgid + ' \n'
            user+= 'Суть заказа: '
            user+= post.dops + ' \n'
            tb.send_message(-381217332, user)
            
            return redirect('post_list')
            

    else:
        form = OrderForm()

    return render(request, 'blog/send_bot.html', {'form': form})
def contact(request):
    errors = []
    form = {}
    if request.POST:
         
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')
         
        if not form['name']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')
             
        if not errors:
            # ... сохранение данных в базу
            return HttpResponse('Спасибо за ваше сообщение!')
         
    return render(request, 'contact.html', {'errors': errors, 'form':form})