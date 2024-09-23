from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def candidate_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_candidate:
            return Response({"msg":"Only candidates are allowed to login", "status" :status.HTTP_403_FORBIDDEN},
                            status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
