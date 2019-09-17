from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Ability(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    hp_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mp_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    attack_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    magic_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    defense_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    spirit_porc = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.item.name


class Equipment(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    ability = models.ManyToManyField(Ability, related_name='+')
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    hp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    attack = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    magic = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    defense = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    spirit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.item.name


class Unit(models.Model):
    ability = models.ManyToManyField(Ability, related_name='+')

    name = models.CharField(max_length=120)
    rarity = models.IntegerField(default=0)
    role = models.CharField(max_length=40)
    gender = models.CharField(max_length=5)
    race = models.CharField(max_length=50)

    hp = models.DecimalField(max_digits=10, decimal_places=2)
    mp = models.DecimalField(max_digits=10, decimal_places=2)
    attack = models.DecimalField(max_digits=10, decimal_places=2)
    magic = models.DecimalField(max_digits=10, decimal_places=2)
    defense = models.DecimalField(max_digits=10, decimal_places=2)
    spirit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
