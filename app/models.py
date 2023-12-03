from django.db import models
import re



class UserManager(models.Manager):
    def validator(self,POST_data):
        errors = {}
        if len(POST_data['first_name']) < 2:                                        #first name length
            errors['first_name'] = 'your first name should be at least 4 characters'

        if len(POST_data['last_name']) < 2:                                         #last name length
            errors['last_name'] = 'your last name should be at least 4 characters'

        if User.objects.filter(email = POST_data['email']):                         #account already exists? unique email
            errors['account_exsits'] = 'email address used for another account!'

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  #email syntax valid?
        if not email_regex.match(POST_data['email']):
            errors['vaild_email'] = "Invalid email address!"

        if len(POST_data['password']) < 8:                                          #password length 8
            errors['password_len'] = 'your password should be at least 8 characters'

        if POST_data['password2'] != POST_data['password']:                        #password confirmation
            errors['password_confirm'] = 'password and password confirmation does not match!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
###################################################################End User table with validations