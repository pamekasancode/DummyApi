from django.http import JsonResponse
from .utils.parser import parse_from_json


def library_view(req):
    return JsonResponse(parse_from_json("book_library.json"), safe=False)


def albums_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "albums.json"), safe=False)


def comments_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "comments.json"), safe=False)


def photos_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "photos.json"), safe=False)

def posts_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "posts.json"), safe=False)

def todos_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "todos.json"), safe=False)

def users_view(req):
    return JsonResponse(parse_from_json("json_placeholder", "users.json"), safe=False)
