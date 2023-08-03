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
        title = request.POST.get('title')
        content = request.POST.get('content')
        point = request.POST.get('point')
    return JsonResponse({'message': '작성 성공'})

def post_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        area.name = data["name"]
        posts = list(Post.objects.filter(name__contains=name).values("name"))
        context = {
            "posts": posts
        }
        return JsonResponse(context,{
            "id": 1,
			"title" : "도와주세요",
			"content" : "배고파여",
			"point" : 500,
			"numChat" : 5,
			"area" : "동작구"
        })


def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    post.save()
    context = {
        "post": post,
    }
    return JsonResponse(context,{
        "id" : "1",
        "title": "배고파요",
        "content": "안녕하세여",
        "numChat": 5,
        "point": 500,
        "created_at" : "2023-07-21T23:00:50Z",
        "area" : "동작구"
    })

    # post.objects.filter(id)