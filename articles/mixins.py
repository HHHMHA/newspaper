from django.contrib.auth.mixins import AccessMixin


class UserIsArticleAuthorMixin(AccessMixin):
    """Deny a request with a permission error if the user who sent the request is not the author of the article."""
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AddUserToKwargsMixin:
    """Adds the user who sent the request to the kwargs so it can be accessed outside for example in forms"""
    def get_form_kwargs(self):
        kwargs = super(AddUserToKwargsMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs