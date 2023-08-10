from .models import StaffLogin
from importlib import import_module
from django.conf import settings

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class PreventConcurrentStaffLogin:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.get_response(request)

        staff_session = request.session.session_key

        if not hasattr(request.user, 'staff_stafflogin'):
            StaffLogin.objects.create(
                staff=request.user,
                session_key=staff_session,
            )
            return self.get_response(request)

        staff_db_session = request.user.staff_stafflogin.session_key
        if staff_session != staff_db_session:
            SessionStore(staff_db_session).delete()
            request.user.staff_stafflogin.session_key = staff_session
            request.user.staff_stafflogin.save()

        return self.get_response(request)