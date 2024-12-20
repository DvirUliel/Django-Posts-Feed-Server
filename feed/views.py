from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # use the father func to get the db
        context["posts"] = Post.objects.all().order_by('-id') # add to the db
        return context
    
class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "post.html"
    form_class = PostForm
    success_url = '/' # home

    def dispatch(self, request, *args, **kwargs): # to save the request for the output message
        self.request=request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_objects = Post.objects.create(
            title = form.cleaned_data["title"],
            image = form.cleaned_data["image"]
        )
        messages.add_message(self.request, messages.SUCCESS, "Successful to upload the post!")
        return super().form_valid(form)