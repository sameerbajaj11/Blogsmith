from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

# from models.py in the current package
from .models import Post

# importing loginmixin to restrict user for create blog post view.
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin
)

# importing the generic class based views aka CBVs.
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)

# from django.http import HttpResponse



def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    # attribute names below are inbuilt in django.

    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    # orders our posts from newest to oldest on our homepage
    ordering = ['-date_posted']

    # paginating. CBV already passes the context that we need in our template.
    paginate_by = 4

class UserPostListView(ListView):
    # All the posts from a particular user, will come from a url(we'll create the username
    # and the urlpattern itself.)

    # To modify the queryset, this url will return, we'll use get_query_set()

    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    # overriding thequery that this listview will be making.
    def get_queryset(self):
        # if that user exists, then we'll capture them in that user variable or the 404.
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        # filtering the posts from the user that we have got and order will get 
        # overridden as well, so will execute it inside our query
        return Post.objects.filter(author=user).order_by('-date_posted')
    
         

    


class PostDetailView(DetailView):
    # attribute names below are inbuilt in django.
    model = Post
    # here, we'll create the template according to the convention spcified above.

# Sequence of parent classes matter as priority is implemented.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # The title and content views we see on the create blog page, are due to these fields
    # specified below.
    fields = ['title', 'content'] # date_posted will be set automatically.

    def form_valid(self, form):
        # SETTING THE AUTHOR (our logged in user), BEFORE SUBMITTING OUR BLOG POST.

        # Basically, here we are setting the author before running the form validation method.

        # before you submit the form, take the instance and set the author to the current
        # logged in user.
        form.instance.author = self.request.user

        # After carriying out the step above, we can validate our form.

        # do not forget the return keyword here, otherwise you get the 'returning None'
        # error and you won't get redirected to the PostDetailView of your newly added blog.
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})