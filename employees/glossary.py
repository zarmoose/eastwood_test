from django.core.paginator import InvalidPage


class AlphabetGlossary(object):
    """Алфавитный глоссарий"""
    def __init__(self, object_list, on=None, num_groups=7):
        self.object_list = object_list  # список объектов
        self.count = len(object_list)   # количество объектов в списке
        self.max_froups = num_groups    # количество алфавитных групп
        self.groups = []                # список алфавитных групп

        # Словарь, в котором ключ - буква алфавита, а значение - список объектов на эту букву из object_list
        chunks = {}

        for obj in self.object_list:
            if on:
                obj_str = str(getattr(obj, on))
            else:
                obj_str = str(obj)

            letter = str.upper(obj_str[0])

            if letter not in chunks:
                chunks[letter] = []

            chunks[letter].append(obj)

        # Вычисляем предполагаемое количество объектов в алфавитной группе
        per_group = self.count / num_groups
        for letter in chunks:
            chunk_len = len(chunks[letter])
            if chunk_len > per_group:
                per_group = chunk_len

        # Распределяем объекты по алфавитным группам
        current_group = AlphabetGroup(self)

        for letter in chunks:
            sub_list = chunks[letter]  # элементы списка объектов на указанную букву

            # Определяем, уместится ли sub_list в текущую алфавитную группу, или его
            # нужно переносить в новую. Новая группа будет создана, если:
            # - добавление sub_list приведёт к переполнению текущей группы
            # - в текущей группе свободного места меньше, чем количество неумещающихся объектов
            # - текущая группа не пуста (в противном случае, это будет означать, что len(sub_list) > per_group
            new_group_count = len(sub_list) + current_group.count
            if new_group_count > per_group and \
                    abs(per_group - current_group.count) < abs(per_group - new_group_count) and \
                    current_group.count > 0:
                self.groups.append(current_group)
                current_group = AlphabetGroup(self)

            current_group.add(sub_list, letter)

        # Если по окончании цикла осталась непустая группа, добавляем её в глоссарий
        if current_group.count > 0:
            self.groups.append(current_group)

    def group(self, num):
        """Возвращает список объектов указанной группы"""
        if len(self.groups) == 0:
            return None
        elif num > 0 and num <= len(self.groups):
            return self.groups[num - 1]
        else:
            raise InvalidPage

    @property
    def num_groups(self):
        """Возвращает количество алфавитных групп"""
        return len(self.groups)


class AlphabetGroup(object):
    """Алфавитная группа глоссария"""
    def __init__(self, glossary):
        self.glossary = glossary
        self.object_list = []
        self.letters = []

    @property
    def count(self):
        """Возвращает количество объектов в группе"""
        return len(self.object_list)

    @property
    def start_letter(self):
        """Возвращает первую букву группы"""
        if len(self.letters) > 0:
            self.letters.sort(key=str.upper)
            return self.letters[0]
        else:
            return None

    @property
    def end_letter(self):
        """Возвращает последнюю букву группы"""
        if len(self.letters) > 0:
            self.letters.sort(key=str.upper)
            return self.letters[-1]
        else:
            return None

    @property
    def number(self):
        """Возвращает номер группы в глоссарии"""
        return self.glossary.groups.index(self) + 1

    def add(self, new_list, letter=None):
        """Добавляет список объектов в группу"""
        if len(new_list) > 0:
            self.object_list = self.object_list + new_list
        if letter:
            self.letters.append(letter)

    def __repr__(self):
        """Возвращает метку группы"""
        if self.start_letter == self.end_letter:
            return self.start_letter
        else:
            return '%c-%c' % (self.start_letter, self.end_letter)
