from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, Recipe, Building

import json

import os

# Create your views here.
def index(request):
    return  HttpResponse("")

def add_items__internal(request):
    with open("data/db_population/factorio_entities.json") as file_with_json:
        DB_in_json_from_file = json.load(file_with_json)
    print(DB_in_json_from_file)
    for item in DB_in_json_from_file["items"]:

        if "resource" in item.keys():
            resource = item["resource"]
        else:
            resource = False
        
            #TODO: Remake with Item.objects.get_or_create
            
            new_item, created = Item.objects.get_or_create(
                name = item["name"],
                type = item["type"],
                max_stack_size = item["max_stack_size"],
                resource = resource
            )
            
            if not created:
                #TODO: Make a log instead
                print(f"Item with name {item["name"]} already exists in {Item.__name__} model")
            else:
                new_item.save()
                #TODO: Make a log instead
                print(f"Item {model_to_dict(new_item)} was created in {Item.__name__} model")

    return HttpResponse("")
