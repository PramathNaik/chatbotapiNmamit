from django.http import JsonResponse


def page_not_found_view(request, exception):
    obj = {"message":"Not Defined"}
    return JsonResponse(obj)