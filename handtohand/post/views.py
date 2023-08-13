import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Area, Post
from .forms import PostForm
from ..user.models import Token, User


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



# def create_post(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         point = request.POST.get('point')
#     return JsonResponse({'message': '작성 성공'})
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        point = request.POST.get('point')
        area = request.POST.get('area')
        token = request.POST.get('token')
        token = Token.objects.get(token=token)
        user = token.nickname
        post = Post(
            title=title,
            content=content,
            point=point,
            numChat=0,
            user=user,
            area=area
        )
        post.full_clean()  # 데이터 유효성 검사 실행
        post.save()
    return JsonResponse({'message': '작성 성공'})

def post_list(request):
    if request.method == "POST":
        # data = json.loads(request.body)
        # area.name = data["name"]
        # posts = list(Post.objects.filter(name__contains=name).values("name"))
        area = request.POST.get('area')
        posts = Post.objects.filter(area=area)
        post_list=serializers.serialize('json',posts)

        return JsonResponse(post_list)

def post_delete(request, pk):
    if request.method == "DELETE":
        post = Post.objects.get(id=pk)
        post.delete()
        return JsonResponse({"message" : "complete"})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    # post.save()
    context = {
        "id" : post.pk,
        "title" : post.title,
        "content" : post.content,
        "numChat" : post.numChat,
        "point" : post.point,
        "created_at" : post.created_at,
        "area" : post.area
    }
    return JsonResponse(context)
    # post.objects.filter(id)


# 신고 올리기
def declare_post(request, pk):
    post = Post.objects.get(id=pk)
    post.declare = post.declare+1
    post.save()

#채택하기




