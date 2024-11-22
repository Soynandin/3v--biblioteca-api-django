# Em core/custom_permissions.py
from rest_framework.permissions import BasePermission

class IsColecionador(BasePermission):
    def has_permission(self, request, view):
        # Confirma apenas que o usuário está autenticado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Apenas o colecionador da coleção pode editá-la
        return obj.colecionador == request.user
