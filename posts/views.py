from django.shortcuts import render, Http404, HttpResponse,get_object_or_404 ,redirect,HttpResponseRedirect,redirect,reverse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q
from django.contrib.admin.views.decorators  import staff_member_required
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        form = PostForm(request.POST or None ,request.FILES or None)
        if form.is_valid():
            instace = form.save(commit=False)
            instace.user = request.user
            instace.save()
            messages.success(request, 'تم انشاء المقال بنجاح')
            return HttpResponseRedirect(instace.get_absolute_url())
    else:
        messages.error(request, 'لم يتم انشاء المقال هنالك خطا يرجي مراجعته')
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'post/create-post.html', context)

def post_home(request):
    # posts = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
    posts = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        posts = Post.objects.all()
    
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)|
            Q(user__username__icontains=query)
            ).distinct()
    paginator = Paginator(posts, 5)  # Show 25 contacts per page.
    page_request_var = 'page-of'
    page_number = request.GET.get(page_request_var)
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'page_request_var': page_request_var
            }
    # if request.user.is_authenticated:
    #     context = {
    #         'title': 'title admin'
    #     }
    # else:
    #     context = {
    #         'title': 'title user'
    #     }
    return render(request, 'post/post_list.html', context)
    

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    shareing_string = quote_plus(instance.content)
    # content_type = ContentType.objects.get_for_model(Post)
    # obj_id = instance.id
    # comments = Comment.objects.filter(content_type=content_type,object_id=obj_id)
    # comments = Comment.objects.filter_by_instance(instance)
    comments = instance.comments
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id':instance.id
    }
    form = CommentForm(request.POST or None,  initial=initial_data)
    if form.is_valid():
        # print(form.cleaned_data)
        c_type = form.cleaned_data.get("content_type")
        # c = c_type.split('|')[1]
        print("===", c_type)
        content_type = ContentType.objects.get(model=c_type)
        # content_type = ContentType.objects.get_for_model(instance)
        
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = request.POST.get("parent_id")
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()


        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent = parent_obj
        )

        # return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        

    context = {
        'instance': instance,
        'shareing': shareing_string,
        'comments': comments,
        'comment_form': form,
        
            }
    
    # return render(request, 'post/post_detail.html', context)
    if request.is_ajax():
        html = render_to_string('post/comment.html',context,request=request)
        return JsonResponse({'form':html})
    
    return render(request, 'post/post_detail.html', context)

@staff_member_required
def post_update(request, slug):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    post = get_object_or_404(Post, slug=slug)
    # if request.method == "POST":
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=post)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        form.save()
        # instance.id = post_detail
        # instance.save() 
        messages.success(request, 'تم حفظ التعديل')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'لم يحفظ')
        # form = PostForm()

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'post/edit-post.html', context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'success delete')
    return redirect('posts:post_list')
