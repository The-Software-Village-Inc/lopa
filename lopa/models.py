from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name


class Event(BaseModel):
    description = models.CharField(max_length=1000)
    target_frequency = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.description


class Cause(BaseModel):
    description = models.CharField(max_length=1000)
    initial_frequency = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "cause"

    def __str__(self):
        return self.description


class Cause_Barrier(BaseModel):
    description = models.CharField(max_length=1000)
    pfd = models.FloatField()
    cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "cause_barrier"

    def __str__(self):
        return self.description


class Consequence(BaseModel):
    description = models.CharField(max_length=1000)
    target_frequency = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "consequence"

    def __str__(self):
        return self.description


class Consequence_Barrier(BaseModel):
    description = models.CharField(max_length=1000)
    pfd = models.FloatField()
    consequence = models.ForeignKey(Consequence,
                                    on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "consequence_barrier"

    def __str__(self):
        return self.description
