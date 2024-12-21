import sympy as sp

# Definir las constantes simbólicas
E, V0, a, m, hbar, eps = sp.symbols('E V0 a m hbar eps')

# Definir las expresiones para T y R en función de E y V0
T = (1 + (V0**2 / (4*E*(E - V0))) * sp.sin(a*sp.sqrt(2*m*V0 / hbar**2) * sp.sqrt(E/V0 - 1))**2)**-1
R = (1 + (4*(E/V0)*((E/V0) - 1)) / sp.sin(a*sp.sqrt(2*m*V0 / hbar**2) * sp.sqrt(E/V0 - 1))**2)**-1


# Sustituir E por eps*V0 en T y R
T_eps = T.subs(E, eps*V0)
R_eps = R.subs(E, eps*V0)

sp.pprint(T_eps)
sp.pprint(R_eps)

# Tomar el límite cuando eps -> 1
T_lim = sp.limit(T_eps, eps, 1)
R_lim = sp.limit(R_eps, eps, 1)

# Mostrar los resultados
sp.pprint(T_lim, use_unicode=True)
sp.pprint(R_lim, use_unicode=True)
