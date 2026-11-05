import matplotlib.pyplot as plt
import numpy as np
import timeit

L1mat = np.zeros((21,21))
L2mat = np.zeros((21,21))
L3mat = np.zeros((21,21))
CL1mat = np.zeros((21,21))
CL2mat = np.zeros((21,21))
CL3mat = np.zeros((21,21))

L1mat_ord = np.zeros((21,21))
L2mat_ord = np.zeros((21,21))
L3mat_ord = np.zeros((21,21))
CL1mat_ord = np.zeros((21,21))
CL2mat_ord = np.zeros((21,21))
CL3mat_ord = np.zeros((21,21))

for row in range(21):
    for col in range(21):
        # inputs 
        lim = 10
        x = np.linspace(-lim,lim,6000)
        mu = 0.012155099
        q2 = row/20
        q1 = col/20
        
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
        for i in x: 
            phi1[np.where(x==i)] = i + q1*nu/(i+mu)**2 + q2*mu/(i+mu-1)**2
            phi2[np.where(x==i)] = i - q1*nu/(i+mu)**2 + q2*mu/(i+mu-1)**2
            phi3[np.where(x==i)] = i - q1*nu/(i+mu)**2 - q2*mu/(i+mu-1)**2

        phi2max = max(phi2)
        phi2min = min(phi2)
        phi1cut = np.where(phi2==phi2min)[0][0]
        phi2cut = np.where(phi2==phi2max)[0][0]

        plt.plot(x[0:phi1cut],phi1[0:phi1cut])
        plt.plot(x[phi1cut:phi2cut],phi2[phi1cut:phi2cut])
        plt.plot(x[phi2cut:len(phi3)],phi3[phi2cut:len(phi3)])
        plt.plot(x,x,'k')
        plt.plot(x,np.zeros(len(x)),'gray')
        plt.axvline(x=0,c='gray')

        plt.xlim(-4,4)
        plt.ylim(-4,4)

        plt.legend(['x<-µ', '-µ<x<1-µ', 'x>1-µ', 'φ=x'])

        plt.xlabel('x')
        plt.ylabel('φ')

        L1 = 0
        L2 = 0
        L3 = 0
        for j in x:
            if j < x[phi1cut]:
                if phi1[np.where(x==j)] > 0:
                    L3 = j
                    break
            
        for k in x:
            if x[phi1cut] < k < x[phi2cut]:
                if phi2[np.where(x==k)] > 0:
                    L1 = k
                    break

        for l in x:
            if l > x[phi2cut]:
                if phi3[np.where(x==l)] > 0:
                    L2 = l
                    break

        # print('L1 = ',round(L1,10))
        # print('L2 = ',round(L2,10))
        # print('L3 = ',round(L3,10))

        plt.text(L1,-0.3,'L1')
        plt.text(L2,-0.3,'L2')
        plt.text(L3,-0.3,'L3')
        plt.text(-mu,0.2,'-µ')
        plt.text(nu,0.2,'ν')

        plt.scatter(L1,0,c='k')
        plt.scatter(L2,0,c='k')
        plt.scatter(L3,0,c='k')
        plt.scatter(-mu,0,c='k')
        plt.scatter(nu,0,c='k')

        tit = 'q1=' + str(q1) + ', q2=' + str(q2)
        plt.title(tit)

        # plt.show()

        # Calculation of the Lagrange point energies
        CL1 = (L1**2) + 2*(q1*nu/np.sqrt((L1+mu)**2) + q2*mu/np.sqrt((L1-nu)**2))
        CL2 = (L2**2) + 2*(q1*nu/np.sqrt((L2+mu)**2) + q2*mu/np.sqrt((L2-nu)**2))
        CL3 = (L3**2) + 2*(q1*nu/np.sqrt((L3+mu)**2) + q2*mu/np.sqrt((L3-nu)**2))

        # print()
        # print('CL1 = ',round(CL1,10))
        # print('CL2 = ',round(CL2,10))
        # print('CL3 = ',round(CL3,10))
        # print()

        L1mat[row,col] = L1
        L2mat[row,col] = L2
        L3mat[row,col] = L3
        CL1mat[row,col] = CL1
        CL2mat[row,col] = CL2
        CL3mat[row,col] = CL3    

        pairs = [
            (CL1, L1),
            (CL2, L2),
            (CL3, L3)
        ]

        pairs.sort() 
        
        CL3mat_ord[row, col] = pairs[0][0]  # lowest CL
        CL2mat_ord[row, col] = pairs[1][0]  # middle CL
        CL1mat_ord[row, col] = pairs[2][0]  # highest CL

        L3mat_ord[row, col] = pairs[0][1]   # L matching lowest CL
        L2mat_ord[row, col] = pairs[1][1]   # L matching middle CL
        L1mat_ord[row, col] = pairs[2][1]   # L matching highest CL

print(f"L1 = np.array({repr(L1mat.tolist())})")
print()
print(f"L2 = np.array({repr(L2mat.tolist())})")
print()
print(f"L3 = np.array({repr(L3mat.tolist())})")
print()
print(f"CL1 = np.array({repr(CL1mat.tolist())})")
print()
print(f"CL2 = np.array({repr(CL2mat.tolist())})")
print()
print(f"CL3 = np.array({repr(CL3mat.tolist())})")
print()
print()
print(f"L1_ord = np.array({repr(L1mat_ord.tolist())})")
print()
print(f"L2_ord = np.array({repr(L2mat_ord.tolist())})")
print()
print(f"L3_ord = np.array({repr(L3mat_ord.tolist())})")
print()
print(f"CL1_ord = np.array({repr(CL1mat_ord.tolist())})")
print()
print(f"CL2_ord = np.array({repr(CL2mat_ord.tolist())})")
print()
print(f"CL3_ord = np.array({repr(CL3mat_ord.tolist())})")
print()