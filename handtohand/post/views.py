import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Area, Post
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
        title = request.POST.get('title')
        content = request.POST.get('content')
        point = request.POST.get('point')
        area = request.POST.get('area')
        user = request.POST.get('user')
        post = Post(
            title=title,
            content=content,
            point=point,
            numChat=0,
            user=user,
            area=area
        )
        post.save()
    return JsonResponse({'message': '작성 성공'})

def post_list(request):
    if request.method == "POST":
        # data = json.loads(request.body)
        # area.name = data["name"]
        # posts = list(Post.objects.filter(name__contains=name).values("name"))
        area = request.POST.get('area')
        posts = list(Post.objects.filter(area=area))
        context = {
            "posts": posts
        }
        return JsonResponse(context=context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    # post.save()
    context = {
        "post": post,
    }
    return JsonResponse(context=context)

    # post.objects.filter(id)

# 신고 올리기
def declare_post(request, pk):
    post = Post.objects.get(id=pk)
    post.declare= post.declare+1
    post.save()
