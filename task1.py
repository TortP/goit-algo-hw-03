import os
import shutil
import sys
import codecs
import locale

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')

def copy_and_sort_files(src_dir, dest_dir):
    try:
        # Перевіряємо, чи існує директорія призначення, якщо ні - створюємо її
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Проходимося по всім елементам директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            try:
                # Якщо елемент - директорія, викликаємо функцію рекурсивно
                if os.path.isdir(item_path):
                    new_dest_dir = os.path.join(dest_dir, item)
                    copy_and_sort_files(item_path, new_dest_dir)
                # Якщо елемент - файл, копіюємо його у відповідну піддиректорію
                elif os.path.isfile(item_path):
                    file_extension = os.path.splitext(item)[1][1:]  # отримуємо розширення файлу без крапки
                    extension_dir = os.path.join(dest_dir, file_extension if file_extension else "no_extension")

                    # Створюємо піддиректорію для відповідного розширення, якщо вона ще не існує
                    if not os.path.exists(extension_dir):
                        os.makedirs(extension_dir)

                    # Копіюємо файл у відповідну піддиректорію
                    shutil.copy2(item_path, extension_dir)
            except PermissionError as e:
                print(f"Помилка доступу до файлу/директорії {item_path}: {e}")
            except FileNotFoundError as e:
                print(f"Файл або директорія не знайдені: {item_path}: {e}")
            except shutil.Error as e:
                print(f"Помилка копіювання файлу {item_path}: {e}")
            except Exception as e:
                print(f"Невідома помилка при обробці файлу/директорії {item_path}: {e}")
    except PermissionError as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")
    except FileNotFoundError as e:
        print(f"Директорія не знайдена: {src_dir}: {e}")
    except Exception as e:
        print(f"Невідома помилка при обробці директорії {src_dir}: {e}")


def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_вихідної_директорії> [шлях_до_директорії_призначення]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        sys.exit(1)

    # Виконуємо рекурсивне копіювання та сортування файлів
    copy_and_sort_files(src_dir, dest_dir)
    print("Файли успішно скопійовані та відсортовані.")


if __name__ == "__main__":
    main()