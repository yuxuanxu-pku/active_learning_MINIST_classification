import pickle
import json
import matplotlib.pyplot as plt
import numpy as np
d = pickle.load(open( 'Active-learning-experiment-40.pkl', 'rb'))
print(d)
results = json.loads(json.dumps(d, indent=2, sort_keys=True))
print(results)

# plot the comparison figure
# def performance_plot(fully_supervised_accuracy, dic, models, selection_functions, Ks, repeats):
#     fig, ax = plt.subplots()
#     ax.plot([0,500],[fully_supervised_accuracy, fully_supervised_accuracy],label = 'algorithm-upper-bound')
#     for model_object in models:
#       for selection_function in selection_functions:
#         for idx, k in enumerate(Ks):
#             x = np.arange(float(Ks[idx]), 500 + float(Ks[idx]), float(Ks[idx]))
#             Sum = np.array(dic[model_object][selection_function][k][0])
#             for i in range(1, repeats):
#                 Sum = Sum + np.array(dic[model_object][selection_function][k][i])
#             mean = Sum / repeats
#             ax.plot(x, mean ,label = model_object + '-' + selection_function + '-' + str(k))
#     ax.legend()
#     ax.set_xlim([50,500])
#     ax.set_ylim([40,100])
#     ax.grid(True)
#     plt.show()
#
# models_str = ['SvmModel', 'RfModel', 'LogModel']
# selection_functions_str = ['RandomSelection', 'MarginSamplingSelection', 'EntropySelection']
# Ks_str = ['250','125','50','25','10']
# repeats = 1
# random_forest_upper_bound = 97.
# svm_upper_bound = 94.
# log_upper_bound = 92.47
# total_experiments = len(models_str) * len(selection_functions_str) * len(Ks_str) * repeats
#
# print('So which is the better model? under the stopping condition and hyper parameters - random forest is the winner!')
# performance_plot(random_forest_upper_bound, d, ['RfModel'] , selection_functions_str    , Ks_str, 1)
# performance_plot(svm_upper_bound, d, ['SvmModel'] , selection_functions_str    , Ks_str, 1)
# performance_plot(log_upper_bound, d, ['LogModel'] , selection_functions_str    , Ks_str, 1)