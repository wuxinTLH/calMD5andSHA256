import hashlib
import sys


def main(path: str):
    try:
        file_name = path
        print(path + '的MD5:' + cal_md5(file_name) + '\n')
        print(path + '的sha1:' + cal_sha1(file_name) + '\n')
        print(path + '的SHA256:' + cal_sha256(file_name) + '\n')
    except FileNotFoundError:
        print("文件未找到，可能是文件名或位置错误")


def cal_sha256(file_name):
    with open(file_name, "rb") as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        hash_value = sha256obj.hexdigest()
        return hash_value


def cal_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    return file_md5


def cal_sha1(file_name):
    with open(file_name, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        sha1_hash = sha1obj.hexdigest()
        return sha1_hash


if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        main(sys.argv[i])
    while True:
        path = input("请输入相对地址或绝对地址或手动退出：")
        main(path)
