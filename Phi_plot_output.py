import matplotlib.pyplot as plt
import numpy as np
import timeit

np.set_printoptions(precision=6, suppress=True)

# inputs 
lim = 10
x = np.linspace(-lim,lim,1000000)
mu = 1/3
q1vec = [0, 0.25, 0.5, 0.75, 1]
q2vec = [0, 0.25, 0.5, 0.75, 1]

# initializing arrays
L1mat = np.zeros((5, 5))
L2mat = np.zeros((5, 5))
L3mat = np.zeros((5, 5))

CL1mat = np.zeros((5, 5))
CL2mat = np.zeros((5, 5))
CL3mat = np.zeros((5, 5))

for q1 in q1vec:
    for q2 in q2vec:
        Cmin = 2
        Cmax = 4
        Cin = np.linspace(Cmin,Cmax,11)

        nu = 1-mu 

        # print('q1 = ',q1)
        # print('q2 = ',q2)
        # print('')

        phi1 = np.zeros(len(x))
        phi2 = np.zeros(len(x))
        phi3 = np.zeros(len(x))
        with np.errstate(divide='ignore', invalid='ignore'):
            phi1 = x + q1*nu/(x+mu)**2 + q2*mu/(x-nu)**2
            phi2 = x - q1*nu/(x+mu)**2 + q2*mu/(x-nu)**2
            phi3 = x - q1*nu/(x+mu)**2 - q2*mu/(x-nu)**2

        phi1cut = np.searchsorted(x, -mu)
        phi2cut = np.searchsorted(x, nu)        

        L1 = np.nan
        L2 = np.nan
        L3 = np.nan

        # L3
        indices = np.where(x < -mu)[0]
        crossings = indices[:-1][
            (phi1[indices[:-1]] <= 0) &
            (phi1[indices[1:]] > 0)
        ]
        if len(crossings) > 0:
            L3 = x[crossings[0] + 1]

        # L1
        indices = np.where((x > -mu) & (x < nu))[0]
        crossings = indices[:-1][
            (phi2[indices[:-1]] <= 0) &
            (phi2[indices[1:]] > 0)
        ]
        if len(crossings) > 0:
            L1 = x[crossings[0] + 1]

        # L2
        indices = np.where(x > nu)[0]
        crossings = indices[:-1][
            (phi3[indices[:-1]] <= 0) &
            (phi3[indices[1:]] > 0)
        ]
        if len(crossings) > 0:
            L2 = x[crossings[0] + 1]

        # Calculation of the Lagrange point energies
        def jacobi(L):
            if np.isnan(L):
                return np.nan

            term1 = q1*nu/abs(L+mu) if q1 != 0 else 0
            term2 = q2*mu/abs(L-nu) if q2 != 0 else 0

            return L**2 + 2*(term1 + term2)

        CL1 = jacobi(L1)
        CL2 = jacobi(L2)
        CL3 = jacobi(L3)

        # print()
        # print('CL1 = ',round(CL1,10))
        # print('CL2 = ',round(CL2,10))
        # print('CL3 = ',round(CL3,10))
        # print()

        L1mat[int(q2*4)][int(q1*4)] = float(L1)
        L2mat[int(q2*4)][int(q1*4)] = float(L2)
        L3mat[int(q2*4)][int(q1*4)] = float(L3)

        CL1mat[int(q2*4)][int(q1*4)] = float(CL1)
        CL2mat[int(q2*4)][int(q1*4)] = float(CL2)
        CL3mat[int(q2*4)][int(q1*4)] = float(CL3)


arrays = {
    "L1": L1mat,
    "L2": L2mat,
    "L3": L3mat,
    "CL1": CL1mat,
    "CL2": CL2mat,
    "CL3": CL3mat
}

for name, matrix in arrays.items():
    print(f"\n{name} = np.array([")

    for row in matrix:
        values = ", ".join(
            "np.nan" if np.isnan(value) else f"{value:.16g}"
            for value in row
        )
        print(f"    [{values}],")

    print("])")
