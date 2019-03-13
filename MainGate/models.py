from django.db import models

# Create your models here.


class User(models.Model):
    account = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    create_time = models.DateTimeField(auto_created=True)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "account:{},email:{}".format(self.account, self.email)

    class Meta:
        ordering = ['login_time']


if __name__ == "__main__":
    print('is go')