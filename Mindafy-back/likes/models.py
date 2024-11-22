from django.db import models
from accounts.models import User
from tests.models import Test
from comments.models import Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, related_name='test_like')
    comment = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, related_name='comment_like')