class ComBand:
    def __init__(self, pipeline, decoder):
        # Pipeline Parameter
        self.decoder = decoder
        self.allalgs = sum(pipeline, [])
        self.algsInEachSteps = [len(step) for step in pipeline]
        self.NPipelineSteps = len(self.algsInEachSteps)

        # Combinatorial Bandit parameter
        self.K = len(self.allalgs)
        self.p = np.zeros(self.K)
        self.q = np.zeros(self.K)+(1.0/self.K)
        self.gamma = 0.2
        self.mu = 0.2

        # index for choice pipelines
        self.step_index = [0]
        for i, ni in enumerate(self.algsInEachSteps):
            self.step_index += [ni + self.step_index[i]]

        print("COMBAND, gamma:", self.gamma, self.step_index)

    def initialize(self, setting=None):
        if setting is None:
            pass
        else:
            # TODO
            ## 実験設定を外部ファイルに出力して
            ## 実験のパラメータを読み出せるようにする
            pass

    def save_parameter(self):
        filename = get_id(prefix="ComBandParams")
        # TODO
        ## パラメータの保存形式を決める

    def get_E(self, k_vector):
        edge = np.zeros([self.K, self.K])
        node = np.argwhere(k_vector==1).flatten().tolist()

        for i in range(self.NPipelineSteps-1):
            node_i, node_j = node[i], node[i+1]
            edge[node_i, node_j] = 1
            edge[node_j, node_i] = 1

        return edge

    def get_next_path(self):
        self.p = (1.0 - self.gamma)*self.q + self.gamma/self.K
        pathI = []

        for i in range(self.NPipelineSteps):
            left, right = self.step_index[i], self.step_index[i+1]
            temp = weighted_random_choice(self.p[left:right],\
                                          itemset=self.allalgs[left:right])
            pathI += [temp]

        return pathI

    def update(self, path, score):
        # calc loss for every edge
        k_vector = np.array(self.decoder.decode(path)) # 1s
        Eps = self.get_E(k_vector) # E{ps}
        ones_ones_T = self.NPipelineSteps # [1s.1s^T]
        InvP = np.linalg.pinv(Eps*ones_ones_T)

        # TODO
        ## lossが最小になるように計算を行っている
        xhat = (-1.0)*score*(InvP.dot(k_vector))

        # update parameter
        for k in range(self.K):
            q_tk = self.q[k] # q_t(k)
            v_k = np.eye(self.K, dtype=int)[k] # v(k)
            lt_vk = xhat.dot(v_k) # l_t v(k)
            exp = np.exp((-1)*self.mu*lt_vk)
            self.q[k] = q_tk * exp
