import random

from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import random_string


class TokenView(APIView):
    @staticmethod
    def get(request):
        data = {"access_token": random_string(32), "expires_in": 7200}
        return Response(data)


class GetTicketView(APIView):
    @staticmethod
    def get(request):
        data = {
            "errcode": 0,
            "errmsg": "ok",
            "ticket": random_string(86),
            "expires_in": 7200,
        }
        return Response(data)


class InfoView(APIView):
    @staticmethod
    def get(request):
        subscribe = random.randint(0, 1)
        if subscribe:
            data = {
                "subscribe": subscribe,
                "openid": request.query_params["openid"],
                "nickname": random_string(6),
                "sex": 1,
                "language": "zh_CN",
                "city": "广州",
                "province": "广东",
                "country": "中国",
                "headimgurl": "http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc5"
                "6vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
                "subscribe_time": 1382694957,
                "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL",
                "remark": "",
                "groupid": 0,
                "tagid_list": [128, 2],
                "subscribe_scene": "ADD_SCENE_QR_CODE",
                "qr_scene": 98765,
                "qr_scene_str": "",
            }
        else:
            data = {"subscribe": subscribe}
        return Response(data)
