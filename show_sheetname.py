
import time
import pandas as pd
import numpy as np
from multiprocessing import Pool

import os

def show_sheet_name(file):

    xl =  pd.ExcelFile(file)
    all_sheet = xl.sheet_names  # see all sheet names

    return all_sheet


def jion_sheets(file,chose_type,filename,TO,AXIS,indexs):
    """

    :param file: 需要合并的文件
    :param chose_type: 合并的类型
    :param filename: 原始文件名 eg：ls.xlsx -- ls
    :param TO: 合并方向
    :param indexs: 取决于TO参数，左右合并需要指名合并轴
    :return:
    """

    datas = pd.DataFrame()
    sheet_names = show_sheet_name(file)
    for i,sheet_name in enumerate(sheet_names):
        # print('即将处理%s'%sheet_name)
        try:
            df = pd.read_excel(file,sheet_name=sheet_name,header=0)
            df['from'] = filename+"_"+sheet_name
        except:
            pass
        if AXIS == 0:
            datas = pd.concat([datas, df], axis=AXIS, join=chose_type, ignore_index=True,sort=True)
        elif AXIS == 1:
            print(chose_type)
            datas = datas.append(df)



    return datas


def main(files,chose_type,TO,AXIS,indexs):
    """

    :param files: 目标文件
    :param chose_type: 合并类型
    :param TO: 合并方向
    :param indexs: 索引列
    :return:
    """
    print('Parent process %s.' % os.getpid())
    print(AXIS,indexs,'================')
    t1 = time.clock()
    all_data  =pd.DataFrame()
    p = Pool(4)
    for file in files:
        (filepath, tempfilename) = os.path.split(file)
        (filename, extension) = os.path.splitext(tempfilename)

        if AXIS == 0:
            res = p.apply_async(jion_sheets, args=(file,chose_type,filename,TO,AXIS,indexs))
            all_data = pd.concat([all_data, res.get()], axis=AXIS, join=chose_type, ignore_index=True,sort=True)

        elif AXIS == 1:
            print('横向全链接')
            res = p.apply_async(jion_sheets, args=(file, chose_type, filename,TO,AXIS,indexs))
            # all_data = all_data.append(res.get())
            all_data =pd.concat(all_data,axis=0, join=chose_type, ignore_index=True, sort=True )



    p.close()
    p.join()

    t2 = time.clock()
    ts = t2-t1
    try:
        all_data.set_index('from',inplace=True)
    except:
        pass
    all_data.to_excel('./%s_%s_result.xlsx'%(chose_type,str(len(files))))
    print(all_data)
    print("用时{}s".format(ts))
    print('All subprocesses done.')
    return 1




def jion_left_right(left_files,right_files,indexs,chose_type,header):
    try:
        df_left = pd.read_excel(left_files[0],header=header)
        df_right = pd.read_excel(right_files[0],header=header)
        result = pd.merge(df_left, df_right, on=indexs, how=chose_type)
        result.to_excel('./%s.xlsx'%chose_type)
        print('合并完成')
    except:
        print('未知错粗')
        pass


def cols_name(file,nums):
    try:
        df = pd.read_excel(file,header=nums,nrows=5)
        cols = df.columns.tolist()
        return cols
    except:
        pass





if  __name__ =="__main__":
    files = [r'C:\Users\Administrator\Desktop\cy\excs\9.xlsx',r'C:\Users\Administrator\Desktop\cy\excs\10.xlsx']
    main(files)
