from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from common.utils import random_string


class Oauth2AccessTokenView(APIView):
    @staticmethod
    def get(request):
        data = {
            "access_token": random_string(100),
            "expires_in": 7200,
            "refresh_token": random_string(100),
            "openid": random_string(28),
            "scope": "SCOPE"
        }
        return Response(data)


class UserInfoView(APIView):
    @staticmethod
    def get(request):
        data = {
            "openid": request.query_params["openid"],
            "nickname": random_string(6),
            "sex": "1",
            "province": "广东",
            "city": "深圳",
            "country": "中国",
            "headimgurl": "http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaF"
                          "qAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46",
            "privilege": []
        }
        return Response(data)


class TestView(APIView):
    @staticmethod
    def get(request):
        return redirect("http://127.0.0.1:9000/nezha/server/log-test/")
