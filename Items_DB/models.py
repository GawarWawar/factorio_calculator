from django.db import models

# Create your models here.
class Item (models.Model):
    name = models.CharField(verbose_name="Item Name", max_length=100, primary_key=True)
    # type = #solid/liquid
    # max_stack_size = 
    # raw = #True/False
    # researches = 
     
class Receipe (models.Model):
    ...
    # name = models.CharField(verbose_name="Receipe Name", max_length=100, primary_key=True)
    items = models.ManyToManyField(Item, through="Items_In_Recipe")
    # time_to_produce = 
    # output_quantity = 
    # description =     
    
class Items_In_Recipe (models.Model):
    ...
    # receipe =
    # item_name = 
    # item_quantity =
    
class Building (models.Model):
    ... 
    # name =
    # item = 
    recipes = models.ManyToManyField(Receipe)
    # speed =
    # power_source = #electricity/burner
    # power_consumption = #in watts
    # drain = #can be NONE
    # n_of_module_slots = #0/1/2/3/4
    # productivity = #upps with productivity module, base = 1
