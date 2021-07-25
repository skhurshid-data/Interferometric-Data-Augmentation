import os
import glob
import json
import ntpath
import cv2


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


#window = [2,3,4,5]
#window = [2,3,4]
window = [2,3]

input_path = "/home/reserved/Sumair/concatenation/vertic_con/vert_Input_images"
output_path = "/home/reserved/Sumair/concatenation/vertic_con/vert_output_images"
dict_path = "/home/reserved/Sumair/concatenation/vertic_con"

images = sorted([f for f in glob.glob(os.path.join(input_path , "**", "*.png"), recursive=True)])
print("Total Images: ",len(images))

# w = 2

# [{1,1,2},{1,2,3},{1,3,4},{1,4,4},{2,1,2},{2,2,3},{2,3,4},{2,4,4}]

two_array = []
three_array = []
#four_array = []
#five_array = []
index = 0
for w in window:
    scale_percent = 1/w
    for x in range(0,len(images),1):
        for y in range(0,len(images),1):
            if w == 2:
                image_list = [path_leaf(images[x]), path_leaf(images[y])]                
                image_1 = cv2.imread(os.path.join(input_path,image_list[0]))
                image_2 = cv2.imread(os.path.join(input_path,image_list[1]))
                width = int(image_1.shape[1])
                height = int(image_1.shape[0] * scale_percent)
                dim = (width, height)
                image_1_resized = cv2.resize(image_1, dim, interpolation = cv2.INTER_AREA)
                image_2_resized = cv2.resize(image_2, dim, interpolation = cv2.INTER_AREA)
                v_img = cv2.vconcat([image_1_resized, image_2_resized])
                output_image_name = 'image_vert_' + str(index) + '.png'
                output_image_path = os.path.join(output_path, output_image_name)
                cv2.imwrite(output_image_path, v_img)
                two = {"image_name" : output_image_name, "image_list" : image_list}
                two_array.append(two)
                index +=1
            elif w == 3:
                if y != len(images)-1:
                    image_list = [path_leaf(images[x]), path_leaf(images[y]), path_leaf(images[y+1])]
                else:
                    image_list = [path_leaf(images[x]), path_leaf(images[y]),path_leaf(images[y])]
                image_1 = cv2.imread(os.path.join(input_path,image_list[0]))
                image_2 = cv2.imread(os.path.join(input_path,image_list[1]))
                image_3 = cv2.imread(os.path.join(input_path,image_list[2]))
                width = int(image_1.shape[1])
                height = int(image_1.shape[0] * scale_percent)
                dim = (width, height)
                image_1_resized = cv2.resize(image_1, dim, interpolation = cv2.INTER_AREA)
                image_2_resized = cv2.resize(image_2, dim, interpolation = cv2.INTER_AREA)
                image_3_resized = cv2.resize(image_3, dim, interpolation = cv2.INTER_AREA)
                v_img = cv2.vconcat([image_1_resized, image_2_resized, image_3_resized])
                output_image_name = 'image_vert_' + str(index) + '.png'
                output_image_path = os.path.join(output_path, output_image_name)
                cv2.imwrite(output_image_path, v_img)
                three = {'image_name' : output_image_name, 'image_list' : image_list}
                three_array.append(three)
                index +=1
            # elif w == 4:
                # if y != len(images)-1:
                    # image_list = [path_leaf(images[x]), path_leaf(images[y]), path_leaf(images[x]), path_leaf(images[y+1])]
                # else:
                    # image_list = [path_leaf(images[x]), path_leaf(images[y]),path_leaf(images[x]),path_leaf(images[y])]
                # image_1 = cv2.imread(os.path.join(input_path,image_list[0]))
                # image_2 = cv2.imread(os.path.join(input_path,image_list[1]))
                # image_3 = cv2.imread(os.path.join(input_path,image_list[2]))
                # image_4 = cv2.imread(os.path.join(input_path,image_list[3]))
                # width = int(image_1.shape[1])
                # height = int(image_1.shape[0] * scale_percent)
                # dim = (width, height)
                # image_1_resized = cv2.resize(image_1, dim, interpolation = cv2.INTER_AREA)
                # image_2_resized = cv2.resize(image_2, dim, interpolation = cv2.INTER_AREA)
                # image_3_resized = cv2.resize(image_3, dim, interpolation = cv2.INTER_AREA)
                # image_4_resized = cv2.resize(image_4, dim, interpolation = cv2.INTER_AREA)
                # v_img = cv2.vconcat([image_1_resized, image_2_resized, image_3_resized, image_4_resized])
                # output_image_name = 'image_vert_' + str(index) + '.png'
                # output_image_path = os.path.join(output_path, output_image_name)
                # cv2.imwrite(output_image_path, v_img)
                # four = {'image_name' : output_image_name, 'image_list' : image_list}
                # four_array.append(four)
                # index +=1
 #           elif w == 5:
 #               if y != len(images)-1:
 #                   image_list = [path_leaf(images[x]), path_leaf(images[y+1]), path_leaf(images[x]), path_leaf(images[y+1]), path_leaf(images[x])]
 #               else:
 #                  image_list = [path_leaf(images[x]), path_leaf(images[y]),path_leaf(images[x]),path_leaf(images[y]),path_leaf(images[x])]
 #              image_1 = cv2.imread(os.path.join(input_path,image_list[0]))
 #              image_2 = cv2.imread(os.path.join(input_path,image_list[1]))
 #              image_3 = cv2.imread(os.path.join(input_path,image_list[2]))
 #              image_4 = cv2.imread(os.path.join(input_path,image_list[3]))
 #               image_5 = cv2.imread(os.path.join(input_path,image_list[4]))
 #               width = int(image_1.shape[1])
 #               height = int(image_1.shape[0] * scale_percent)
 #               dim = (width, height)
 #               image_1_resized = cv2.resize(image_1, dim, interpolation = cv2.INTER_AREA)
 #               image_2_resized = cv2.resize(image_2, dim, interpolation = cv2.INTER_AREA)
 #               image_3_resized = cv2.resize(image_3, dim, interpolation = cv2.INTER_AREA)
 #              image_4_resized = cv2.resize(image_4, dim, interpolation = cv2.INTER_AREA)
 #               image_5_resized = cv2.resize(image_5, dim, interpolation = cv2.INTER_AREA)
 #               v_img = cv2.vconcat([image_1_resized, image_2_resized, image_3_resized, image_4_resized, image_5_resized])
 #               output_image_name = 'image_vert_' + str(index) + '.png'
