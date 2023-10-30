from django.http import JsonResponse
from .utils.parser import parse_from_json


def library_view(req):
    return JsonResponse(parse_from_json("book_library.json"))