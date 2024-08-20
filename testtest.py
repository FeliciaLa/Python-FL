class Father():
    def transport(self):
        print("The transport used is a car")


# Subclass
class Son(Father):
    def transport(self):
        print("The transport used is a bicycle")

# This will output "The transport used is a bicycle" # because the inherited method is being overridden
# by the Son subclass
# Subclass
son_1.transport()