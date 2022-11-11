from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'app1/home.html',context)

class PostListView(ListView):
    model= Post
    template_name = 'app1/home.html'
    context_object_name = 'post'
    ordering = ['-date_of_post']

class PostDetailView(DetailView):
    model= Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model= Post
    fields = ['topic','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Post
    fields = ['topic','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Post
    success_url: '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def room(request):
    return render(request,'app1/about.html',{'title':'About'})

