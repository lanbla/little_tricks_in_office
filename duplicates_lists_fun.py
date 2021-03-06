#本函数获取两个list，去除各自重复项目形成set，比较两个sets，并返回其交集中的元素
# # little_tricks_in_office
# Some useful tricks for office use. 一些办公小技巧
#
# 1. duplicates_lists_fun.py
# It creates a function duplicates_in_two_lists(path_a,path_b) which could be used to get duplicate items in two lists. It reads in two single-column .csv files, gets rid of duplicate items respectively, and return the intersection as a list.
# 函数duplicates_in_two_lists(path_a,path_b) 获取可以用来获取两个list的重复项目。原理是读取两个单列csv文件，去除各自重复项目形成set，以list形式返回其交集。


def readCSV2List(filePath):
    try:
        file = open(filePath, 'r')  # , encoding="gbk")  # 读取以utf-8
        context = file.read()  # 读取成str
        list_result = context.split("\n")  # 以回车符\n分割成单独的行
        # 每一行的各个元素是以【,】分割的，因此可以
        length = len(list_result)
        for i in range(length):
            list_result[i] = list_result[i].split(",")
        return list_result
    except Exception:
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();  # 操作完成一定要关闭


def writeList2CSV(myList, filePath):
    try:
        file = open(filePath, 'w', encoding='utf-8-sig')
        for items in myList:
            for item in items:
                file.write(item)
                file.write(",")
            file.write("\n")
    except Exception:
        print("数据写入失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();  # 操作完成一定要关闭


# ————————————————
# 版权声明：本文为CSDN博主「新手村的0级玩家」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u011446177/java/article/details/79155670
# 以上代码来源见链接
def duplicates_in_two_lists(path_a,path_b):
    try:
        list_a = readCSV2List(path_a) #读取路径为path_a的csv格式存储的列a, 建议用Path()处理文件路径./
                                    # read in list a stored in a csv file path_a, Path() is suggested.
        list_b = readCSV2List(path_b)
        set_a = set() #初始化一个集合
        set_b = set()
        for x in range(len(list_a)):
            set_a.add(tuple(list_a[x])) #将list a的内容放入set a, put all elements in list a into set a
        for x in range(len(list_b)):
            set_b.add(tuple(list_b[x]))
        return list(set_a & set_b) #获取交集. Get intersection of set a and b.
    except Exception:
        print("查找重复数据失败，请检查文件路径及文件编码是否正确")


#以下为应用示例. Examples
#
# from pathlib import Path
#
# patha = "file_path_a"
# pathb = "file_path_b"
#
# set_inter = set()
# set_inter = duplicates_in_two_lists(Path(patha),Path(pathb))
# print("The two lists has ", len(set_jiaoji), " items in common after eliminating their respective /
# duplicate items.")
#
# writeList2CSV(set_inter,
#               Path("file_path_set_inter"))


