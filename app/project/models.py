from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Project(models.Model):
    project_uuid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    project_name=models.CharField(_('project_name'),max_length=255,blank=True,null=True)
    updated_at=models.DateTimeField(_('updated_at'), null=False,blank=False,default=timezone.now)
    is_active=models.BooleanField(_('is_active'),default=True)
    class Meta:
        ordering = ["-id"]
