class Resistor():
    """
        Класс Resistor представляет собой резистор, который определяется по цветовому коду на корпусе.
        Цветовой код состоит от 2 до 5 полос, которые определяют сопротивление резистора и его допустимую погрешность.
    """

    def __init__(self, *colors):
        self.colors = colors
        self.color_map = {
            "черный": 0,
            "коричневый": 1,
            "красный": 2,
            "оранжевый": 3,
            "желтый": 4,
            "зеленый": 5,
            "синий": 6,
            "фиолетовый": 7,
            "серый": 8,
            "белый": 9,
            "золотой": 0,
            "серебро": 0
        }

    def resistance(self):
        """
            Вычисляет сопротивление резистора, используя заданный цветовой код.
        """
        if len(self.colors) == 4:
            multiplier = 10 ** self.color_map[self.colors[3]]
        elif len(self.colors) == 5:
            multiplier = (10 ** self.color_map[self.colors[3]]) + (10 ** self.color_map[self.colors[4]]) * 0.1
        else:
            multiplier = 1

        return round((self.color_map[self.colors[0]] * 10 + self.color_map[self.colors[1]]) * multiplier)

    def tolerance(self):
        """
            Определяет допустимую погрешность резистора, используя заданный цветовой код.
        """

        if len(self.colors) == 4 and self.colors[3] == "серебро":
            return 10
        elif len(self.colors) == 4 and self.colors[3] == "золотой":
            return 5
        elif len(self.colors) == 4 and self.colors[3] == "коричневый":
            return 1
        elif len(self.colors) == 4 and self.colors[3] == "красный":
            return 2
        elif len(self.colors) == 4 and self.colors[3] == "зеленый":
            return 0.5
        elif len(self.colors) == 4 and self.colors[3] == "синий":
            return 0.25
        elif len(self.colors) == 4 and self.colors[3] == "фиолетовый":
            return 0.1
        elif len(self.colors) == 4 and self.colors[3] == "серый":
            return 0.05
        elif len(self.colors) == 4:
            return None

        elif len(self.colors) == 5 and self.colors[4] == "золотой":
            return 5
        elif len(self.colors) == 5 and self.colors[4] == "серебро":
            return 10
        elif len(self.colors) == 5 and self.colors[4] == "коричневый":
            return 1
        elif len(self.colors) == 5 and self.colors[4] == "красный":
            return 2
        elif len(self.colors) == 5 and self.colors[4] == "зеленый":
            return 0.5
        elif len(self.colors) == 5 and self.colors[4] == "синий":
            return 0.25
        elif len(self.colors) == 5 and self.colors[4] == "фиолетовый":
            return 0.1
        elif len(self.colors) == 5 and self.colors[4] == "серый":
            return 0.05
        elif len(self.colors) == 4:
            return None
        else:
            return None


if __name__ == "__main__":
    colors = input("Введите цветовой код резистора через пробел (например: красный желтый зеленый). Можно вести от 2 до 5 цветового кода. \n"
                   "Если на резисторе 4 полосы то на 4 полосе можно водить еще такие цвета (золотой и серебро) для указания точности, тоже самое для 5-и полос. \n").lower().split()


    resistor = Resistor(*colors)
    print("Сопротивление резистора:", resistor.resistance(), "Ом;", (resistor.resistance()/1000), "кОм;",(resistor.resistance()/1000000), "мОм;", (resistor.resistance()/1000000000), "ГОм;")
    print("Допустимая погрешность:", resistor.tolerance(), "%")
