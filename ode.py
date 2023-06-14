import numpy as np
from params import Params


def ode_system(_yk: list, params: Params):
    """
    Define as equações do sistema de equações diferenciais ordinárias (EDO).

    Args:
    - _yk (list): Lista contendo as variáveis S, I, R e I_norm.
    - params (Params): Objeto contendo os parâmetros do sistema.

    Returns:
    Um array numpy contendo as derivadas das variáveis S, I, R e I_norm.
    """
    S, I, R = _yk[0], _yk[1], _yk[2]
    I_norm = _yk[3]

    alpha = params.tx_infeccao
    beta = params.tx_recuperacao
    gama = params.tx_mortalidade
    theta = params.tx_nascimento

    dS_dt = theta * (S + R + I) - alpha * S * I_norm
    dI_dt = alpha * S * I_norm - beta * I - gama * I
    dR_dt = beta * I

    return np.array([dS_dt, dI_dt, dR_dt, I_norm])


def rk4(func, _yk: list, params: Params, _dt=0.01):
    """
    Implementa o método Runge-Kutta de quarta ordem para resolver equações diferenciais.

    Args:
    - func (function): Função que define o sistema de equações diferenciais.
    - _yk (list): Lista contendo as variáveis do sistema.
    - params (Params): Objeto contendo os parâmetros do sistema.
    - _dt (float): Tamanho do passo de integração (opcional, padrão=0.01).

    Returns:
    Um array numpy contendo os valores atualizados das variáveis do sistema.
    """
    f1 = func(_yk, params)
    f2 = func(_yk + (f1 * (_dt / 2)), params)
    f3 = func(_yk + (f2 * (_dt / 2)), params)
    f4 = func(_yk + (f3 * _dt), params)

    return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)
