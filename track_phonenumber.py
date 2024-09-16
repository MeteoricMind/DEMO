import phonenumbers
# x = phonenumbers.parse("+918591245278",None)
# print(x)

from phonenumbers import timezone , geocoder , carrier
number = '1 831 657-8479'
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg= geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
z= phonenumbers.is_valid_number(phone)
print(z)
# import phonenumbers

# x = phonenumbers.parse("+442083661177", None)
# print(x)
# y = phonenumbers.parse("020 8366 1177", None)
# print(y)