from django.contrib.auth.mixins import AccessMixin


class UserIsArticleAuthor(AccessMixin):
    """Deny a request with a permission error if the user who sent the request is not the author of the article."""
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
