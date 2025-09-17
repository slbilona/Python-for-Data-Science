from load_image import ft_load


def main():
    try:
        print(ft_load("images.jpg"))
    except Exception as error:
        print("error :", error)


if __name__ == "__main__":
    main()
