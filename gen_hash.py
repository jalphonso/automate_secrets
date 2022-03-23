import getpass
from passlib.hash import sha512_crypt
 
clear_password1 = getpass.getpass('New password: ')
clear_password2 = getpass.getpass('Retype new password: ')
if clear_password1 != clear_password2:
    raise ValueError('Passwords are not equal; aborting')
rounds = 5000
salt = '2o35AbB3'
crypt_string = sha512_crypt.hash(clear_password1,
                                    rounds=rounds,
                                    salt=salt)
print("The hashed password is: %s" % (crypt_string))