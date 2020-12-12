import base64
import sys
import orchestrator
import setup
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


could_create = setup.create_password_table()

if could_create == -1:
    print('Could not create table')

if len(sys.argv) < 3:
    print('Not enough arguments')
    print('Syntax: python passmanager.py <master_password> -method <website> <username> <password>')
    sys.exit(1)

# we eliminate the file name
sys.argv.pop(0)

# get master password
# master_password_file = sys.argv[0]
# master_password = open(master_password_file, "r").read()
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(sys.argv[0].encode())
master_password = base64.urlsafe_b64encode(digest.finalize())
sys.argv.pop(0)

# get method from args
method = sys.argv[0]
sys.argv.pop(0)

# pass the method and the list of args to orchestrator
result = orchestrator.execute(master_password, method, sys.argv)

if result:
    sys.exit(0)
else:
    sys.exit(2)
