from django.db import models

class Brand (models.Model):
    name = models.CharField('ブランド', max_length=50)

    def __str__(self):
        return self.name

class Item_model (models.Model):
    name = models.CharField('モデル名', max_length=50)

    def __str__(self):
        return self.name

class Category (models.Model):
    name = models.CharField('アイテムタイプ', max_length=50)

    def __str__(self):
        return self.name

class Condition (models.Model):
    name = models.CharField('状態ランク', max_length=5)

    def __str__(self):
        return self.name

class Comment (models.Model):
    text = models.TextField('備考')

    def __str__(self):
        return self.text
# Create your models here.
