def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    result = []

    for i in array:
        if i not in result:
            result.append(i)

    print(result)

if __name__ == "__main__":
    main()
