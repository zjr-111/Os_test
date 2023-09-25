import os

# 经过处理后的视频文件夹
mubiao_path = r'F:\project\vidios'

# 刚从硬盘上拷贝下来还没进行剪辑的视频文件夹
folder_path = r'F:\project\after'

# 获取文件夹内的所有文件名
file_names = os.listdir(folder_path)
mubiao_names = os.listdir(mubiao_path)

print(file_names)
print(mubiao_names)

a = 0
for i in mubiao_names:
    old_name = os.path.join(mubiao_path, i)
    new_name = os.path.join(mubiao_path, file_names[a])
    print(old_name)
    print(new_name)
    os.rename(old_name, new_name)
    a += 1
