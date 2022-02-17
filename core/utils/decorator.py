import jwt

from django.http  import JsonResponse
from django.conf  import settings
from json.decoder import JSONDecodeError

from users.models import User


def signin_decorator(func):
    def wrapper(self, request, *args, **kargs):
        try:
            token        = request.headers.get('Authorization', None)
            payload      = jwt.decode(token, settings.SECRET_KEY, algorithms = settings.ALGORITHM)
            user         = User.objects.get(id = payload['id'])
            request.user = user
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)
        return func(self,request,*args,**kargs)
    return wrapper