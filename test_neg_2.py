# Создать отдельный файл для негативных тестов. Функцию проверки вынести в отдельную
# библиотеку. Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки (e) и проверки (t)
# поврежденного архива.

from seminar2_1 import checkout_negative

folderin = " /home/user/tst"
folderout = " /home/user/out"
folderext = " /home/user/folder1"
folderbad = " /home/user/folder2"

def test_neg1():
    # test1
    assert checkout_negative(f"cd {folderout};  7z e arx2.7z -o{folderext} -y", "ERROR"), "test1 FAIL"


def test_neg2():
    # test2
    assert checkout_negative(f"cd {folderbad}; 7z t arx2.7z", "ERROR"), "test2 FAIL"