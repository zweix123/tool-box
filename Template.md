+ 得到`root`下的所有以某个后缀名的所有文件：

  ```python
  def get_file_list(root, extension):
      return [
          os.path.join(pre, file_name)
          # os.walk(root) 会遍历root下的所有目录和文件, 返回的是迭代器, 每次迭代返回当前迭代到的路径位置, 当前路径下的目录列表, 当前路径下的文件列表
          for pre, dirs, files in os.walk(root)
          for file_name in files
          if str(file_name).endswith("." + extension)
      ]
  ```

+ 检测文件编码类型：

  ```python
  import chardet
  with open(file_name, "rb") as f:
      res = chardet.detect(f.read())
  res
  # {'encoding': '...', 'confidence': 数字}  # 编码和概率
  ```

  
