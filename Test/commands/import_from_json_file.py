"""
Import json data from JSON file to Datababse
"""
import os
import json
from Test.models import Registrartion
from django.core.management.base import BaseCommand
from datetime import datetime
from Assessment.settings import BASE_DIR


class Command(BaseCommand):
    def import_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'import_data', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    userid= data_object.get('userid',None)
                    title = data_object.get('title', None)
                    body = data_object.get('body', None)

                    try:
                        data, created = Registrartion.objects.get_or_create(
                            title=title,
                            userid=userid,
                            body=body
                        )
                        if created:
                            data.save()
                            display_format = "\nRegistrartion, {}, has been saved."
                            print(display_format.format(data))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(title, str(ex))
                        print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_from_file()

