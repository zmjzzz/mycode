
def run():
    raise Exception('error_file_not_found')

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        if str(e) == 'error_file_not_found':
            print("抓到错误了")
        else:
            print("没有判别到",e)
    else:
        print("尽然没错误")
    finally:
        print("最后执行")