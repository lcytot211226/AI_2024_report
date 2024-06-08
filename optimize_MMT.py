class optimize_MMT():
    def optimize(X, y):
        def f(a, u, v):
            total = 0
            for i in range(4):
                for j in range(4):
                    total += a[4*i+j] * (u**(3-i)) * (v**(3-j))
            return total
        
        max_value, max_posi = 0, [0,0]
        
        h = 1/500
        for i in range(500):
            for j in range(500):
                value = f(y, i*h, j*h)
                if value > max_value:
                    max_value = value
                    max_posi  = [i*h, j*h]

        opti_x = []
        for i in range(6):
            A = [ X[j][i] for j in range(16) ]
            opti_x.append( f(A, max_posi[0], max_posi[1]) )
            
        return opti_x