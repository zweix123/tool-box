import os
import time
from PyPDF2 import PdfFileReader, PdfFileWriter


def get_file_list(root, extension):
    return [
        os.path.join(pre, file_name)
        # os.walk(root) 会遍历root下的所有目录和文件, 返回的是迭代器, 每次迭代返回当前迭代到的路径位置, 当前路径下的目录列表, 当前路径下的文件列表
        for pre, dirs, files in os.walk(root)
        for file_name in files
        if str(file_name).endswith("." + extension)
    ]


def merge_pdf(path=os.getcwd(), result_name="meged pdf.pdf"):
    """
    将path在文件系统的子树中的所有.pdf文件都merge
    会检测是否有名为meged pdf.pdf文件, 如果有会要求用户处理
    """

    start = time.time()

    file_list = get_file_list(path, "pdf")

    if file_list.count(os.path.join(path, "meged pdf.pdf")):
        print("There is file named \"meged pdf.pdf\" that needs to be solved!")
        return

    result = PdfFileWriter()

    sum_pages = 0
    for file in file_list:
        now = PdfFileReader(open(file, "rb"))
        cur_pages = now.getNumPages()
        sum_pages += cur_pages
        for i in range(cur_pages):
            result.addPage(now.getPage(i))

        print('file : {}'.format(file))
        print('page : {}'.format(cur_pages))

    print("merged file name : {}".format(
        os.path.join(os.getcwd(), result_name)))
    print("merged file page : {}".format(sum_pages))

    with open(os.path.join(os.getcwd(), result_name), "wb") as f:
        result.write(f)
        print("finish! ", end="")

    end = time.time()
    print('Total time is {} second'.format(end - start))


if __name__ == "__main__":
    merge_pdf(os.getcwd())
