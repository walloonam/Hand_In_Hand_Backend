from django.http import JsonResponse
from .models import EmailVerification


def email_verification_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.emailverification.is_verified:
            return JsonResponse({"message": "이메일 인증이 필요합니다."}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
