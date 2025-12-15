while True:
    print("\n1.Length")
    print("2.Concatenation")
    print("3.Comparison")
    print("4.Reverse")
    print("5.Substring Check")
    print("6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        s = input("Enter string: ")
        print("Length:", len(s))

    elif ch == 2:
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        print("Concatenated String:", s1 + s2)

    elif ch == 3:
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        if s1 == s2:
            print("Strings are equal")
        else:
            print("Strings are not equal")

    elif ch == 4:
        s = input("Enter string: ")
        print("Reversed String:", s[::-1])

    elif ch == 5:
        s = input("Enter main string: ")
        sub = input("Enter substring: ")
        if sub in s:
            print("Substring found")
        else:
            print("Substring not found")

    elif ch == 6:
        break

    else:
        print("Invalid choice")
