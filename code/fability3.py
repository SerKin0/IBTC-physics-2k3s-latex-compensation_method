# from fabpy import Values, Formula

# _R_1 = 5425
# _R_2 = 11111 - _R_1
# _I_3 = 0
# _r = 0
# _E = 3

# # R_1x = Values(name=r"R_{1x}", values=_R_1x, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True)
# R_1 = Values(name=r"R_{1}", values=_R_1, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True, use_random_error=False)
# R_2 = Values(name=r"R_{2}", values=_R_2, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True, use_random_error=False)
# I_3 = Values(name=r"I_{3}", values=_I_3, delta=1, unit=r"\text{А}", roundoff=1, rounded=True, use_random_error=False)
# r = Values(name=r"r", values=_r, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True, use_random_error=False)
# E = Values(name=r"\Epsilon", values=_E, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True, use_random_error=False)

# form = (E * R_1 - I_3 * (r * (R_1 + R_2) + R_1 * R_2)) / (R_1 + R_2)
# temp = Formula(form, [R_1, R_2, I_3, r, E], r'\text{В}', r'\Epsilon_x')

# print(temp.indetect_error.latex())

r = 0
R_1 = 5425
R_2 = 11111 - R_1
Delta_I = 0.5*0.001
Delta_R_1 = 5
Delta_R_2 = 5
I_3 = 0
E = 3
Delta_E = 0.115

Delta_E_x = - (r * (R_1 + R_2) + R_1 * R_2) / (R_1 + R_2) * Delta_I + (R_2 * (E - I_3 * R_2)) / (R_1 + R_2)**2 * Delta_R_1 + (R_1 * (R_1 + R_2 - E + I_3 * R_2)) / (R_1 + R_2)**2 * Delta_R_2 + (R_1) / (R_1 + R_2) * Delta_E
print(Delta_E_x)
