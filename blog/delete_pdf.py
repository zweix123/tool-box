import os


def get_file_list(root, extension):
    return [
        os.path.join(pre, file_name)
        # os.walk(root) 会遍历root下的所有目录和文件, 返回的是迭代器, 每次迭代返回当前迭代到的路径位置, 当前路径下的目录列表, 当前路径下的文件列表
        for pre, dirs, files in os.walk(root)
        for file_name in files
        if str(file_name).endswith("." + extension)
    ]


if __name__ == "__main__":
    for f in get_file_list(os.getcwd(), "pdf"):
        os.system("del \"{}\"".format(f))
        print("成功删除\"{}\"".format(f))
