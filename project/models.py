from django.db import models
import uuid

from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="static/images/projects", default="static/images/projects/default.jpg")
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=400, null=True, blank=True)
    source_code = models.CharField(max_length=4000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio','vote_total','title']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value="up").count()
        totalVotes = reviews.count()

        ratio = (upVotes/totalVotes) * 100
        self.vote_ratio = ratio
        self.vote_total = totalVotes
        self.save()

    @property 
    def reviewers(self):
        querySet = self.review_set.all().values_list('owner__id',flat=True) 
        return querySet 

class Review(models.Model):
    VOTE_TYPE = (
        ('up', "Up Vote"),
        ('down', 'Down Vote')
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'project']]
        ordering = ['created']


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.name
