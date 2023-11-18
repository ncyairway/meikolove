from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Post, Comment, Vote, Reward, Product
from .serializers import UserSerializer, PostSerializer, CommentSerializer, VoteSerializer, RewardSerializer, ProductSerializer

# 用户视图集
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 帖子视图集
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 评论视图集
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# 投票视图集
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

# 打赏视图集
class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

# 商品视图集
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
