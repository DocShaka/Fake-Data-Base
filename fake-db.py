import os
from os import *

system("pip install Faker")
system("pip install random")
system("pip install uuid")
system("pip install secret")
system("cls")

import faker
import random
import faker
import randomuser
import random_username
import uuid
import secrets
from faker import Faker 

faker = faker.Faker()  

names = faker.name()
user = faker.currency_code()
mail = faker.company_email()
stringId  = faker.md5()

print(colored(text2art ("\t____________________\n"),'blue'))
print(colored(text2art ("\t_______Fake-DB________"),'white'))
print(colored(text2art ("\t______________________"),'red')) 

print("\nID :   ", names)
print("user : ", user)
print("mail : ", mail)
print("Adresse M.A.C =", secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1))
print("Hash =", stringId)        
print("\n[!]la derniére entrée à été éffacé !")
