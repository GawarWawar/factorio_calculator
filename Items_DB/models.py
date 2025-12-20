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
        
 
class Research (models.Model):
    ...
    # name = 
    # packs = 
    
class Technologies (models.Model):
    ...
    # name = 
    

class Packs_In_Research (models.Model):
    ...
    # research =
    # pack = 
    # item_quantity =
    # pack_consume_time = 