import os
#遍历目标文件夹的文件
mubiao_path = r"F:\project\D01_20230524\picture"
mubiao = os.listdir(mubiao_path)
#遍历参考文件夹的文件
cankao_path = r"F:\project\D01_20230524\biaozhu"
cankao = os.listdir(cankao_path)
#将后缀去掉
mubiao_1 = []
for i in mubiao:
    i_s = i.split('.')
    i = i_s[0]
    mubiao_1.append(i)
#print(mubiao_1)
cankao_1 = []
for i in cankao:
    i_s = i.split('.')
    i = i_s[0]
    cankao_1.append(i)
#print(cankao_1)

different_values = set(mubiao_1) - set(cankao_1)
print('没有对应的数量：' + str(len(different_values)))
begin = input('是否删除y/n\n')

if begin == 'y' :
    #对比删除
    for ele in mubiao_1:
        if ele not in cankao_1:
            weizhi = mubiao_1.index(ele)
            dizhi_part = mubiao[weizhi]
            dizhi = mubiao_path+'\\'+dizhi_part
            os.remove(dizhi)

#输出检查结果
if cankao_1 == mubiao_1 :
     print('已经全部对应')
else:
     print('以下是没有对应的文件')
     for ele in mubiao_1:
         if ele not in cankao_1:
             print(ele)
'''
#检查
for ele in cankao_1:
    if ele not in mubiao_1:
        weizhi = cankao_1.index(ele)
        dizhi_part = cankao[weizhi]
        dizhi = cankao_path+'\\'+dizhi_part
        os.remove(dizhi)
'''