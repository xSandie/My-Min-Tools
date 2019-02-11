"""
作用:爬取imooc网相应课程目录，在本地生成相应目录结构，方便不同章节的代码编写。
"""
from imoocCodingGen.dirMarker import gen_dir_list, make_dir
from imoocCodingGen.contentsSpider import get_web, get_contents_title

if __name__ == '__main__':
    """
    使用方法如下
    """
    course_url = 'https://coding.imooc.com/class/chapter/213.html#Anchor'
    relative_location = '../../'
    html = get_web(course_url)
    title_list = get_contents_title(html, '.chapter-bd')
    gen_list = gen_dir_list(title_list,relative_location)
    make_dir(gen_list)


    
    