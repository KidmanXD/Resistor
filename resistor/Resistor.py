class Resistor():
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
        if len(self.colors) == 4:
            multiplier = 10 ** self.color_map[self.colors[3]]
        elif len(self.colors) == 5:
            multiplier = (10 ** self.color_map[self.colors[3]]) + (10 ** self.color_map[self.colors[4]]) * 0.1
        else:
            multiplier = 1

        return (self.color_map[self.colors[0]] * 10 + self.color_map[self.colors[1]]) * multiplier

    def tolerance(self):
        """
        Если указаны 4 цветовые полоски, то это означает, что резистор без указания точности, и допустимая погрешность будет 20%.
        Если указаны 5 цветовых полосок и последняя полоска имеет цвет "золотой", то допустимая погрешность составляет 5%.
        Если указаны 5 цветовых полосок и последняя полоска имеет цвет "серебро", то допустимая погрешность составляет 10%.
        """
        if len(self.colors) == 4:
            return 20
        elif len(self.colors) == 5 and self.colors[4] == "золотой":
            return 5
        elif len(self.colors) == 5 and self.colors[4] == "серебро":
            return 10
        else:
            return None


if __name__ == "__main__":
    colors = input("Введите цветовой код резистора через пробел (например: красный желтый зеленый)"
                   "\nМожно вести от 2 до 5 цветового кода"
                   "\nЕсли на резисторе 5 полос то на 5 полосе можно водить еще такие цвета (золотой и серебро) для указания погрешности \n").lower().split()


    resistor = Resistor(*colors)
    print("Сопротивление резистора:", resistor.resistance(), "Ом")
    print("Допустимая погрешность:", resistor.tolerance(), "%")
