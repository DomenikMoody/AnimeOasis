from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from app.models import User
from app.serializers import UserSerializer

#TODO: refactor into class-based views
# the csrf_exempt decorator is just for testing.
# Once we get the redux store up, we will remove
# the decorators and grab the csrf_token from cookies
# before calling the fetch from frontend
# (django auto assigns csrf cookie)


# TODO: only the user in question should be able to edit, delete
@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request):
    """
    list all users, or create a new user
    """
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, edit, or delete one specific User
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        error = {'message': f'User with id {pk} does not exits'}
        return JsonResponse(error, status = 404)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else: return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)
