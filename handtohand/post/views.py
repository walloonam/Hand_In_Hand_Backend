from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from post.models import Area


def create_area(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            area = Area.objects.create(name=name)
            return JsonResponse({'message': '지역이 성공적으로 생성되었습니다.', 'name': area.name})
        else:
            return JsonResponse({'message': '이름을 입력해주세요.'}, status=400)


def delete_area(request, pk):
    area = get_object_or_404(Area, pk=pk)

    if request.method == 'DELETE':
        area_name = area.name
        area.delete()
        return JsonResponse({'message': '지역이 성공적으로 삭제되었습니다.', 'name': area_name})

    return JsonResponse({'message': 'POST 요청이 아닙니다.'}, status=400)
