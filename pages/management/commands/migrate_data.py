# from django.core.management.base import BaseCommand
# from django.db import connections
# from users.models import Reviews
# from django.contrib.auth.models import User

# class Command(BaseCommand):
#     help = 'Transfer data from SQLite to PostgreSQL'

#     def handle(self, *args, **kwargs):
#         old_cursor = connections['old'].cursor()
#         old_cursor.execute('SELECT * FROM auth_user')

#         for row in old_cursor.fetchall():
#             User.objects.create(
#                 id=row[0],
#                 password=row[1],
#                 last_login=row[2],
#                 is_superuser=row[3],
#                 username=row[4],
#                 last_name=row[5],
#                 email=row[6],
#                 is_staff=row[7],
#                 is_active=row[8],
#                 date_joined=row[9],
#                 first_name=row[10],
                
#                 # map all fields accordingly
#             )

#         self.stdout.write(self.style.SUCCESS('Data transfer complete'))
