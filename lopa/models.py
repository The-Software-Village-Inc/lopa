from django.db import models
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    target_frequency = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Cause(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    initial_frequency = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Cause_Barrier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    pfd = models.FloatField()
    cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Consequence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    target_frequency = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Consequence_Barrier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    pfd = models.FloatField()
    cause = models.ForeignKey(Consequence,
                              on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
