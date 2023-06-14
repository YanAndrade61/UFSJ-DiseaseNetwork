import numpy as np
from params import Params

def ode_system(_yk: list, params: Params):

    S = _yk[0]; I = _yk[1]; R = _yk[2]
    I_norm = _yk[3]

    alpha = params.tx_infeccao
    beta = params.tx_recuperacao
    gama = params.tx_mortalidade
    theta = params.tx_nascimento

    dS_dt =  theta*(S+R+I) - alpha*S*I_norm
    dI_dt =  alpha*S*I_norm - beta*I - gama*I
    dR_dt =  beta*I
 
    return np.array([dS_dt,dI_dt,dR_dt,I_norm])  

def rk4(func, _yk,params: dict, _dt=0.01):

    # evaluate derivative at several stages within time interval
    f1 = func(_yk, params)
    f2 = func(_yk + (f1 * (_dt / 2)), params)
    f3 = func(_yk + (f2 * (_dt / 2)), params)
    f4 = func(_yk + (f3 * _dt), params)

    # return an average of the derivative over tk, tk + dt
    return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)