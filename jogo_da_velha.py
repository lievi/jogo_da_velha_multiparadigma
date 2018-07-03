#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""
Um jogo da velha simples

Licensa:

Copyright 2018 Lievi Silva
"""

from curses import initscr, wrapper
from random import randint


def boas_vindas(stdscr):
    stdscr.addstr(1, 1, "Bem vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Pressione q para sair ou h para obter ajuda.")
    stdscr.addstr(15, 1, "Desenvolvido por: Lievi Silva.")
    stdscr.addstr(17, 1, "Licensa Nova BSD.")


def ajuda(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, "Pressione q para sair ou h para exibir essa ajuda.")
    stdscr.addstr(2, 1, "Para mudar a posição, use as teclas: W, A, S, D")
    stdscr.addstr(3, 1, "Para definir uma posição do jogo, digite: L")
    stdscr.addstr(4, 1, "Para reiniciar a partida, digite: Y")
    stdscr.addstr(5, 1, "Pressione espaço para sair dessa tela.")
    stdscr.refresh()


def reiniciar_tela(stdscr):
    stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()


def main(stdscr):
    stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()

    while True:
        entrada = stdscr.getkey()
        if entrada == 'q':
            break
        if entrada == 'h':
            ajuda(stdscr)
        else:
            boas_vindas(stdscr)


if __name__ == "__main__":
    initscr()
    wrapper(main)
