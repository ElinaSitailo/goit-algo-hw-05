class HashTable:
    """Реалізація хеш-таблиці з використанням списків для розв'язання колізій."""

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """Хеш-функція, яка використовує вбудовану функцію hash()."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка ключа та значення в хеш-таблицю."""
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        """Отримання значення за ключем з хеш-таблиці."""
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        """Видалення ключа та його значення з хеш-таблиці."""
        key_hash = self.hash_function(key)

        if self.table[key_hash] is None:
            return False
        for i in range(len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

    def display(self):
        """Відображення вмісту хеш-таблиці."""
        for i in range(len(self.table)):
            print(f"Індекс {i}: {self.table[i]}")


# Тестуємо нашу хеш-таблицю:
h = HashTable(5)
h.insert("apple", 10)
h.insert("orange", 20)
h.insert("banana", 30)
h.insert("papaya", 40)
print("Початковий стан хеш-таблиці:")
h.display()

h.remove("orange")
print("Після видалення 'orange':")
h.display()

h.remove("banana")
print("Після видалення 'banana':")
h.display()


h.insert("apple", 30)
print("Після оновлення 'apple' з 10 на 30:")
h.display()

print("Отримане значення для 'papaya':", h.get("papaya"))
