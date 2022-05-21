#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Создать класс Liquid (жидкость), имеющий поля названия и плотности. Определить методы
переназначения и изменения плотности. Создать производный класс Аlcohol (спирт),
имеющий крепость. Определить методы переназначения и изменения крепости.
"""


class Liquid:
    def __init__(self, title, density):
        self.title = title
        self.__density = density

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    @property
    def density(self):
        return self.__density

    @density.setter
    def density(self, value: float):
        self.__density = value


class Alcohol(Liquid):
    def __init__(self, title, density, strength):
        super().__init__(title, density)
        self.__strength = strength

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value: float):
        self.__strength = value


def main():
    alcohol = Alcohol("Метиловый", 0.812, 80)
    liquid = Liquid("Этиловый", 0.806)
    print(f"Спирт: {alcohol.title}, плотность спирта: {alcohol.density} г/см^3, "
          f"крепость спирта: {alcohol.strength}%")
    print(f"Спирт: {liquid.title}, плотность спирта: {liquid.density} г/см^3")
    alcohol.title = "Пропиловый"
    alcohol.density = 0.816
    alcohol.strength = 60
    print(f"Спирт: {alcohol.title}, плотность спирта: {alcohol.density} г/см^3, "
          f"крепость спирта: {alcohol.strength}%")


if __name__ == "__main__":
    main()
