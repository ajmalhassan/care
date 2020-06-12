from care.facility.models.mixins.permissions.base import BasePermissionMixin
from care.users.models import User


class FacilityPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_bulk_upsert_permission(request):
        return request.user.is_superuser

    def has_object_read_permission(self, request):
        return (
            super().has_object_read_permission(request) or request.user.is_superuser or request.user in self.users.all()
        )

    def has_object_write_permission(self, request):
        return super().has_write_permission(request) or request.user.is_superuser or request.user in self.users.all()


class FacilityRelatedPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_write_permission(request):
        from care.facility.models.facility import Facility

        facility = False
        try:
            facility = Facility.objects.get(external_id=request.parser_context["kwargs"]["facility_external_id"])
        except Facility.DoesNotExist:
            return False
        return (request.user.is_superuser or request.user.verified) and (
            (hasattr(facility, "created_by") and request.user == facility.created_by)
            or (
                hasattr(facility, "district")
                and request.user.user_type >= User.TYPE_VALUE_MAP["DistrictAdmin"]
                and request.user.district == facility.district
            )
            or (
                hasattr(facility, "state")
                and request.user.user_type >= User.TYPE_VALUE_MAP["StateAdmin"]
                and request.user.state == facility.state
            )
        )

    def has_object_read_permission(self, request):
        return (
            super().has_object_read_permission(request)
            or request.user.is_superuser
            or request.user in self.facility.users.all()
        )

    def has_object_write_permission(self, request):
        return (
            super().has_write_permission(request)
            or request.user.is_superuser
            or request.user in self.facility.users.all()
        )
