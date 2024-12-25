from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ["is_done", "datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=255)
