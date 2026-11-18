# 输入约定

所有TSV均含表头，所有ID是不透明字符串。类型行、层行、动作行不保证排序。

| 文件 | 语义 |
|---|---|
| study.json | horizon=4，已知有限面板与无放回语义，路径budget，总体harm_limit，成本惩罚cost_penalty，合成总体与支持假设说明。 |
| strata.tsv | stratum_id、share、panel_size、conditional_harm_limit，后者为该层J/E上限kappa_s；panel_size是已知整数成员数量；原始总体层比例，和为1。 |
| types.tsv | type_id及Y0、YA、YB、YAB、YR五个0/1潜在反应。 |
| actions.tsv | action_id、operation、response_column、cost。response_column=Y0的动作是对照。 |
| channels.tsv | action_id、stratum_id、true_response、observed、probability。observed为0、1或`.`；每个动作/层/真实反应三种读数概率和为1。此表是原始B先验下的读数边际诊断，联合读数以batch_channels为准。 |
| capture.tsv | cohort_id、stratum_id、type_id、p_capture，为该层该类型按原始B先验平均的入组边际诊断。联合模型以batch_capture为准。 |
| batch_weights.tsv | stratum_id、batch_id、probability；每层B先验和1，给定层在入组前与成员类型独立；整个实验共用一次抽取。 |
| batch_channels.tsv | action_id、stratum_id、true_response、observed、batch_id、probability；每个动作/层/真实反应/B下三读数和1，是实际条件测量通道。 |
| batch_capture.tsv | cohort_id、stratum_id、type_id、batch_id、p_capture；给定U及同一B的成员入组概率。 |
| observed.tsv | record_id、cohort_id、stratum_id、action_id、observed、probability。给定成功入组的单项读数概率。 |
| observed_pairs.tsv | record_id、cohort_id、stratum_id、action1_id、observed1、action2_id、observed2、probability。同一单位两份克隆等分样本的联合读数概率，给定成功入组。 |
| observed_distinct.tsv | record_id、cohort1_id、cohort2_id、stratum_id、action1_id、observed1、action2_id、observed2、probability_lower、probability_upper。两名不同成员均匀有序无放回抽取，分别尝试进入两个cohort，给定两者都入组后的成对技术读数期望包络。 |
| support.tsv | stratum_id、type_id、allowed，false对应q分量必须为0。true仅表示允许，不保证实际非零。 |
| queries.tsv | query_id、stratum_id、scientific_label。`*`表示原始总体；指定层的查询使用层内概率。 |
| query_events.tsv | query_id、type_id、numerator、denominator，两个0/1掩码，分子包含于分母。 |
| protocols.json | 协议ID到完整策略树的对象。null为立即停止；非空节点精确包含unit、action与children，unit为整数0或1；children有`0`、`1`、`.`三个子树。 |

总体观测用原始share加权。指定层观测只纳入该层，层权重取1。共享隐含批次联合公式见PROJECT_REQUEST.md：先对同一个B的入组/读数乘积积分，再合并总体分子分母。单项和克隆对入组一次；不同成员入组两次，B只抽一次。不能相乘各自边际概率。

总体查询的分子、分母均按原始share加权；指定层查询只在该层取概率，层权重1。对查询先求分母在完整可行集合上的上下界，再对正分母分布求同一q的条件比率上下界。

协议是否违规应审查全部结构路径，包括缺失读数路径，不以某个推测的总体下该路径概率小为理由忽略。`repeated_unit_action`指路径重复同一(unit,action)，不同unit使用相同action允许；`horizon_exceeded`指路径动作数超过4；`path_budget_exceeded`指某路径成本大于budget+1e-9。原因按ASCII顺序逗号连接，无违规记valid。输入保证结构和动作ID本身有效；不需要猜测修复非法协议。max_depth和max_path_cost对所有候选都按其结构计算，即便其非法。

主任务的q须等于整数计数除以已知N；只有明确标记的连续q/对称成员对耦合外松弛比较使用任意连续q和满足边际一致性的M；其定义见PROJECT_REQUEST.md。输入观测为精确重复技术测量期望，不是把一次抽样频数当精确概率。

参考最优值不依赖任何私有生成分布。它只取决于上述输入约束，不允许从某个拟合分布或随机抽样近似替代所有可行q。

双成员主问题的有序类型对概率仍为n_s(u)*(n_s(v)-I[u=v])/[N_s*(N_s-1)]，随后对同一个B积分两槽位的批次条件入组和读数联合量。每个有标号成员有序对权重1/[N_s*(N_s-1)]；同类型多个成员的类型对质量要乘计数。外松弛仅以对称M替代这一物理对质量，全部B积分、观测和边际一致性保留。批次条件入组严格正，共同分母正；包络等价两条分子分母线性不等式。

所有层共用同一协议混合x。J_s/E_s是该层内部的期望人数之比，不乘share；总体事件R/H/C按原始share加权。J_s每个受伤成员只计一次，E_s每个暴露的基线阳性成员只计一次，均非“至少一人”的事件概率。观察cohort的共同入组分母与目标实验的条件暴露人数E_s是不同对象。
