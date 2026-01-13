from rest_framework import permissions
from products.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_class = [permissions.IsAdminUser, IsStaffEditorPermission]