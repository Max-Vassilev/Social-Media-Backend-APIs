from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        if len(self.content) < 20:
            return f"Post: {self.content}"
        else:
            return f"Post: {self.content[0: 15]}..."


class Like(models.Model):
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.to_post.content) < 20:
            return f"Like for post: {self.to_post} By: {self.user}"
        else:
            return f"Like for: {self.to_post.content[0: 15]}..."
