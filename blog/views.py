from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy, path


from django.contrib.auth.views import LoginView, LogoutView

# importacion de login required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'blog_list.html', context)
    
#Listview de admin
# login required para BlogListViewAdmin


class BlogListViewAdmin(LoginRequiredMixin, View):
    login_url = reverse_lazy('blog:login')  # Utiliza el nombre de la URL definido en urls.py
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog_admin.html', context)
    
class BlogCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('blog:login')
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            image = form.cleaned_data.get('image')

            # Crea la instancia del modelo y asigna los valores
            post_instance = Post(title=title, content=content, image=image)
            post_instance.save()

            return redirect('blog:home')

        context = {'form': form}
        return render(request, 'blog_create.html', context)
    
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        
        context={
            'post':post
        }
        return render(request, 'blog_detail.html', context)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('blog:login')
    redirect_field_name = 'redirect_to'
    model=Post
    fields=['title', 'content']
    template_name='blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('blog:login')
    redirect_field_name = 'redirect_to'
    
    model=Post
    template_name='blog_delete.html'
    success_url=reverse_lazy('blog:home')



class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nombre de tu plantilla de inicio de sesión

    def get_success_url(self):
        # Redirigir a la vista 'detail' de cualquier post
        return reverse_lazy('blog:homeadmin')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('blog:home')  # Redirección después del cierre de sesión
