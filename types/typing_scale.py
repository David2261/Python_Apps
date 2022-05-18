from typing import List


Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# Проверка типа; список чисел с плавающей точкой квалифицируется как вектор.


def main():
    print(f'{2.0, [1.0, -4.2, 5.4]} - old')
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    print(f'{new_vector} - new')



if __name__ == '__main__':
    print("Псевдоним типа определяется путем присвоения типа псевдониму.")
    main()