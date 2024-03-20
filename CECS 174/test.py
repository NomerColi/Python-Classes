# Q14
count = 0

for i in range(0):
    s = input()
    if s.find('a') != -1:
        count += 1

print(count)

# Q15
class LB_phone_number:
    area_code = "562"

    def __init__(self):
        self.ph_num = "000-0000"

    def update_number(self, num_str):
        self.ph_num = num_str

    def print_phone_num(self):
        print(self.area_code + '-' + self.ph_num)

num = LB_phone_number()
num.update_number("985-1234")
num.print_phone_num()

# Q16
list_of_strings = ['earthworm', 'wallaby', 'buffalo', 'whale']

for a_string in list_of_strings:
    print("element by element: ", end='')
    print(a_string)

# Q17
def calculate_box_volume(length, width, height):
    return length * width * height

print(calculate_box_volume(2.5, 4.0, 2.0))
print(calculate_box_volume(12.5, 10.7, 13.7))

# Q18
def traffic_direction():
    while True:
        s = input()

        if s == "stop" or s == "STOP":
            print("Stop!")
            break

        print("Respect the traffic sign " + s)

traffic_direction()