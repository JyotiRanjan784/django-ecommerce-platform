from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    head0 = models.CharField(max_length=500, default='')
    chead0 = models.CharField(max_length=5000, default='')
    head1 = models.CharField(max_length=500, default='')
    chead1 = models.CharField(max_length=5000, default='')
    head2 = models.CharField(max_length=500, default='')
    chead2 = models.CharField(max_length=5000, default='')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images/', blank=True, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} on {self.post.title}"
