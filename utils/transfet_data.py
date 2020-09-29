import os
import sys

input_str = "/media/shinan/DATA/ROSbag/180_stereo/180_left_single/rabbish3_2020-08-13-09-18-44/DetectionResult.txt"
output_dir = "/media/shinan/DATA/ROSbag/Cubeslam/mydata/filter_2d_obj_txts_new/"

if __name__ == '__main__':
    f = open(input_str,'r')
    data = f.readlines()
    file_id = 0
    for line in data: 
        result = line.split(':')
        image_name = result[0]
        new_txt_name = str(file_id)
        new_txt_name.rjust(4,'0')
        filepath = output_dir + new_txt_name +'_yolo2_0.15.txt'
        myfile = open(filepath,'w'+'a')
        detection_ret = result[1]
        things = detection_ret.split(';')
        for cur_stuff in things:
            params = cur_stuff.split()
            params_size = len(params)
            if params_size > 1:
                class_name = params[0]
                class_score = params[1]
                class_xmin = params[2]
                class_ymin = params[3]
                class_xmax = params[4]
                class_ymax = params[5]   
                width = int(class_xmax) - int(class_xmin)
                height = int(class_ymax) - int(class_ymin)         
                new_string = class_name + ' ' +class_xmin + ' ' + class_ymin + ' '+ str(width) + ' ' + str(height)
                myfile.write(new_string)
                myfile.write('\r\n')
        file_id=file_id+1
