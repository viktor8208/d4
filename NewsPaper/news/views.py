from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class PostDetail(DetailView):

    model = Post

    template_name = 'post.html'

    context_object_name = 'post'


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_time'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10


class PostFilterList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

   # def form_valid(self, form):
    #    post = form.save(commit=False)
    #    post.category_type = 'NEWS'
     #   return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

   # def form_valid(self, form):
    #    post = form.save(commit=False)
    #    post.category_type = 'NW'
    #    return super().form_valid(form)



class PostDelete(DeleteView):

    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')



