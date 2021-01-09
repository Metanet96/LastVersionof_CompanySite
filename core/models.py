from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify



class User (AbstractUser):
    pass

# ***********************************************************************************


def generate_slug(name, model):
    name = name
    slug = slugify(name)
    num = 1
    while model.objects.filter(slug=slug).exists():
        slug = '{}-{}'.format(slug, num)
        num += 1
    return slug

# ***********************************************************************************

class Companye (models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    tin = models.CharField(max_length=50)
    about = models.TextField()
    is_deleted = models.BooleanField(default=False)

# ***********************************************************************************

class Branch (models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# ***********************************************************************************

class Staff (models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, related_name='branch')
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# ***********************************************************************************

class StaffType (models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=180, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name, StaffType)
        super().save()

# ***********************************************************************************

class Gender (models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=180, unique=True, blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name, Gender)
        super().save()

# ***********************************************************************************

class Employee (models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    cell_phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    staff_type = models.ForeignKey(StaffType, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# ***********************************************************************************

class EducationType(models.Model):
    edu_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=180, unique=True, blank=True)

    def __str__(self):
        return self.edu_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.edu_name, EducationType)
        super().save()

# ***********************************************************************************

class EmployeeEducation(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True, blank=True)
    education_type = models.ForeignKey(EducationType, on_delete=models.SET_NULL, null=True, blank=True)
    education_center = models.CharField(max_length=150, null=True, blank=True)
    edu_from_date = models.DateField(null=True, blank=True)
    edu_to_date = models.DateField(null=True, blank=True)
    document_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.education_center

# ***********************************************************************************

class EmployeeExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    work_place = models.CharField(max_length=150,null=True, blank=True)
    exp_from_date = models.DateField(null=True, blank=True)
    exp_to_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    reason_of_left = models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return self.work_place

# ***********************************************************************************

class Language(models.Model):
    lang_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=180, unique=True, blank=True)

    def __str__(self):
        return self.lang_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.lang_name, Language)
        super().save()

# ***********************************************************************************

class LanguageLevel(models.Model):
    lvl_name = models.CharField(max_length=100)

    def __str__(self):
        return self.lvl_name

# ***********************************************************************************
class EmployeeLanguage(models.Model):
    emplooyee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    language_level = models.ForeignKey(LanguageLevel, on_delete=models.SET_NULL, null=True, blank=True)
    certificate_number = models.CharField(max_length=150,null=True, blank=True)
    certificate_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.certificate_number

# ***********************************************************************************

class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='sender')
    to_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='receiver')
    subject = models.CharField(max_length=45)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

# ***********************************************************************************