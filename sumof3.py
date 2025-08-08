print("my name is khalid sarfraz")
def main():
    num_1 = int(input("enter first numebr: "))
    num_2 = int(input("enter second number: "))
    num_3 = int(input("enter third number: "))

    if num_1 == num_2 and num_1 == num_3:
        print(f,"all number are equal{num_1}")

    if num_1 > num_2 and num_1 > num_3:
        print(f"num_1 is the largest: {num_1}")
