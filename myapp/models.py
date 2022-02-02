from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
# from .managers import UserManager
#from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    
    def __str__(self):
        return self.name

class Department(models.Model):
    emp_name=models.ForeignKey(employee,on_delete=models.CASCADE,null=True)
    d_name=models.CharField(max_length=20)

# now we have to regiter our model in admin.py file first import model than ragister        


#  # custom user
# class User(BaseModel,AbstractBaseUser,PermissionsMixin):
#     user_role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
#     username = models.CharField(max_length=50,null=True,blank=True)
#     email = models.EmailField(unique = True)         
#     password = models.CharField(max_length=255,null=True,blank=True)               
#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255,null=True,blank=True)
#     phone_number = models.CharField(max_length = 15,null=True,blank=True)
#     dob = models.DateField(null=True)
#     gender = models.CharField(choices = GENDER_CHOICE, max_length = 20,null=True,blank=True)
#     address = models.TextField(null=True,blank=True)
#     profile_picture = models.FileField(upload_to ='profile',null = True,blank = True)
#     civil_id = models.CharField(max_length=12,null=True,blank=True)
#     social_id = models.TextField(null=True,blank=True)
#     unique_id = models.CharField(max_length=255,default='',null=True,blank = True)
#     # registration_date = models.DateTimeField(default=timezone.now,null=True)
#     token=models.CharField(max_length=60, null=True, blank=True)

#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)


#      # str function to return name instead of object
#     def __str__(self):
#         """Return full name in representation instead of objects"""
#         return self.email
    

#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#     class Meta:
#         """A meta object for defining name of the user table"""
#         db_table = "user" 
#         ordering =   ["-created_at"]
        

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name']

#     objects = UserManager()
