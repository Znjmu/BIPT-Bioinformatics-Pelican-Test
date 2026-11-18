# 输出、分层条件伤害与全局证书

一次生成14项。TSV表头及列顺序精确一致，下文示意空格实际用制表符。数值有限，绝对1e-8+相对1e-6容差；布尔小写true/false。键唯一，ID按输入，不硬编码；概率向量非负和1。未定义比率上下端点写NA，但分母区间仍为数值（如[0,0]），不把分母界也写NA。

1. estimands.tsv：`query_id lower upper denominator_lower denominator_upper status n_attainable_values relaxed_lower relaxed_upper relaxed_denominator_lower relaxed_denominator_upper`。每查询一行。整数面板锐界/分母范围/status规则见主说明；n_attainable_values为正分母上条件值按小数后10位归并的个数，undefined为0。后四列为指定连续q/对称M外松弛界与分母范围，保留三类全部观测；该比较同时放松整数网格与固定面板二次抽样关系。
2. protocol_audit.tsv：`protocol_id valid reason max_depth max_path_cost`。所有候选一行，原因合法valid，违规按数据字典ASCII顺序逗号连接；非法也算全结构深度/成本。
3. protocol_scores.tsv：`protocol_id worst_utility best_utility lower_help upper_help upper_harm min_cost max_cost feasible_harm`。全部合法协议。前七个数值为全部物理面板上U最小/最大、H最小/最大、总体事件R最大、C最小/最大。feasible_harm=true当且仅当单个协议同时满足总体伤害上限和所有层J/E限制；undefined层约束为空。不要仅按总体事件R判断。
4. protocol_safety.tsv：`protocol_id stratum_id lower_exposure upper_exposure lower_conditional_harm upper_conditional_harm status feasible_conditional`。全部合法协议×全部层。exposure为E_s人数期望在全部物理面板上的最小/最大；conditional_harm为正E_s物理面板上的J_s/E_s最小/最大。status仅defined或undefined。后者两个比率端点NA，但exposure仍数值。feasible_conditional按上界≤该层kappa_s+1e-9；undefined时true（空约束，不等于比率0）。
5. mixtures.tsv：`decision protocol_id probability`。decision仅unconstrained、robust，每类列全部合法协议，包括零概率。
6. mixture_metrics.tsv：`decision worst_utility best_utility lower_help upper_help upper_harm min_cost max_cost protocol_aware_worst_utility separate_cost_bound with_replacement_worst_utility pooled_confirmation_worst_utility reset_batch_worst_utility`。每类一行，按自己所交x重算。前七项为同一完整物理面板上的组合极值。protocol_aware=sum x_pi*min_n U_pi；separate_cost=min_n H_x-lambda*max_n C_x。两个错误模型只用于对相同x的比较：with_replacement把槽位改为独立均匀有放回，H/R/C定义不变；pooled_confirmation保持无放回，将所有Y0=0槽位上实际测试且真实阳性的不同非对照response_column合并，至少两种即计H，R/C不变。reset_batch在每一步独立重抽B，即按channels.tsv边际生成该错误实验的路径分布，再积分H/R/C。三项都保持原x和同一整数面板集合求最坏U，不能据此重新拟合观测或选择真正最优x。
7. mixture_safety.tsv：`decision stratum_id lower_exposure upper_exposure lower_conditional_harm upper_conditional_harm status feasible_conditional`。两类组合×全部层；按相同x先组合J/E的分子分母，再对正分母物理面板取比率极值。规则与第4项相同，不能照抄逐协议比率平均。
8. census_witnesses.tsv：`witness_id stratum_id type_id count`。每见证含全部层×类型，零计数也列，非负整数且层和N，满足全部三类观测/支持。数学整数的1.0可接受，整数误差≤1e-9。非undefined查询须交`QUERY_ID:lower`、`QUERY_ID:upper`且正分母；另交unconstrained:utility、unconstrained:risk、robust:utility、robust:risk达到自己组合的最坏U与最大总体事件R。对自己组合在某层的条件伤害率defined时，再交`DECISION:conditional:STRATUM_ID`，达到该层J/E上界且E>1e-10；undefined时不交该端点。可另加任意唯一ID供证书引用，每个额外物理面板也须完整可行。不能把非整数证书平均计数冒充物理见证。
9. nature_weights.tsv：`decision side witness_id probability`。decision两类；side为utility、risk或`conditional:STRATUM_ID`（每层一个side）。每类每side至少一行，概率非负各和1，引用可行物理见证，不重复三字段键。可省略零权重；即使对应乘数为0，该side仍交一个任意可行面板分布。权重不必是最坏比率见证，不要求参考ID或向量。
10. certificates.json：顶层unconstrained、robust，各含eta、risk_multiplier、conditional_multipliers、global_upper_bound。conditional_multipliers为全部stratum_id到非负rho_s的映射；risk_multiplier为非负rho_0。无约束类所有rho为0。记A_s(n,pi)=J_s(n,pi)-kappa_s E_s(n,pi)，wU/wR/ws为对应nature_weights，则对每个合法协议都须满足：sum_n wU_n U_pi(n)-rho_0*sum_n wR_n R_pi(n)-sum_s rho_s*sum_n ws_n A_s(n,pi)≤eta。global_upper_bound=eta+rho_0*harm_limit（各A_s约束右端为0，不再加sum rho_s*kappa_s），并与自己组合的最坏U相差≤1e-6；全部不等式违反≤1e-6。不同side可用不同面板混合，它们是数学上界证书，不是拼成一个物理面板。允许额外普通字符串notes注释，不扣分；其他未知顶层决策按额外对象处理。证书/组合/见证均允许非唯一，按可行性与达到值验证。
11. summary.json：以下字段必须包含，允许另加说明。计数JSON整数、布尔JSON布尔、集合无重复字符串数组；纯协议并列按差≤1e-8全部保留：n_strata、n_conditional_groups、conditional_safety_enforced（true，指robust问题执行新约束）、n_response_types、n_feasible_censuses（完整跨层计数组合数，非成员标号排列数）、n_protocols、n_valid_protocols、n_invalid_protocols、n_identified、n_not_identified、n_undefined、n_queries_with_finite_vs_relaxed_bound_difference（上下界任一差>1e-7或定义状态不同，不比较分母界）、best_pure_unconstrained_value、best_pure_robust_value、best_pure_unconstrained_ids、best_pure_robust_ids、best_mixed_unconstrained_value、best_mixed_robust_value、robust_randomization_strictly_beneficial（稳健混合比稳健纯大>1e-8）、sampling_without_replacement、biological_independence_assumed、natural_causality_established、persistent_shared_batch（true）、batch_independent_of_biological_type_before_capture（true）、capture_changes_batch_posterior（true）。
12. interpretation.md：按R01至R10分别成节，给本例证据。核心正确且所需本例证据齐3.5，核心正确但缺本例证据1.75，缺失/明确科学错误/错误通用公式/与正确表格反向冲突0。同一错误不重复扣，不以正确表格抵消错误正文。
13. evidence.png：至少1200×800，清楚展示整数/外松弛查询界与状态、纯/混合关键值、总体伤害上限与各层条件伤害率/上限（undefined明确标注）。阈值、单位与表/正文一致，不能标成置信区间，也不能把人数期望叫作事件概率。
14. README.md：运行、依赖、算法、全部枚举完备性、复核与新向量证书验证。

