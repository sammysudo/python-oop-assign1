class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")

class AndroidSmartphone(Smartphone):
    def __init__(self, brand, model, price, android_version):
        super().__init__(brand, model, price)
        self.android_version = android_version

    def display_info(self):
        print(f"Android Smartphone: {self.brand} {self.model}, Price: ${self.price}, Android Version: {self.android_version}")

# Example usage
smartphone = Smartphone("Generic", "ModelX", 300)
android_phone = AndroidSmartphone("Samsung", "Galaxy S21", 800, "Android 12")

smartphone.display_info()
android_phone.display_info()
