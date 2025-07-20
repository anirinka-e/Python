from mailing import Mailing
from address import Address

to_address = Address("123456", "Ромашково", "пр. Лесной", "11", "7")
from_address = Address("456789", "Ромашково", "ул. Речная ", "17", "5")

mailing = Mailing(to_address, from_address, 200, 123)

print(mailing)
