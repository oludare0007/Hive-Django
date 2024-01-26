from .models import Post  # Import the Post model

def posts_processor(request):
    latest_posts = Post.objects.order_by('-date_posted')[:5]
    return {'posts': latest_posts}