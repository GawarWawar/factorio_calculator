from django.db import models

# Create your models here.
class Item (models.Model):
    ITEM_TYPES = {
        "s" : "solid",
        "l" : "liquid",
    }
    
    name = models.CharField(verbose_name="Item Name", max_length=100, unique=True)
    type = models.CharField(verbose_name="Item Type", max_length=3, choices=ITEM_TYPES) #solid/liquid
    max_stack_size = models.IntegerField(verbose_name="Item Stack Size")
    raw = models.BooleanField(verbose_name="Is Item Raw") #True/False
     
class Recipe (models.Model):
    name = models.CharField(verbose_name="Recipe Name", max_length=100, unique=True)
    items = models.ManyToManyField(Item, through="Items_In_Recipe")
    time_to_complete = models.FloatField(verbose_name="Recipe Time to complete")
    output_quantity = models.FloatField(verbose_name="Recipe Output Quantity")
    # description =     
    
class Items_In_Recipe (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.FloatField(verbose_name="Quantity of Items Needed for Recipe")
    
class Building (models.Model):
    ... 
    # name =
    # item = 
    recipes = models.ManyToManyField(Recipe)
    # speed =
    # energy_source = #electricity/burner
    # power_consumption = #in watts
    # drain = #can be NONE
    # pollution = 
    # n_of_module_slots = #0/1/2/3/4
    # productivity = #upps with productivity module, base = 1

    
class Module(models.Model):
    ...
    # item =
    # speed_modifier = 
    # productivity_modifier =
    # power_consumption_modifier =
    
class Fuel(models.Model):
    ...
    # item = 
    # energy_stored =
    
class Conveyor_belt (models.Model):
    ...
    # item =
    # moving_speed =
    
class Manipulator (models.Model):
    ...
    # item =
    # rotation_speed =
    # hand_size = 
    # power_source = #electricity/burner
    # power_consumption = #in watts
    # drain = #can be NONE
    # pollution = 
    # rotation_speed = 
