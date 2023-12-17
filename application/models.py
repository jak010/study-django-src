from django.db import models


class Person(models.Model):
    class Meta:
        db_table = "person"

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class GroupManager(models.Manager):

    def create(self, name: str, members: Person):
        obj = self.model(name=name)
        obj.save(force_insert=True, using=self.db)
        return obj


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    objects = GroupManager()

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
