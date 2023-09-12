# Добавить в проект тесты, проверяющие работу команд d (удаление из архива) и u (обновление архива).
# Вынести в отдельные переменные пути к папкам с файлами, с архивом
# и с распакованными файлами. Выполнить тесты с ключом -v.

# Доработать позитивные тесты таким образом, чтобы при
# архивации дополнительно проверялось создание файла
# архива, а при распаковке проверялось создание файлов.

"""
Задание 1.
Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
и разархивирования с путями (x).
*Задание 2. *
- Установить пакет для расчёта crc32 > sudo apt install libarchive-zip-perl
- Доработать проект, добавив тест команды расчёта хеша (h).
Проверить, что хеш совпадает с рассчитанным командой crc32.
"""

from seminar2_1 import checkout
import  subprocess

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"

def test_step1():
    # test1
    assert checkout(f"cd {folderin};  7z a {folderout}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    # test6
    res1 = checkout(f"cd {folderin};  7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"

def test_step7():
    # test7
    res1 = checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = checkout(f"ls {folderext}", "test1.txt")
    res3 = checkout(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"

def test_step8():
    """проверка команды h (расчета хеша)"""
    res1 = checkout(f"cd {folderin}; 7z h test1.txt", "Everything is Ok")
    hash_value = subprocess.run(f"cd {folderin}; crc32 test1.txt", shell=True, stdout=subprocess.PIPE, encoding="utf-8").stdout.strip().upper()
    res2 = checkout(f"cd {folderin}; 7z h test1.txt", hash_value)
    assert res1 and res2, "test 8 FAIL"