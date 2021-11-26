from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """A study topic that the user will create and is learning about """
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # the attribute auto_now_add=True tells django to automatically set this to current date and time
    # whenever the user creates a new Topic
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """returns a string represantation of the model"""
        return self.text

class Entry(models.Model):
    """something learned abt the topic"""
    # connect each entry to a specific Topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # the on_delete=models.CASCADE tells django that
    # if a topic is deleted all the entries associated with it are deleted as well
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """extra infomation for managing the model"""
        verbose_name_plural = 'entries'
        # tells django to refer to multiple Entrys as entries

    def __str__(self):
        """returns a string represantation of the model"""
        if len(self.text) >= 50:
            return f"{self.text[:50]}...."
        else:
            return self.text