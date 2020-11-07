from django.db import models


class Specie(models.Model):
    description = models.TextField("Description")

    def __str__(self):
        return self.description


class Tree(models.Model):
    description = models.TextField("Description")
    age = models.IntegerField("Age")
    specie = models.ForeignKey(
        Specie,
        on_delete=models.deletion.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.description} - {self.specie}"


class TreeGroup(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    trees = models.ManyToManyField(Tree)

    def __str__(self):
        return self.name


class Harvest(models.Model):
    info = models.TextField("Informations")
    harvest_date = models.DateField()
    gross_weight = models.DecimalField("Gross weight", max_digits=8, decimal_places=2)
    tree = models.OneToOneField(
        Tree,
        on_delete=models.deletion.DO_NOTHING
    )

    def __str__(self):
        return f"Data {self.harvest_date} - {self.info}"