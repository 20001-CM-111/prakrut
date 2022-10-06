from django.db import models
from django.contrib.auth.models import User

class Userdata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Status=models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class Vegetable(models.Model):
    Name = models.CharField(max_length=30,primary_key=True)
    Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default="")

    def __str__(self):
        return self.Name

class Product(models.Model):
    product=models.CharField(max_length=30)
    user=models.CharField(max_length=100)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='null')
    class Meta:
        unique_together = ('product', 'user',)
    def __str__(self):
        return self.product

class Tomato(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Tomato')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Okra(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Okra')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Brinjal(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Brinjal')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Chillies(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Chillies')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Cabbage(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Cabbage')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class RunnerBeans(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='RunnerBeans')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Cauliflower(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Cauliflower')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Capsicum(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Capsicum')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class GreenBeans(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='GreenBeans')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class DrumStick(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='DrumStick')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Spinach(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Spinach')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Amaranthus(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Amaranthus')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Coriander(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Coriander')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class CurryLeaves(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='CurryLeaves')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class IvyGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='IvyGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class RidgeGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='RidgeGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class BitterGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='BitterGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class SnakeGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='SnakeGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class SpineGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='SpineGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class BottleGourd(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='BottleGourd')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class YellowCucumber(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='YellowCucumber')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Potato(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Potato')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Sweetpotato(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Sweetpotato')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Ginger(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Ginger')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Taro(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Taro')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Carrot(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Carrot')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Radish(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Radish')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Beetroot(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Beetroot')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Onion(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name=models.ForeignKey(Vegetable,on_delete=models.CASCADE,default='Onion')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)

class Garlic(models.Model):
    Price=models.IntegerField()
    user=models.CharField(max_length=100,unique=True)
    name = models.ForeignKey(Vegetable, on_delete=models.CASCADE,default='Garlic')
    class Meta:
        unique_together = ('Price', 'user',)
    def __str__(self):
        return str(self.Price)








# Create your models here.
