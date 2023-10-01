from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView# type: ignore
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .models import LoginUser
from .models import ImageUpload, ThreadUpload, ModUpload
# from .models import FavoriteImg
from .models import Thread
from .forms import ImageUploadForm, ThreadUploadForm, ModUploadForm
from .forms import LoginForm
from .forms import CreateAccountForm
from .forms import ThreadPostForm
from .imagelist import list_path
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.core.paginator import Paginator
# from sqlalchemy import create_engine
# import pandas as pd
# from .models import Likes, Articles
# from django.http import JsonResponse
# Create your views here.


class MainView(TemplateView):
    template_name = "main.html"
    # form_class = LoginForm, ImageUploadForm
    # model = NoteTable
    def get(self, request, **kwargs):
        ctx = {
            # 'user': self.request.user,
            'username': self.request.user.username,# type: ignore
            'img':ImageUpload.objects.all()[:10],
            'thread':ThreadUpload.objects.all()[:10],
            'mod':ModUpload.objects.all()[:10]
        }
        # return self.render_to_response(ctx)
        return render(request,"main.html",ctx)
    
    
    # example
    # def get_context_data(self, **kwargs):
    #     context = super(HolidayListView, self).get_context_data(**kwargs)
    #     context.update({
    #         'object_list2': holiday2.objects.all(),
    #     })
    #     return context

class IndexView(LoginView):
    # form_class = LoginForm
    authentication_form = LoginForm
    template_name = "index.html"
    
    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1000000)
        return super().form_valid(form) # type: ignore
    
    
    # another case
    # def post(self, request, *args, **kwargs):
        # email = request.POST['email']
        # password = request.POST['password']
        # user = authenticate(email=email, password=password)
        # next_url = request.POST['next'] # 追記箇所
        # if user is not None and user.is_active:
            # login(request, user)
        # if next_url: # 追記箇所(28～29行目)
            # return redirect(next_url)
        # return redirect('account:top')

class LogoutView(LogoutView):
    pass
# CASE1
# class MyLogoutView(View):
    # 
    # def get(self, request, *args, **kwargs):
        # logout(request)
        # return redirect('account:login')

class CreateAccountView(CreateView):
    template_name = "createAccount.html"
    form_class = CreateAccountForm
    model = LoginUser
    success_url = reverse_lazy("minecraft:index")    

class ResetPasswordView(TemplateView):
    template_name = "resetPassword.html"
    # model = NoteTable


class PostView(LoginRequiredMixin, CreateView, generic.edit.ModelFormMixin):
    form_class = ImageUploadForm
    template_name = "post.html"
    # success_url = reverse_lazy("minecraft:post")
    
    # def get_form_kwargs(self):
    #     kwgs = super().get_form_kwargs()
    #     kwgs["user"] = self.request.user
    #     return kwgs
    
class PostImageView(LoginRequiredMixin, CreateView, generic.edit.ModelFormMixin):
    form_class = ImageUploadForm
    template_name = "post_image.html"
    success_url = reverse_lazy("minecraft:post")
    
    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs["user"] = self.request.user
        return kwgs
    
class PostThreadView(LoginRequiredMixin, CreateView, generic.edit.ModelFormMixin):
    form_class = ThreadUploadForm
    template_name = "post_thread.html"
    success_url = reverse_lazy("minecraft:post")
    
    
    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs["user"] = self.request.user
        return kwgs
    
class PostModView(LoginRequiredMixin, CreateView, generic.edit.ModelFormMixin):
    form_class = ModUploadForm
    template_name = "post_mod.html"
    success_url = reverse_lazy("minecraft:post")


    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs["user"] = self.request.user
        return kwgs


class SearchView(TemplateView):
    template_name = "search.html"
    # model = NoteTable
    
    
