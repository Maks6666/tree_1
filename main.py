# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький
# або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник
# звернень);
# ■ відображати топ-10 найнепопулярніших слів
# (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього
# завдання.


class TreeNode:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.left = None
        self.right = None

class Dictionary:
    def __init__(self):
        self.root = None

    def add_word(self, word, translation):
        if not self.root:
            self.root = TreeNode(word, translation)
        else:
            self.add_next_word(self.root, word, translation)

    def add_next_word(self, node, word, translation):
        if word < node.word:
            if node.left is None:
                node.left = TreeNode(word, translation)
            else:
                self.add_next_word(node.left, word, translation)
        elif word > node.word:
            if node.right is None:
                node.right = TreeNode(word, translation)
            else:
                self.add_next_word(node.right, word, translation)
        else:
            node.translation.append(translation)

    def find_word(self, word):
        return self.find_next_word(self.root, word)

    def find_next_word(self, node, word):
        if node is None:
            return None
        if word == node.word:
            return node.translation
        elif word < node.word:
            return self.find_next_word(node.left, word)
        else:
            return self.find_next_word(node.right, word)

dictionary = Dictionary()

dictionary.add_word("apple", "яблуко")
dictionary.add_word("auto", "машина")
dictionary.add_word("table", "стіл")


print("Translation of 'apple':", dictionary.find_word("apple"))
print("Translation of 'auto':", dictionary.find_word("auto"))
print("Translation of 'table':", dictionary.find_word("table"))






