from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Category
from django.core.paginator import Paginator


# Create your views here.

@login_required
def home(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    posts = Post.objects.select_related('author').prefetch_related('categories').all()

    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)

    if category_id:
        posts = posts.filter(categories__id=category_id)

    paginator = Paginator(posts.order_by('-created_at'), 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    categories = Category.objects.all()

    return render(request, 'blog/home.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'query': query,
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
