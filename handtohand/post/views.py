from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Area
from .forms import PostForm

def create_area(request): # 지역 생성
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            area = Area.objects.create(name=name)
            return JsonResponse({'message': '지역이 성공적으로 생성되었습니다.', 'name': area.name})
        else:
            return JsonResponse({'message': '이름을 입력해주세요.'}, status=400)


def delete_area(request, pk): # 지역 삭제
    area = get_object_or_404(Area, pk=pk)

    if request.method == 'DELETE':
        area_name = area.name
        area.delete()
        return JsonResponse({'message': '지역이 성공적으로 삭제되었습니다.', 'name': area_name})

    return JsonResponse({'message': 'POST 요청이 아닙니다.'}, status=400)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(' post_detail', post.id)
        else:
            return render(request, 'create_post.html')
    else:
        return render(request, 'create_post.html')
#
def post_detail(request):
    post = Post.objects.get(id=post_id)
    post.save()
    #채팅하는 사람의 수..
    context = {
        "post": post,
        #채팅하는 사람의 수
    }
    return render(request, "post_detail.html", context)
#
def update_post(request):
    post = get_object_or_404(Job_post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.id)
        else:
            return render(request, 'create_post.html')

    else:
        return render(request, 'create_post.html', {"post": post})
#
def delete_post(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')

def post_list(request): #ajax?
    posts = list(Post.objects.all().order_by("-created_at").values("id", "title", "content")) #채팅자 수