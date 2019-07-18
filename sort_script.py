import shutil
import os
# Каталог с набором данных
data_dir = r"C:\Users\username\Downloads\letters3"
finall_dir = r"C:\Users\username\Downloads\Finally"
if os.path.exists(finall_dir):
    shutil.rmtree(finall_dir)
os.mkdir(finall_dir)
# Каталог с данными для обучения
train_dir = os.path.join(finall_dir, 'train')
# Каталог с данными для проверки
val_dir = os.path.join(finall_dir, 'val')
# Каталог с данными для тестирования
test_dir = os.path.join(finall_dir, 'test')
# Часть набора данных для тестирования
test_data_portion = 0.15
# Часть набора данных для проверки
val_data_portion = 0.15
# Количество элементов данных в одном классе
nb_images = 200
def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    for i in range(1, 34):
        os.makedirs(os.path.join(dir_name, f"{i}"))
create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)
def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        for j in range(1, 34):              # j номер буквы в русском алфавите
            if j // 10 < 1:
                j_str = '0' + str(j)
            else:
                j_str = str(j)
            shutil.copy2(os.path.join(source_dir, f"{j_str}_" + str(i+231) + ".png"),
                        os.path.join(dest_dir, f"{j}"))
start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))
start_test_data_idx = int(nb_images * (1 - test_data_portion))
print(start_val_data_idx)
print(start_test_data_idx)
copy_images(0, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, start_test_data_idx, data_dir, val_dir)
copy_images(start_test_data_idx, nb_images, data_dir, test_dir)
