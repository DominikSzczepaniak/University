class CMA_ES:
    def __init__(self, x0, sigma, maxfevals = 10000, popsize = None, weights = None):
        N = x0.shape[0]
        self.dimension = N
        self.chiN = N**0.5 * (1 - 1. / (4 * N) + 1. / (21 * N**2))
        self.lam = 4 + int(3 * np.log(N)) if not popsize else popsize
        print(f"Popsize: {self.lam}")
        self.mu = int(self.lam / 2)
        self.shape = tf.cast((self.lam, N), tf.int32)
        
        if weights:
            self.weights = weights
        else:
            self.weights = np.array([np.log(self.lam / 2 + 0.5) - np.log(i + 1) if i < self.mu else 0
                        for i in range(self.lam)])
            self.weights /= np.sum(self.weights)
        if(self.weights.shape == (self.lam,)):
            self.weights = self.weights[:, np.newaxis]
        self.mueff = np.sum(self.weights)**2 / np.sum(self.weights**2)
        
        self.cc = (4 + self.mueff/N) / (N+4 + 2 * self.mueff/N)
        self.cs = (self.mueff + 2) / (N + self.mueff + 5)
        self.c1 = 2 / ((N + 1.3)**2 + self.mueff) 
        # self.cmu = min([1 - self.c1, 2 * (self.mueff - 2 + 1/self.mueff) / ((N + 2)**2 + self.mueff)])
        self.cmu = 2 * (self.mueff - 2 + 1 / self.mueff) / ((N + 2)**2 + 2 * self.mueff / 2)
        # self.damps = 2 * self.mueff/self.lam + 0.3 + self.cs
        self.damps = 1 + 2 * max(0, np.sqrt((self.mueff - 1)/(N + 1)) - 1) + self.cs

        self.xmean = np.array(x0[:])
        self.sigma = sigma
        self.pc = np.zeros(N) 
        self.ps =np.zeros(N) 
        self.lazy_gap_evals = 0.5 * N * self.lam * (self.c1 + self.cmu)**-1 / N**2
        self.maxfevals = maxfevals
        self.C = np.identity(N)
        self.counteval = 0 
        self.fitvals = []   
        self.best = (x0, None)
        self.condition_number = 1
        self.eigen_values = np.ones(N)
        self.eigen_vectors = np.identity(N)
        self.updated_eval = 0
        self.inv_sqrt = np.ones(N)
        self.B = np.eye(self.dimension)
        self.D = np.eye(self.dimension)

    def _update_eigensystem(self, current_eval, lazy_gap_evals):
        if current_eval <= self.updated_eval + lazy_gap_evals:
            return self
        self.eigen_values, self.eigen_vectors = np.linalg.eig(self.C)
        self.inv_sqrt = self.eigen_vectors @ np.diag(self.eigen_values**-0.5) @ self.eigen_vectors.T
        self.condition_number = self.eigen_values.max() / self.eigen_values.min()
         
    def sample(self):
        z = tf.random.normal(self.shape, dtype=tf.float64)
        z = np.array(z)
        y = z @ (self.B @ self.D)
        x = self.xmean + self.sigma * y
        return x
    
    def update(self, x, fitvals):
        """Zaktualizuj wartoĹci uzyskanych parametrĂłw"""
        self.counteval += fitvals.shape[0] 
        
        #------------------------------------------------------------------------------------------------------
        idx = np.argsort(fitvals)
        x_sorted = x[idx]
        self.fitvals = fitvals[idx] 
        self.best = (x[0], self.fitvals[0])
        taken = x_sorted[:self.mu]

        xdiff = x_sorted - self.xmean
        x_mean = np.sum(xdiff * self.weights, axis=0)
        m = self.xmean + x_mean
        #------------------------------------------------------------------------------------------------------
        y_mean = x_mean / self.sigma 
        pc = (1 - self.cc) * self.pc + np.sqrt(self.cc * (2 - self.cc) * self.mueff) * y_mean
        pcmatrix = pc[:, np.newaxis]

        C_m = np.array([e[:, np.newaxis] * e.T for e in (xdiff / self.sigma)])
        y_s = np.sum(C_m * self.weights[:, np.newaxis], axis=0)

        C = (1 - self.c1 - self.cmu) * self.C + self.c1 * pcmatrix * pcmatrix.T + self.cmu * y_s

        C = (C + C.T)/2.0
        
        #--------------------------------------------------------------------------------------------------------

        D_inv = np.diag(np.reciprocal(np.diag(self.D)))
        C_inv_squared = (self.B @ D_inv) @ (self.B.T)
        C_inv_squared_y = np.squeeze(C_inv_squared @ y_mean[:, np.newaxis])  
        ps = (1 - self.cs) * self.ps + np.sqrt(self.cs * (2 - self.cs) * self.mueff) * C_inv_squared_y  

        sigma = self.sigma * np.exp((self.cs / self.damps) * ((np.linalg.norm(ps) / self.chiN) - 1))

        #--------------------------------------------------------------------------------------------------------
        u, B, _ = tf.linalg.svd(C)
        u = np.array(u)
        B = np.array(B)
        diag_D = np.sqrt(u)
        D = np.diag(diag_D)

        #--------------------------------------------------------------------------------------------------------

        self.pc = pc
        self.ps = ps
        self.C = C
        self.sigma = sigma
        self.B = B
        self.D = D
        self.xmean = m
        return taken
        
    def terminate(self):
        """ZakoĹcz algorytm"""
        if self.counteval <= 0:
            return False
        if self.counteval >= self.maxfevals:
            return True
        if self.condition_number > 1e13:
            return True
        if self.sigma * np.max(self.eigen_values)**0.5 < 1e-13:
            return True
        return False