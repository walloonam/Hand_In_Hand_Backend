from datetime import datetime

from django.contrib.auth import authenticate
from django.core import serializers
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt

from .decorators import email_verification_required
from .models import User, EmailVerification, Token, Attendance
from post.models import Area

from .utils import send_verification_email
def email_validation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            email = EmailVerification(email=email)
            token = email.generate_verification_token()
            email.save()
            verification_url = f"http://127.0.0.1:8000/api/user/verify/{email.pk}/{token}/"

            content= 'hi'
            subject = 'Verify Your Email'
            message = render_to_string('email/email_confirmation_signup_message.html', {'verification_url': verification_url, 'email': email.email})
            from_email = 'jh37106@gmail.com'
            recipient_list = [email.email]

            send_mail(subject,content, from_email, recipient_list,html_message=message )
            return HttpResponse("이메일 보내기 성공")

        except Exception as e:
            print(e)
            return HttpResponse("이메일 보내기 실패")
    elif request.method == "GET":
        email = request.GET.get('email')

def verify_email(request, pk, token):
    try:
        email = EmailVerification.objects.get(pk=pk)
        email.verify()
        email.save()

    except:
        return HttpResponse("error user 오류")


@csrf_exempt
@email_verification_required
def user_signup(request):
    timezone.deactivate()
    if request.method == 'POST':
        try:
            data = request.POST  # 클라이언트에서 전달된 데이터를 받아옵니다.
            #user 비밀번호 :aqazcmcqyoxnjdlx
            # 데이터 유효성 검사
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            nickname = data.get('nickname')
            date_of_birth_str = data.get('date_of_birth')
            address = data.get('address')
            area = data.get('area')

            if not all([name, email, password, nickname, date_of_birth_str, address]):
                return JsonResponse({"message": "누락된 필수 데이터가 있습니다."}, status=400)

            date_of_birth = parse_date(date_of_birth_str)

            if len(date_of_birth_str) == 6 and date_of_birth_str.isdigit():
                date_of_birth = datetime.strptime(date_of_birth_str, "%y%m%d")

            area = Area.objects.get(name=area)
            # User 객체 생성
            user = User(
                name=name,
                email=email,
                password=password,
                nickname=nickname,
                date_of_birth=date_of_birth,
                address=address,
                point=1000,
                area=area
            )
            emailVerify=EmailVerification.objects.get(email=email)
            print (emailVerify.verification())
            if(emailVerify.verification()):
                user.full_clean()  # 데이터 유효성 검사 실행
                user.save()
                emailVerify.delete()
            else:
                return HttpResponse("이메일 인증 실패")

            return JsonResponse({"message": "success"}, status=201)
        except ValidationError as e:
            return JsonResponse({"message": str(e)}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({"message": "서버 오류가 발생했습니다."}, status=500)
    else:
        return JsonResponse({"message": "잘못된 요청입니다."}, status=400)


def login(request):
    if request.method=="POST":
        try:
            data=request.POST
            email=data.get("email")
            password=data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                token = Token(email=user.email)
                token.generate_verification_token()
                return JsonResponse({'token': token.token})
            else:
                return HttpResponse("아이디 비밀번호를 확인하세요")
        except Exception as e:
            print(e)


def logout(request):
    if request.method=="POST":
        token = request.POST.get("token")
        token = Token.objects.get(token=token)
        token.delete()
        return JsonResponse({"message":"complete"})


def find_email(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        birth = data.get("birth")
        user = User.objects.filter(name=name)
        if user is not None:
            for u in user:
                if u.date_of_birth == birth:
                    context={
                        "email": u.email
                    }
                    return JsonResponse(context=context)
                else:
                    return HttpResponse("생일이 일치 하지 않 습니다")
        else:
            return HttpResponse("이름을 다시 입력해 주세요")


def find_password(request):
    if request.method == "POST":
        data = request.POST


def password_reset(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        new_password = data.get("new_password")
        user = User.objects.get(email=email)
        user.password = new_password
        user.save()
        context = {"reuslt": "success"}
        return JsonResponse(context)
    else:
        context = {"reuslt": "fail"}
        return JsonResponse(context)

def user_info(request):
    if request.method == "POST":
        token = request.POST.get("token")
        email = Token.objects.get(token=token)
        user = User.objects.get(email=email.email)
        users = serializers.serialize("json", user)
        return JsonResponse(users)

def check_nickname(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        user = User.objects.get(nickname=nickname)
        if user is not None:
            return JsonResponse({"message": "fail"})
        else:
            return JsonResponse({"message": "success"})

def check_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        if user is not None:
            return JsonResponse({"message": "fail"})
        else:
            return JsonResponse({"message": "success"})


def attend_check(request):
    current_date = datetime.now().date()
    check_date=False
    if request.method == "POST":
        token = request.POST.get("token")
        token = Token.objects.get(token=token)
        check = Attendance.objects.filter(user=token.email)
        for ch in check:
            if ch.date == current_date:
                check_date=True
        if check_date:
            return JsonResponse({"message": "already done"})
        else:
            attend = Attendance(
                user=token.email
            )
            attend.save()
            return JsonResponse({"message": "success"})