| 项目 | 要求，每项3.5分 |
|---|---|
| R01 | 说明完整整数面板的归一/支持/三类共同观测约束与穷举，给本例N、数量、残差/包络违反量及支持限制；技术期望不是实现频数，支持不是自然因果证明。 |
| R02 | 给本例点/部分/undefined数量、具体查询/分母/可达值；Dmin=0<Dmax与Dmax=0不同；正确解释连续q/对称M外松弛保留全部观测、放松网格与二次关系，给本例实际比较或相等证据，非置信区间。 |
| R03 | H/R是实验事件，J/E的分子分母是按成员最多计一次的人数期望；同槽位真实双路线、基线阳性伤害、给定同一个B后的技术噪声条件独立，说明边际化B产生相关，给实际批次通道/联合读数与人数/事件区别证据，不声称临床安全或疗效。 |
| R04 | 无放回成员对、同成员克隆与两成员都入组的不同分母，给本例N、实际双入组cohort顺序/包络/概率/分母与有放回诊断；给本例入组前后B分布及联合分子分母证据，不把观测富集后的类型或B权重套给目标实验。 |
| R05 | 全结构路径预算、最多四步、禁止重复(unit,action)但允许跨槽位同动作；给所有非法ID/原因/深度/成本，不用平均成本或低概率路径豁免。 |
| R06 | 所有层同一x，面板可知x但不能依协议/成员/读数重选；物理面板与不同side证书混合区别；给共同面板与protocol_aware实际值及证书支持数量，允许相等；B是已知随机量，不能当对抗状态或逐步重抽。 |
| R07 | 全部纯最优集合、两类混合值/实际支撑概率、总体R及每层J/E与上限；解释先组合人数再取比率、undefined空约束非风险0、STOP不能修复固定协议的条件伤害率；给本例严格收益或相等证据。 |
| R08 | 实际x比较min(H-lambda*C)与minH-lambda*maxC（后者为下界）；给本例成本范围、路径成本机制与真实差异/相等，深度相同不保证成本相同；给同x的reset_batch错误实验实际比较，若相等照实举证，不能把边际化批次等同每步重抽。 |
| R09 | 实际整数见证层和/原始观测残差/包络违反量/达到值；单见证只证明可达，需对全部合法协议的向量上界证书。给实际eta、rho_0、各rho_s、上界、最大违反与上下界差，不能把松上界叫全局精确最优。 |
| R10 | 实际PNG、summary、正文与所有表的科学含义/维度/人数与概率单位/阈值/参数/状态/数值一致；已计R01-R09的同错不重复扣。 |

数值60：查询10、协议指标8、审查4（合法合计1、两类非法各1.5）、最优组合6、组合指标6、协议条件安全表4、组合条件安全表4、整数见证6、全局证书8、summary4。表按完整正确行比例计；组合及其安全指标按自己x验证。见证通常查询/总体组合/条件上界各2；若自己两类组合所有层均undefined则查询/总体组合各3。有效可选证书面板不能稀释必交端点缺失。复跑5要求入口退出0、全部14项非空且PNG有效足尺寸。公开20%、两隐藏各40%；科学未审完只报区间。所有模型产物交同一个固定评估者，按首次运行前冻结标准；目标分数不用于追改规则。