class SearchModView(ListView):
    model = ModUpload
    template_name = "search-mod.html"
    # model = NoteTable
    def get(self, request, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        if q := query.get('q'): #python3.8以降
            queryset = queryset.filter(title__icontains=q)
        else:
            queryset = ModUpload.objects.all()
        context = {
            # 'user': self.request.user,
            'username': self.request.user.username,# type: ignore
            # 'img':ImageUpload.objects.all()
            'mod':queryset
        }
        return render(request,"search-mod.html",context)
    

class SearchPhotoView(ListView):
    template_name = "search-photo.html"
    model = ImageUpload
    def get(self, request, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        if q := query.get('q'): #python3.8以降
            queryset = queryset.filter(title__icontains=q).order_by('-created_at')
        else:
            queryset = ImageUpload.objects.all()
        context = {
            # 'user': self.request.user,
            'username': self.request.user.username,# type: ignore
            # 'img':ImageUpload.objects.all()
            'img':queryset
        }
        return render(request,"search-photo.html",context)


class SearchThreadView(ListView):
    model = ThreadUpload
    template_name = "search-thread.html"
    def get(self, request, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        if q := query.get('q'): #python3.8以降
            queryset = queryset.filter(title__icontains=q)
        else:
            queryset = ThreadUpload.objects.all()
        context = {
            # 'user': self.request.user,
            'username': self.request.user.username,# type: ignore
            # 'img':ImageUpload.objects.all()
            'Thread':queryset
        }
        return render(request,"search-thread.html",context)
    #     return queryset.order_by('-created_at')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # {'pk':{'count':ポストに対するイイネ数,'is_user_liked_for_post':bool},}という辞書を追加していく
    #     d = {}
    #     for post in self.object_list:
    #         # postに対するイイね数
    #         like_for_post_count = post.favoriteimg_set.count()
    #         # ログイン中のユーザーがイイねしているかどうか
    #         is_user_liked_for_post = False
    #         if not self.request.user.is_anonymous:
    #             if post.favoriteimg_set.filter(user=self.request.user).exists():
    #                 is_user_liked_for_post = True

    #         d[post.pk] = {'count': like_for_post_count, 'is_user_liked_for_post': is_user_liked_for_post}
    #     context['post_like_data'] = d
    #     return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # 投稿に対するいいねの数
    #     like_count = self.object.favoriteimg_set.count()# type: ignore
    #     context['like_count'] = like_count
        
    #     if self.object.favoriteimg_set.filter(user_id=self.request.user).exists():# type: ignore
    #         context['is_user_liked'] = True
    #     else:
    #         context['is_user_liked'] = False
            
    #     return context
    
# def like(request):
#     ImageUpload_pk = request.POST.get('ImageUpload_pk')
    
#     context = {
#         'user_id': f'{ request.user }',
#     }
#     print(request.user.id)
#     print(ImageUpload.id)
#     print(ImageUpload_pk)
#     imageupload = get_object_or_404(ImageUpload, pk=ImageUpload_pk)
#     print(request.user.id)
#     like = FavoriteImg.objects.filter(target=imageupload, user_id=request.user.id)
    
#     form = ThreadPostForm(request.POST or None)
#     # print(ThreadUpload.objects.get(pk=pk))
#     if like.exists():
#         like.delete()
#         context['method'] = 'delete'
#     else:
#         like.create(target=imageupload, user_id=request.user)
#         context['method'] = 'create'
#     context['like_count'] = imageupload.favoriteimg_set.count()# type: ignore

#     return JsonResponse(context)

# class LikeBase(LoginRequiredMixin, View):
#     """いいねのベース。リダイレクト先を以降で継承先で設定"""
#     def get(self, request, *args, **kwargs):
#         #記事の特定
#         pk = self.kwargs['pk']
#         related_post = ImageUpload.objects.get(pk=pk)

#         #いいねテーブル内にすでにユーザーが存在する場合   
#         if self.request.user in related_post.like.all(): 
#             #テーブルからユーザーを削除 
#             obj = related_post.like.remove(self.request.user)
#         #いいねテーブル内にすでにユーザーが存在しない場合
#         else:
#             #テーブルにユーザーを追加                           
#             obj = related_post.like.add(self.request.user)  
#         return obj
    
# class LikeHome(LikeBase):
#     """HOMEページでいいねした場合"""
#     def get(self, request, *args, **kwargs):
#         #LikeBaseでリターンしたobj情報を継承
#         super().get(request, *args, **kwargs)
#         #homeにリダイレクト
#         return redirect('home')

# class LikeDetail(LikeBase):
#     """詳細ページでいいねした場合"""
#     def get(self, request, *args, **kwargs):
#         #LikeBaseでリターンしたobj情報を継承
#         super().get(request, *args, **kwargs)
#         pk = self.kwargs['pk'] 
#         #detailにリダイレクト
#         return redirect('detail', pk)
    
    


    
	



@login_required
def post_thread_list(request, pk):
    # per_page = 20
    
    threadId = get_object_or_404(ThreadUpload,pk=pk)
    post_list= Thread.objects.filter(threadId=threadId)
    form = ThreadPostForm(request.POST or None)
    # print(ThreadUpload.objects.get(pk=pk))
	
    if form.is_valid():
        post = form.save(commit=False)
        post.threadId = threadId
        post.userId_id = request.user.id# type: ignore 
        post.save()
        return redirect('minecraft:Thread', pk=threadId.pk)
    
    context = {'form': form,'post_list': post_list,'thread':threadId.title}
    return render(request, 'Thread.html', context)

class UserInfoView(LoginRequiredMixin, TemplateView):
    template_name = "userInfo.html"
    def get(self, request, **kwargs):
        ctx = {
            # 'user': self.request.user,
            'username': self.request.user.username,# type: ignore
            'img':ImageUpload.objects.filter(userId=self.request.user.id),# type: ignore
            'thread':ThreadUpload.objects.filter(userId=self.request.user.id),# type: ignore
            'mod':ModUpload.objects.filter(userId=self.request.user.id)# type: ignore
        }
        # return self.render_to_response(ctx)
        return render(request,"userInfo.html",ctx)

class SettingView(LoginRequiredMixin, TemplateView):
    template_name = "setting.html"
    

class ReleasedView(TemplateView):
    template_name = "released.html"
    # model = NoteTable