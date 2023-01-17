from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.
class BlogPageView(ListView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'


@method_decorator(login_required, name='dispatch')
class BlogDetailView(UserPassesTestMixin, DetailView):

    model = BlogPost
    context_object_name = 'post'
    template_name = 'flow_blog/blog_details.html'
    slug_field = 'slug'
    form = CommentForm

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        if self.request.user:
            return redirect('protect_profile')
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            blogpost = self.get_object()
            form.instance.author = request.user
            form.instance.blogpost = blogpost
            form.save()
            messages.success(request, 'YOU ADDED A NEW COMMENT')
            return HttpResponseRedirect(reverse('blog_details', kwargs={'pk': blogpost.pk})) 
            # return HttpResponse('blog_details')
        else:
            form = CommentForm()

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(
            blogpost=self.object.id).count()
        post_comments = Comment.objects.all().filter(blogpost=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context


@method_decorator(login_required, name='dispatch')
class AddBlogView(UserPassesTestMixin, CreateView):

    model = BlogPost
    form_class = BlogForm
    template_name = 'flow_blog/add_blog.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        return redirect('protect_profile')


@method_decorator(login_required, name='dispatch')
class UpdateBlogView(UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'flow_blog/edit_blog.html'
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.creator == self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.role and self.request.user.profile.bio:
            return self.request.user

    def handle_no_permission(self):
        return redirect('protect_profile')


class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/delete_blog.html'
    success_url = reverse_lazy('blog_page')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        if self.request.user == blogpost.creator:
            return True
        return False


# class CommentDeleteView(UserPassesTestMixin, DeleteView):
#     model = Comment
#     template_name = 'flow_blog/blog_details.html'
#     success_url = reverse_lazy('blog_details')

#     def test_func(self):
#         comment = self.get_object()
#         if self.request.user == comment.author:
#             return True
#         else:
#             return False

# def delete_comment(request, pk):
#     post = BlogPost.objects.all()
#     comment = Comment.objects.filter(id=pk)
#     if request.user == comment.author:
#         comment.delete()
#         messages.success('deleted comment')
#         return HttpResponseRedirect(reverse('blog_page'))
#     else:
#         print('no no')
   

def delete_comment(request, comment_id):
    users_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == users_comment.author:
        users_comment.delete()
        messages.success(request, 'COMMENT IS DELETED') 
        # return HttpResponseRedirect(reverse('blog_page'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "CAN'T DELETE COMMENT(YOU ARE NOT CREATOR) ")
        # return HttpResponseRedirect(reverse('blog_page'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))