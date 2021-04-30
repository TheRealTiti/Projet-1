from django.db import models

# Create your models here.



# USERS = {
#     'A': {'Name': 'OM', 'FirstName': 'Matthieu', 'mail': 'matthieuom@mail.com'},
#     'B': {'Name': 'SICAUD', 'FirstName': 'Charles', 'mail': 'charlessicaud@mail.com'},
#     'C': {'Name': 'PRONER', 'FirstName': 'Baptiste', 'mail': 'baptisteproner@mail.com'},
# }

# CONTRACTS = {
#     {'Number': '001', 'Name': 'First contract', 'Description': 'First contract signed', 'Owner': [USERS['A']]},
#     {'Number': '002', 'Name': 'Second contract', 'Description': 'Second contract signed', 'Owner': [USERS['B']]},
#     {'Number': '003', 'Name': 'Third contract', 'Description': 'Third contract signed', 'Owner': [USERS['C']]},
#     {'Number': '004', 'Name': 'Fourth contract', 'Description': 'Fourth contract signed', 'Owner': [USERS['A']]},
#     {'Number': '005', 'Name': 'Fifth contract', 'Description': 'Fifth contract signed', 'Owner': [USERS['B']]},
# }

USERS = {
  '1': {'name': 'Proner', 'firstname': 'Baptiste', 'email': 'baptisteproner@mail.com'},
  '2': {'name': 'Sicaud', 'firstname': 'Charles', 'email': 'charlessicaud@mail.com'},
  '3': {'name': 'OM', 'firstname': 'Matthieu', 'email': 'matthieuom@mail.com'},
  '4': {'name': 'Foujols', 'firstname': 'Claire', 'email': 'clairefoujols@mail.com'},
}


CONTRACTS = [
  {'code': '001','name': 'First contract', 'description': 'The first contract', 'owner': [USERS['1']]},
  {'code': '002','name': 'Second contract', 'description': 'The second contract', 'owner': [USERS['2']]},
  {'code': '003','name': 'Third contract', 'description': 'The third contract', 'owner': [USERS['3']]}
]