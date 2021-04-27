from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from perdorues.models import Perdorues
from .models import Post, Koment, Kategori
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detailview.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    #form_class = PostForm
    template_name = 'add_post.html'
    fields = ('titull','katekoria', 'trupi')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        print(10)
        print(request.body)
        print(request.data)
        return super().post(request, args, kwargs)


class AddKategoriView(CreateView):
    model = Kategori
    template_name = 'add_kategori.html'
    fields = '__all__'

@login_required
def CreateKomentView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    komentuesi = request.user
    trupi = request.POST['text_id']
    komenti = Koment.objects.create(post=post, komentues=komentuesi, body=trupi)
    komenti.save()
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ['titull', 'trupi']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



