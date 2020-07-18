import sys

from cryptography.fernet import Fernet

import os

from airtable import Airtable

if len(sys.argv) == 1:

  print("Oops! Please provide command line arguments.")

f = Fernet(input("Secret key: "))

api_key = input("Airtable API Key: ")

base_key = input("Airtable Base Key: ")

table = Airtable(base_key, 'Admins', api_key)

if sys.argv[1] == "new":

    users_email = input("Admin Username: ")

    users_password = f.encrypt(input("Admin Code: ").encode())

    try:
      table.insert({'Username': users_email,'Password': users_password.decode("utf-8") })
    except:
      print("Oops!  There was an error. Please check you are using valid API crediantals.")

elif sys.argv[1] == "update":

  users_email = input("Admin Username: ")

  users_password = f.encrypt(input("New Admin Code: ").encode())

  try:
    table.update_by_field('Username', users_email, {'Email': users_email,'Password': users_password.decode("utf-8") })

  except:
    print("Oops!  There was an error. Please check you are using valid API crediantals.")

elif sys.argv[1] == "remove":

  users_email = input("Admin Username: ")

  try:
    table.delete_by_field('Username', users_email)
  except:
    print("Oops!  There was an error. Please check you are using valid API crediantals.")

else:

  print("Invalid command line arguments.")
