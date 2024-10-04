import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

def main():
    # Запит рівня рекурсії у користувача з значенням за замовчуванням
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (за замовчуванням 1): ") or 1)
    except ValueError:
        level = 1

    # Повідомлення про початок малювання
    print(f"Починаємо малювання сніжинки Коха з рівнем рекурсії: {level}")

    # Налаштування вікна та "черепашки"
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed('fastest')

    # Початкове положення черепашки
    t.penup()
    t.goto(-150, 150)
    t.pendown()

    # Малювання сніжинки Коха (трикутник із трьох сторін)
    for _ in range(3):
        koch_snowflake(t, 300, level)
        t.right(120)

    # Завершення
    window.exitonclick()

if __name__ == "__main__":
    main()