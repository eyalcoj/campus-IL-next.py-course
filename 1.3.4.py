def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

    # <Add one line of code here>
    print(''.join([chr(ord(x) + 2) if ord(x) in range(ord('a'), ord('z')) else x for x in password]))


if __name__ == "__main__":
    main()
