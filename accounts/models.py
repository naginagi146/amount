from django.db import models
from django.utils import timezone


class Item(models.Model):

    CATEGORY_CHOICES = (
        ('shirt', 'シャツ'),
        ('pant', 'パンツ'),
        ('Tshirt', 'Tシャツ'),
    )
    CONDITION_CHOICES = (
        ('s', 'S'),
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    )

    name = models.CharField('ブランド', max_length=50)
    item_model = models.CharField('モデル名', max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES)
    text = models.TextField('備考')

    def __str__(self):
        return self.name


class Image(models.Model):
    src = models.ImageField('添付画像')
    target = models.ForeignKey(
        Item, verbose_name='アイテム',
        blank=True, null=True,
        on_delete=models.CASCADE
    )





# class Type (models.Model):
#     name = models.CharField('ブランド', max_length=50)
#     item_model = models.CharField('モデル名', max_length=50)
#     category = models.ForeignKey(Item, on_delete=models.CASCADE ,related_name='category')
#     condition = models.ForeignKey(Item, on_delete=models.CASCADE ,related_name='condition')
#     text = models.TextField('備考')

#     def __str__(self):
#         return self.name + ' ' + self.club.name


# class Item_model (models.Model):
#     item_model = models.CharField('モデル名', max_length=50)

#     def __str__(self):
#         return self.name


# class Category (models.Model):
#     name = models.CharField('アイテムタイプ', max_length=50)

#     def __str__(self):
#         return self.name


# class Condition (models.Model):
#     name = models.CharField('状態ランク', max_length=5)

#     def __str__(self):
#         return self.name


# class Comment (models.Model):
#     text = models.TextField('備考')

#     def __str__(self):
#         return self.text
# # Create your models here.
