# DRY - don't repeat yourself

dict_1 = {1: 1, 2: 2}

dict_2 = {3: 3, 4: 4}

merged_dict = {**dict_1, **dict_2}
print(merged_dict)