from fabpy import Values, Formula


list_R_1x = [5425, 2707]
list_R_1N = [3781, 1888]

delta = lambda m, r: 0.1 + 0.2 * (m / r)

# list_dR_1x = [delta(m, r) * r for m, r in zip([4,3], list_R_1x)]
# list_dR_1N = [delta(m, r) * r for m, r in zip([4,4], list_R_1x)]

list_dR_1x = [11.127384884792628, 11.135627262652385]
list_dR_1N = [11.134509124570219, 11.158080508474574]

# print(f"{list_dR_1N=}", f"{list_dR_1x=}")

for _R_1x, _R_1N, _dR_1x, _dR_1N in zip(list_R_1x, list_R_1N, list_dR_1x, list_dR_1N):
    R_1x = Values(name=r"R_{1x}", values=_R_1x, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True)
    print(R_1x.absolute_error._value)
    R_1x.absolute_error._value = _dR_1x
    print(R_1x.absolute_error._value)
    R_1N = Values(name=r"R_{1N}", values=_R_1N, delta=1, unit=r"\text{Ом}", roundoff=1, rounded=True)
    Epsilon_N = Values(name=r"\mathcal{E}_N", values=1.016, delta=0.18, roundoff=3)
    R_1N.absolute_error._value = _dR_1N

    form = Formula(R_1x / R_1N * Epsilon_N, data=[R_1N, R_1x, Epsilon_N], name=r"\mathcal{E}_x", roundoff=3, rounded=True)
    print(R_1x.absolute_error._value)
    print(f"$${form.latex()}$$")
    print(f"$${form.indetect_error.latex()}$$")