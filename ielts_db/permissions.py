
from rest_framework import permissions
from .models import Account, Group

class JustAdmin(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "ADMIN":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "ADMIN":
            return True
        return False

class JustTeacher(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "TEACHER":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "TEACHER":
            return True
        return False

class JustStudent(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "STUDENT":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        usr = Account.objects.get(username=request.user.username)
        print(usr)
        name_group = usr.idgroup.name
        if name_group == "STUDENT":
            return True
        return False