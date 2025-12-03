# Порівняйте ефективність алгоритмів пошуку підрядка:
# Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа
# на основі двох текстових файлів (text1, text2).
# Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків:
# одного, що дійсно існує в тексті,
# та іншого — вигаданого (вибір підрядків за вашим бажанням).
# На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.

# Програмно реалізовано алгоритми пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа.
# Виконайте порівняння та виведіть результати у зручному для читання форматі.

import timeit


def compute_lps(pattern):
    """Обчислити масив найдовших префіксів-суфіксів (LPS) для алгоритму Кнута-Морріса-Пратта."""
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    """Виконує пошук підрядка в основному рядку за допомогою алгоритму Кнута-Морріса-Пратта."""
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    # print(f"Shift table: {shift_table}")
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1


def polynomial_hash(s, base=256, modulus=101):
    """Повертає поліноміальний хеш рядка s."""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    """Виконує пошук підрядка в основному рядку за допомогою алгоритму Рабіна-Карпа."""
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def search_pattern_in_text(text, pattern, kmp_search_times, boyer_moore_search_times, rabin_karp_search_times):
    """Вимірює час виконання кожного алгоритму пошуку підрядка в тексті."""
    n = 1000

    kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=n)
    kmp_search_times.append(kmp_time)

    bm_time = timeit.timeit(lambda: boyer_moore_search(text, pattern), number=n)
    boyer_moore_search_times.append(bm_time)

    rk_time = timeit.timeit(lambda: rabin_karp_search(text, pattern), number=n)
    rabin_karp_search_times.append(rk_time)


def test_search_algorithms():
    """Тестує алгоритми пошуку підрядка на двох текстах з різними підрядками."""
    kmp_search_times = []
    boyer_moore_search_times = []
    rabin_karp_search_times = []

    exists_text1_pattern = "Інтерполяційний пошук"
    exists_text2_pattern = "Комбинаторные алгоритмы"
    non_existent_text_pattern = "Порівняйте ефективність алгоритмів пошуку підрядка"

    with open("data/text_1.txt", "r", encoding="utf-8") as file:
        text1 = file.read()

        print("testing text_1, len =", len(text1))
        search_pattern_in_text(text1, exists_text1_pattern, kmp_search_times, boyer_moore_search_times, rabin_karp_search_times)
        search_pattern_in_text(text1, non_existent_text_pattern, kmp_search_times, boyer_moore_search_times, rabin_karp_search_times)

    with open("data/text_2.txt", "r", encoding="utf-8") as file:
        text2 = file.read()

        print("testing text_2, len =", len(text2))
        search_pattern_in_text(text2, exists_text2_pattern, kmp_search_times, boyer_moore_search_times, rabin_karp_search_times)
        search_pattern_in_text(text2, non_existent_text_pattern, kmp_search_times, boyer_moore_search_times, rabin_karp_search_times)

    return kmp_search_times, boyer_moore_search_times, rabin_karp_search_times


# Приклад використання:
if __name__ == "__main__":
    kmp_times, boyer_moore_times, rabin_karp_times = test_search_algorithms()

    print("Time of search algorithms (in seconds) for both texts:")

    print(f"{'Algorithm':<20}{'exists in text_1':<25}{'exists in text_2':<25}{'non_existent in text_1':<25}{'non_existent in text_2':<25}")

    print(f"{'KMP':<20}{kmp_times[0]:<25.3f}{kmp_times[2]:<25.3f}{kmp_times[1]:<25.3f}{kmp_times[3]:<25.3f}")
    print(f"{'Boyer-Moore':<20}{boyer_moore_times[0]:<25.3f}{boyer_moore_times[2]:<25.3f}{boyer_moore_times[1]:<25.3f}{boyer_moore_times[3]:<25.3f}")
    print(f"{'Rabin-Karp':<20}{rabin_karp_times[0]:<25.3f}{rabin_karp_times[2]:<25.3f}{rabin_karp_times[1]:<25.3f}{rabin_karp_times[3]:<25.3f}")
