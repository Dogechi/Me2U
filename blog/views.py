from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from me2ushop.forms import ProductForm, PostForm, PostUpdateForm
from users.models import SellerProfile
from .models import *
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView, FormView


# Create your views here.

# def home(request):
#     blogs = Post.objects.all()
#
#     return render(request, 'blog/blog.html', locals())

@login_required
def likeView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # post.likes.add(request.user)

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:postView', args=[str(slug)]))


class HomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostDetailedView(DetailView):
    model = Post
    template_name = 'blog/blog_single.html'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        context = super(PostDetailedView, self).get_context_data()

        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked

        # authors = {'author': []}
        # posts = Post.objects.all()
        # count = 0
        # for post in posts:
        #     while count < 5:
        #         if post.author in authors:
        #             continue
        #         else:
        #             authors['author'].append(post.author)
        #             print(authors)
        #         count += 1

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['product', 'title', 'content', 'image']
    template_name = 'sellers/product_form.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:postView', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)

        context.update({

            'page_title': 'post Create',
        })
        return context

    def form_valid(self, form):
        # form.instance.seller = self.request.user
        obj = form.save(commit=False)
        obj.author = self.request.user

        obj.save()
        return super(PostCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['brand_id'] = self.kwargs['pk']
        print(kwargs['brand_id'])

        return kwargs


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    # fields = ['product', 'title', 'content', 'snippet', 'image']
    form_class =PostUpdateForm

    template_name = 'sellers/product_form.html'

    # widgets = {
    #     'snippet': forms.Textarea(attrs={'class': 'form-control'})
    # }
    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)

        context.update({

            'page_title': 'post Update',
        })
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'sellers/product_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:blog_home')

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)

        context.update({

            'page_title': 'post Delete',
        })
        return context
