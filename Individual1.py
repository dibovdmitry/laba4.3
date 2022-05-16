#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Liquid (жидкость), имеющий поля названия и плотности. Определить методы
переназначения и изменения плотности. Создать производный класс Аlcohol (спирт),
имеющий крепость. Определить методы переназначения и изменения крепости.
"""


class Liquid:

    def __init__(self, density: float = 0, name: str = 'liquid'):
        self._density, self._name = density, name  # начальные значения

    density, name = property(), property()

    @density.setter
    def density(self, value: float):
        self._density = value

    @name.setter
    def name(self, value: str):
        self._name = value


class Alcohol(Liquid):

    def __init__(self, density: float = 0, name: str = 'alcohol', percent: float = 0):
        super().__init__(density, name)
        self._percent = percent

    name, percent = property(), property()

    @name.setter
    def name(self, value: str):
        self._name = value

    @percent.setter
    def percent(self, value: float):
        self._percent = value


if __name__ == '__main__':
