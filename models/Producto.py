from peewee import *
import datetime

DB_TYPE = 'postgres'

if DB_TYPE == 'mysql':
    db = MySQLDatabase(
        'flask_4',
        host='localhost',
        user='root',
        password='',
        port=3306
    )
elif DB_TYPE == 'postgres':
    db = PostgresqlDatabase(
        'flask_4',
        host='localhost',
        user='postgres',
        password='',
        port=5432
    )

class Producto(Model):
    id=AutoField()
    nombre=CharField(max_length=255)
    costo=DecimalField(max_digits=10, decimal_places=2)
    precio=DecimalField(max_digits=10, decimal_places=2)
    stock=IntegerField()
    creado_en=DateTimeField(default=datetime.datetime.now)
    actualizado_en = DateTimeField(default=datetime.datetime.now)
    eliminado = BooleanField(default=False)
    
    class Meta:
        database = db

    def save(self, *args, **kwargs):
            self.actualizado_en = datetime.datetime.now()
            return super().save(*args, **kwargs)