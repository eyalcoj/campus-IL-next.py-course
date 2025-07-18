from typing import TextIO


def read_file(file_name):
    print("__CONTENT_START__")
    f = TextIO()
    try:
        f = open(file_name)
    except:
        print("__NO_SUCH_FILE__")
    else:
        print(f.read())
    finally:
        f.close()
    print("__CONTENT_END__")


def main():
    read_file(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\name_length.txt")
    # read_file(r"not a link")


if __name__ == "__main__":
    main()
