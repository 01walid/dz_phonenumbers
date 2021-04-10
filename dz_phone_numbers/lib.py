class DzPhoneNumber:

    carriers = { 
        'ooredoo': '05',
        'mobilis': '06',
        'djezzy': '07'
    }

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.is_valid()

    def is_valid(self) -> bool: 
        if len(self.phone_number) != 10 or not self.phone_number.isdigit():
            raise ValueError("Invalid phone number")
        

    def get_phone_carrier(self): 
        for name, initial in self.carriers.items():
            if self.phone_number[:2] == initial:
                return name

        ValueError("Invalid phone carrier")

    def is_ooredoo(self): 
        return self.get_phone_carrier() == 'ooredoo'

    def is_mobilis(self): 
        return self.get_phone_carrier() == 'mobilis'

    def is_djezzy(self): 
        return self.get_phone_carrier() == 'djezzy'
    