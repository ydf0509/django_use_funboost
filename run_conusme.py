
from index.func import create_report

if __name__ == '__main__':
    # create_report.consume()  # 当前进程内启动，可以这样，也可以下面使用多进程启动。
    create_report.multi_process_consume(4)  #

