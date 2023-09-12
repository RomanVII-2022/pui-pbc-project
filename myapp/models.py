from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, middle_name, last_name, force_number, phone_number, password=None):

        user = self.model(
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            force_number=force_number,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, middle_name, last_name, force_number, phone_number, password=None):
        user = self.create_user(
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            force_number=force_number,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    force_number = models.CharField(max_length=200, unique=True)
    phone_number = PhoneNumberField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "middle_name", "last_name", "force_number", "phone_number"]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



class  Case(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    sno = models.CharField(max_length=200)
    occurence_book_no = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    complainant_name = models.CharField(max_length=200)
    offence = models.TextField()
    investigating_officer = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    remarks = models.TextField(null=True, blank=True)
    results = models.TextField(null=True, blank=True)
    case_file = models.ImageField(upload_to='caseFiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.occurence_book_no + ' - ' + self.police_station 


class PendingBeforeCourt(Case):
    charge_registry_no = models.CharField(max_length=200)
    court_file_number = models.CharField(max_length=200)
    accused_name = models.CharField(max_length=200)
    hearing_mention_date = models.DateTimeField()
    court = models.CharField(max_length=200)
    

class PBCLog(models.Model):
    kase = models.ForeignKey(PendingBeforeCourt, on_delete=models.DO_NOTHING) 
    title = models.CharField(max_length=200) 
    comment = models.TextField(null=True, blank=True)
    file_upload = models.FileField(null=True, blank=True)  
    hearing = models.BooleanField(default=False)
    mention = models.BooleanField(default=False)
    hearing_mention_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kase.occurence_book_no


class PendingUnderInvestigation(Case):
    actual_date = models.DateField()
    suspect_name = models.CharField(max_length=200)


class PUILog(models.Model):
    kase = models.ForeignKey(PendingUnderInvestigation, on_delete=models.DO_NOTHING)  
    title = models.CharField(max_length=200) 
    comment = models.TextField(null=True, blank=True)
    file_upload = models.FileField(null=True, blank=True)  
    hearing = models.BooleanField(default=False)
    mention = models.BooleanField(default=False)
    hearing_mention_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kase.occurence_book_no
    


