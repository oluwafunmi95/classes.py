
class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''
    user_type = ''
    is_active = ''

    def get_full_name(self):
        return "{}, {}".format(user.first_name, user.last_name)

class MenuItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''


class Order():
    pass

class Price():
    pass


user = User()
user.first_name = 'Ini'
user.last_name = 'Arthur'
user.phone_number = '8723438887'
user.email_address = 'ini.arthur@meltwater.org'

print('My name is {} and we are Fuudia'.format(user.get_full_name()))


class Father():
    last_name = ''
    company = ''
    wife = ''
class Son(Father):
    first_name = ''