#
 #               output_image_path = os.path.join(output_path, output_image_name)
 #               cv2.imwrite(output_image_path, v_img)
 #               five = {'image_name' : output_image_name, 'image_list' : image_list}
 #               five_array.append(five)
 #               index +=1

#dictionary = {"two" : two_array, "three" : three_array, "four" : four_array, "five" : five_array}
#dictionary = {"two" : two_array, "three" : three_array, "four" : four_array}
dictionary = {"two" : two_array, "three" : three_array}
with open(dict_path + '/dictionary.json', "w") as outfile: 
    json.dump(dictionary,outfile) 


# Two = [{"image_name" : '', "image_list" : []}]
# {
#     "two" :[
#         {
#         "image_name" : imagename.jpg, "image_list" : [image_list]
#     },{
#         "image_name" : [image_list]
#     }
#     ]s
#     "three" :[{
#         "image_name" : [image_list]
#     }
#     ]
# }










# {
#     "Two" :[
#         {
#             "image1" : "image1.png"
#             "image2" : "image2.png"
#         },
#     {
#         "image1" : "image2.png"
#         "image2" : "image3.png"
#     }
#     ],
#     "Three" : [
#         {
#             "image1" : "image1.png"
#             "image2" : "image2.png"
#             "image3" : "image3.png"
#         },
#         {
#             "image1" : "image2.png"
#             "image2" : "image3.png"
#             "image3" : "image4.png"
#         }
#     ],
#     "Four" :[
#         {
#             "image1" : "image1.png"
#             "image2" : "image2.png"
#             "image3" : "image3.png"
#             "image4" : "image4.png"
#         }
#     ]
# }

