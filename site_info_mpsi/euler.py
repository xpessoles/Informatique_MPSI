import numpy as np
import matplotlib.pyplot as plt

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list


def euler2(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    h=(b-a)/n
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list


def euler3(F, a, b, y0, n):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    h=(b-a)/n
    t_list=np.linspace(a,b,n+1)
    y = y0
    y_list = [y0] # la liste des valeurs renvoyées
    for t in t_list[1:]:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
    return t_list, y_list


def F(y,t):
    return y