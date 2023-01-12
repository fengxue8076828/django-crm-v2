from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class OrganizerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_organizer :
            return redirect("/leads")
        return super().dispatch(request, *args, **kwargs)