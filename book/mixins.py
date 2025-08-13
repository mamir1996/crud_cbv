from django.http import Http404

class UserBookPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise Http404("You do not have permission to access this book.")
        return super().dispatch(request, *args, **kwargs)
