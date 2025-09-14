from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Create groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Get book content type
        content_type = ContentType.objects.get_for_model(Book)

        # Get permissions
        can_view = Permission.objects.get(codename="can_view", content_type=content_type)
        can_create = Permission.objects.get(codename="can_create", content_type=content_type)
        can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
        can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

        # Assign permissions to groups
        editors.permissions.set([can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully!"))
