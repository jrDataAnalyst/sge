from rest_framework.permissions import DjangoModelPermissions

class StrictDjangoModelPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):
        # Verifica se o usuário tem permissão para acessar a view
        if not super().has_permission(request, view):
            return False

        # Aqui você verifica se o usuário está no grupo específico
        # Substitua 'Grupo X' pelo nome do seu grupo
        if request.user.groups.filter(name='Release_view').exists():
            return True
        
        return False
