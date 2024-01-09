from django.db import models, connection
from datetime import datetime

def getmonthday():
    current = datetime.now()
    return f"{current.strftime('%B')}, {current.day} | {current.hour}:{current.minute} "

# Create your models here.
class todolist(models.Model):
    todo = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)
    created = models.CharField(max_length=50, default = getmonthday)

    def __str__(self) -> str:
        return f'{self.todo} ==== {self.priority}'


def truncate_cars():
    with connection.cursor() as cursor:
        table_name = todolist._meta.db_table
        cursor.execute(f'DELETE FROM {table_name};')
        cursor.execute(f'VACUUM;')
