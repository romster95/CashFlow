from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    email = models.EmailField(verbose_name="Почта")
    password = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Баланс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Користувач"
        verbose_name_plural="Користувачі"
        ordering=['name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Назва")
    picture = models.ImageField(upload_to='catIcons')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Категорія"
        verbose_name_plural="Категорії"
        ordering = ['id']


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}"

