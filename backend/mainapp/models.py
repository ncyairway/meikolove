from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户模型
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

# 帖子模型
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(upload_to='photos/')
    content = models.TextField()

# 评论模型
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

# 投票模型
class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=10)  # Example: "美丽" or "帅气"

# 打赏模型
class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# 商品模型
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
