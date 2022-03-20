import pandas as pd
import numpy as np
import io
import csv


# path = '../'
# filename = 'FloatingInfo_mk11.csv'
# file_with_absadress = path + filename
# file = pd.read_csv(file_with_absadress,sep="[;]")
# # print(file)
# print(file.columns)

# ytj_list_title=[file.columns[0],file.columns[1],file.columns[8],file.columns[9],file.columns[10]]
# print("ytj_list_title:",ytj_list_title)

# part=file["part"]
# time=file["time [s]"]
# center_x=file["center.x [m]"]
# center_y=file["center.y [m]"]
# center_z=file["center.z [m]"]
# dataframe = pd.DataFrame({'part':part, 'time [s]':time,'center.x [m]':center_x,'center.y [m]':center_y,'center.z [m]':center_z})
# dataframe.to_csv("np_sum_result.csv",index=False,sep=';',float_format = '%.9f')

# print("center_x:",center_x[:][:])
# print(file["part"]+file["time [s]"])
# 解析一个csv文件，将解析后的结果写入到求和文件中
# 所有粒子都会调用该函数，每次调用完成后，结果都会写入到求和文件中
def handle_single_file(handlefilename,result_sum_file,resultfilename):
    # 解析目标数据文件：handlefilename
    # 将数据求和写入求和数据文件
    csv_sumFile = open("result_sum_file","w")
    writer = csv.writer(csv_sumFile)
    writer.writerow(file.columns)
    pass

# 最终结果文件
# 打开求和后的文件，对于每一时刻的粒子坐标和进行除粒子数
# 所得结果写入到最终结果文件sum_np_file.csv--->final_result.csv
def divid_np_data():
    pass
# 定义粒子数，明确调用多少次handle_single_file()函数
def main():
    num_particles = 33
    name_prefix='../FloatingInfo_mk'
    name_form = '.csv'
    file_name = ''
    result_sum_file ="np_sum_result.csv"
    result_file = 'result_file.csv'
    for i in range(num_particles):
        # print(i,"\n")
        if i==0:
                file_name = name_prefix+str(i+11)+name_form
                print("打开文件：",file_name)
                file = pd.read_csv(file_name,sep="[;]")
                part=file["part"]
                time=file["time [s]"]
                center_x=file["center.x [m]"]
                center_y=file["center.y [m]"]
                center_z=file["center.z [m]"]
                dataframe = pd.DataFrame({'part':part, 'time [s]':time,'center.x [m]':center_x,'center.y [m]':center_y,'center.z [m]':center_z})
                dataframe.to_csv("np_sum_result.csv",index=False,sep=';',float_format = '%.9f')
                continue
        file_name = name_prefix+str(i+11)+name_form
        print("打开文件：",file_name)
        file = pd.read_csv(file_name,sep="[;]")
        file2 = pd.read_csv(result_sum_file,sep="[;]")
        
        part=file["part"]
        time=file["time [s]"]
        center_x=file["center.x [m]"]
        center_y=file["center.y [m]"]
        center_z=file["center.z [m]"]
        
        part2=part
        time2=time
        center_x2=file2["center.x [m]"]+center_x
        center_y2=file2["center.y [m]"]+center_y
        center_z2=file2["center.z [m]"]+center_z
        dataframe = pd.DataFrame({'part':part2, 'time [s]':time2,'center.x [m]':center_x2,'center.y [m]':center_y2,'center.z [m]':center_z2})
        dataframe.to_csv("np_sum_result.csv",index=False,sep=';',float_format = '%.9f')

        file_name = ''
    # handle_single_file(filename,result_sum_file,result_file)
    # divid_np_data()
    pass
main()