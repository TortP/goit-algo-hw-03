def hanoi_tower(n, source, target, auxiliary, state):
    if n > 0:
        # Переміщуємо n-1 дисків з вихідного стрижня на допоміжний
        hanoi_tower(n - 1, source, auxiliary, target, state)
        
        # Переміщуємо один диск з вихідного стрижня на цільовий
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск {disk} з {source} на {target}")
        print(f"Проміжний стан: {state}")
        
        # Переміщуємо n-1 дисків з допоміжного стрижня на цільовий
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main():
    # Запитуємо кількість дисків у користувача
    try:
        n = int(input("Введіть кількість дисків (натисніть Enter для значення за замовчуванням 3): ") or 3)
    except ValueError:
        n = 3

    # Ініціалізуємо стан стрижнів
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")

    # Виконуємо алгоритм Ханойської башти
    hanoi_tower(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()