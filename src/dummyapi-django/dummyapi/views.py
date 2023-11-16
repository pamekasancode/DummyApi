from django.http import JsonResponse
from .utils.parser import parse_from_json
from .api_collections import *

def library_view(req):
    return JsonResponse(BOOK_LIBRARY, safe=False)

def albums_view(req):
    return JsonResponse(ALBUMS, safe=False)


def comments_view(req):
    return JsonResponse(COMMENTS, safe=False)


def photos_view(req):
    return JsonResponse(PHOTOS, safe=False)

def posts_view(req):
    return JsonResponse(POSTS, safe=False)

def todos_view(req):
    return JsonResponse(TODOS, safe=False)

def users_view(req):
    return JsonResponse(USERS, safe=False)


# On developement
# def library_view(req):
#     return JsonResponse(parse_from_json("book_library.json"), safe=False)


# def albums_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "albums.json"), safe=False)


# def comments_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "comments.json"), safe=False)


# def photos_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "photos.json"), safe=False)

# def posts_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "posts.json"), safe=False)

# def todos_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "todos.json"), safe=False)

# def users_view(req):
#     return JsonResponse(parse_from_json("json_placeholder", "users.json"), safe=False)
