def get_scientific_notation(number):
    number_str = str(number)
    
    if '.' in number_str:
        integer_part, decimal_part = number_str.split('.')
        number_str = integer_part + decimal_part.rstrip('0')

    power = len(number_str) - 1
    exponent = 0

    while power > 0:
        digit_sum = sum(map(int, str(power)))
        power = digit_sum
        exponent += 1

    return f"{number_str[0]}.{number_str[1:]}e{exponent}"

def generate_password(number, name):
    scientific_notation = get_scientific_notation(number)

    s1 = ''.join([word[:3] for word in map(str, scientific_notation.split('e')[0])])
    s2 = ''.join([char for i, char in enumerate(name) if (i + 1) % 2 == int(scientific_notation[-1]) % 2])

    return f"{s1}@{s2}"

def main():
    T = int(input().strip())

    for _ in range(T):
        try:
            number, name = input().strip().split()
            number = float(number)
            if number < 0:
                raise ValueError("Invalid input")
            if not all(char.islower() for char in name):
                raise ValueError("Invalid input")
        except ValueError:
            print("Invalid")
            continue

        password = generate_password(number, name)
        print(password)

if __name__ == "__main__":
    main()
