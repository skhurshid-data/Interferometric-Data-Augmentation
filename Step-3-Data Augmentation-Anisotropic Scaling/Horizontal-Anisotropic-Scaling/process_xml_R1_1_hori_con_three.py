import os
import glob
import json
import ntpath
from xml.dom import minidom
import xml.etree.ElementTree as ET


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def readXML(sample_xml_path):
    return ET.parse(sample_xml_path) 

def generate_xml(value, tree, save_path):
    
    root = tree.getroot()

    root.find('filename').text = value[0] + '.png'

    size= ET.SubElement(root,'size')
    width = ET.SubElement(size, 'width')
    height = ET.SubElement(size, 'height')
    depth = ET.SubElement(size, 'depth')

    width.text = str(value[1])
    height.text = str(value[2])
    depth.text = str(3)    
    x_min = value[4]
    y_min = value[5]
    x_max = value[6]
    y_max = value[7]

    obj= ET.SubElement(root,'object')
    name = ET.SubElement(obj, 'name') 
    label=value[3]
    name.text=str(label)

    pose = ET.SubElement(obj, 'pose')
    pose.text='Unspecified'

    truncated = ET.SubElement(obj, 'truncated')
    truncated.text='0'

    difficult = ET.SubElement(obj, 'difficult') 
    difficult.text='0'

    bndbox=ET.SubElement(obj,'bndbox')
    
    xmin=ET.SubElement(bndbox,'xmin')
    xmin.text=str(x_min)

    ymin=ET.SubElement(bndbox,'ymin')
    ymin.text=str(y_min)

    xmax=ET.SubElement(bndbox,'xmax')
    xmax.text=str(x_max)

    ymax=ET.SubElement(bndbox,'ymax')
    ymax.text=str(y_max)
    filename = value[0] + '.xml'
    tree.write(os.path.join(save_path, filename))

def process():
    value = [output_file_name.replace('.xml',''),
                2378,
                1210,
                label,
                int(xmin),     #xmin
                int(ymin),     #ymin
                int(xmax),     #xmax
                int(ymax)      #ymax
                ]
    if os.path.isfile(os.path.join(output_xml_path, output_file_name)):
        output_xml_file = os.path.join(output_xml_path, output_file_name)
        sample_xml_tree = readXML(output_xml_file)
        generate_xml(value, sample_xml_tree, output_xml_path)
    else:
        sample_xml_tree = readXML(sample_xml_path)
        generate_xml(value, sample_xml_tree, output_xml_path)

json_file = "/home/reserved/Sumair/concatenation/hori_con/dictionary.json"
images_path = "/home/reserved/Sumair/concatenation/hori_con/hori_Input_images"
input_xml_path = "/home/reserved/Sumair/concatenation/hori_con/hori_Input_xml"
output_xml_path = "/home/reserved/Sumair/concatenation/hori_con/hori_output_xml"
sample_xml_path = "/home/reserved/Sumair/concatenation/sample.xml"
image_width = 2378
#image_height = 1210

data = json.load(open(json_file))
two = data['two']
three = data['three']
#four = data['four']
#five = data['five']

for iteration in two:
    output_file_name = iteration['image_name'].replace('.png','.xml')
    images = iteration['image_list']
    for index, image in enumerate(images):
        xml_file = os.path.join(input_xml_path,image.replace('.png','.xml'))
        doc = minidom.parse(xml_file)
        objs = doc.getElementsByTagName("object")
        if index == 0:
            for obj in objs:
                label = obj.getElementsByTagName("name")[0].firstChild.data
                bndbox = obj.getElementsByTagName("bndbox")[0]
                ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                xmin = int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/2
                ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                xmax = int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/2
                process()
                
        elif index == 1:
            for obj in objs:
                label = obj.getElementsByTagName("name")[0].firstChild.data
                bndbox = obj.getElementsByTagName("bndbox")[0]
                ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/2) + 1189
                ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/2) + 1189
                process()
###############################################################################################
for iteration in three:
    output_file_name = iteration['image_name'].replace('.png','.xml')
    images = iteration['image_list']
    for index, image in enumerate(images):
        xml_file = os.path.join(input_xml_path,image.replace('.png','.xml'))
        doc = minidom.parse(xml_file)
        objs = doc.getElementsByTagName("object")
        if index == 0:
            for obj in objs:
                label = obj.getElementsByTagName("name")[0].firstChild.data
                bndbox = obj.getElementsByTagName("bndbox")[0]
                ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                xmin = int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/3
                ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                xmax = int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/3
                process()
                
        elif index == 1:
            for obj in objs:
                label = obj.getElementsByTagName("name")[0].firstChild.data
                bndbox = obj.getElementsByTagName("bndbox")[0]
                ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/3) + 792.67	#792.67
                ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/3) + 792.67
                process()

        elif index == 2:
            for obj in objs:
                label = obj.getElementsByTagName("name")[0].firstChild.data
                bndbox = obj.getElementsByTagName("bndbox")[0]
                ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/3) + 792.67 + 792.67
                ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/3) + 792.67 + 792.67
                process()
#############################################################################################################
# for iteration in four:
    # output_file_name = iteration['image_name'].replace('.png','.xml')
    # images = iteration['image_list']
    # for index, image in enumerate(images):
        # xml_file = os.path.join(input_xml_path,image.replace('.png','.xml'))
        # doc = minidom.parse(xml_file)
        # objs = doc.getElementsByTagName("object")
        # if index == 0:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/4
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/4
                # process()
                
        # elif index == 1:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/4) + 594.5
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/4) + 594.5
                # process()

        # elif index == 2:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/4) + 594.5 + 594.5
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/4) + 594.5 + 594.5
                # process()

        # elif index == 3:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/4) + 594.5 + 594.5 + 594.5
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/4) + 594.5 + 594.5 + 594.5
                # process()
###############################################################################################################
# for iteration in five:
    # output_file_name = iteration['image_name'].replace('.png','.xml')
    # images = iteration['image_list']
    # for index, image in enumerate(images):
        # xml_file = os.path.join(input_xml_path,image.replace('.png','.xml'))
        # doc = minidom.parse(xml_file)
        # objs = doc.getElementsByTagName("object")
        # if index == 0:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/5
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/5
                # process()
                
        # elif index == 1:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/5) + 475.6	#475.6
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/5) + 475.6
                # process()

        # elif index == 2:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/5) + 475.6 + 475.6
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/5) + 475.6 + 475.6
                # process()

        # elif index == 3:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/5) + 475.6 + 475.6 + 475.6
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/5) + 475.6 + 475.6 + 475.6
                # process()
                
        # elif index == 4:
            # for obj in objs:
                # label = obj.getElementsByTagName("name")[0].firstChild.data
                # bndbox = obj.getElementsByTagName("bndbox")[0]
                # ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data
                # xmin = (int(bndbox.getElementsByTagName("xmin")[0].firstChild.data)/5) + 475.6 + 475.6 + 475.6 + 475.6
                # ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data
                # xmax = (int(bndbox.getElementsByTagName("xmax")[0].firstChild.data)/5) + 475.6 + 475.6 + 475.6 + 475.6
                # process()

