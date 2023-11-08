import os
import xml.etree.ElementTree as ET


# 定义一个函数来遍历并打印标签和属性
def print_tags_and_attribs(element, filter, tire):
    iter_elem = element.iter()
    cur_elem = None
    for elem in iter_elem:
        if elem.tag in filter:
            print(f"标签名称: {elem.tag}")
            # 打印标签的属性
            for attrib, value in elem.attrib.items():
                print(f"属性: {attrib}, 值: {value}")
            if elem.tag == tire + 'bookmarkStart':
                for next_elem in iter_elem:
                    if next_elem is not None and next_elem.tag == tire + 'rFonts':
                        for attrib, value in next_elem.items():
                            print(f"属性: {attrib}, 值: {value}")
                        next_elem = next(iter_elem, None)
                        if next_elem.tag == tire + 'szCs':
                            for attrib, value in next_elem.items():
                                print(f"属性: {attrib}, 值: {value}")
                        break


if os.path.isfile('C:\\Users\\lay\\Downloads\\document.xml'):
    # 解析XML文件
    tree = ET.parse('C:\\Users\\lay\\Downloads\\document.xml')
    root = tree.getroot()
    #tire表示标签名前缀
    tire = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    filter = [tire + 'bookmarkStart', tire + 'bookmarkEnd']  # , tire + 'lastRenderedPageBreak'
    filter1 = [tire + 'rFonts']
    document_element = root.find('.//w:document',
                                 namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
                                             'xml': 'http://www.w3.org/XML/1998/namespace'})
    if document_element is not None:
        print_tags_and_attribs(document_element, filter, tire)
    # 打印文件的绝对路径
    print('文件存在，路径为{}'.format(os.path.abspath('C:\\Users\\lay\\Downloads\\document.xml')))
else:
    print('文件不存在')
