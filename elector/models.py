from django.db import models
import uuid


def front_upload_to(instance, filename) :
    return 'elector/%s/%s' % (instance.elector_id, 'front' + filename)


def left_upload_to(instance, filename) :
    return 'elector/%s/%s' % (instance.elector_id, 'left' + filename)


def right_upload_to(instance, filename) :
    return 'elector/%s/%s' % (instance.elector_id, 'right' + filename)


class Elector(models.Model):

    SEXE_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    elector_id = models.CharField(max_length=255,null=True,unique=True,editable=False)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    front_picture = models.ImageField(upload_to=front_upload_to)
    left_side_picture = models.ImageField(upload_to=left_upload_to)
    right_side_picture = models.ImageField(upload_to=right_upload_to)
    sexe = models.CharField(max_length=255,choices=SEXE_CHOICES, null=True)
    date_of_issuance = models.DateField(auto_now_add=True)
    date_of_expire = models.DateField(null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs) :
        if not self.pk :
            self.elector_id = str(uuid.uuid4())[0:10]
        super(Elector, self).save(*args, **kwargs)


class File(models.Model):
    file = models.ImageField(blank=False, null=False)
    electorId = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.file.name