from django.shortcuts import render, get_object_or_404,Http404, HttpResponseRedirect
from .models import Comment
from .forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


@login_required
def comment_delete(request, id):
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
        raise Http404
     
    
    if request.method == "POST":
        print("+++", obj.content_object)
        parent_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, 'تم المسح بنجاح')
        return HttpResponseRedirect(parent_url)
    context = {
        'object':obj
    }
    return render(request, 'comments/confirm.html', context)
    

def comment_thread(request, id):
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent

    content_object = obj.content_object
    content_id = obj.content_object.id
    initial_data = {
        'content_type':obj.content_type,
        'object_id': obj.object_id
        # 'content_type': content_object.get_content_type,
        # 'object_id': content_id
    }
    form = CommentForm(request.POST or None and request.is_ajax(), initial=initial_data)
    if form.is_valid():
        # print(form.cleaned_data)
        c_type = form.cleaned_data.get("content_type")
        # c = c_type.split('|')[1]
        # print(c_type)
        content_type = ContentType.objects.get(model='Post')

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
            parent=parent_obj
        )

        # return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


    context = {
        'comment': obj,
        'form': form,
    }
    if request.is_ajax():
        html = render_to_string('comments/replay-comment.html',context,request=request)
        return JsonResponse({'form':html})
    return render(request,'comments/comment_thread.html',context)
