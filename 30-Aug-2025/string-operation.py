def string_operations():
    print("=== STRING OPERATIONS ===\n")

    # 1. String Creation
    s1 = "Mango"
    s2 = 'Banana'
    print("s1 =", s1)
    print("s2 =", s2)

    # 2. Concatenation
    concat = s1 + " " + s2
    print("Concatenated:", concat)

    # 3. Repetition
    repeated = s1 * 3
    print("Repeated:", repeated)

    # 4. String Length
    print("Length of s1:", len(s1))

    # 5. Indexing
    print("First char of s1:", s1[0])
    print("Last char of s1:", s1[-1])

    # 6. Slicing
    print("Slice s1[1:4]:", s1[1:4])
    print("Reverse s1:", s1[::-1])

    # 7. Case Conversion
    print("Lowercase:", s1.lower())
    print("Uppercase:", s1.upper())
    print("Title:", concat.title())
    print("Capitalize:", s1.capitalize())
    print("Swapcase:", s1.swapcase())

    # 8. Searching
    print("Index of 'l' in s1:", s1.find('l'))
    print("Last index of 'l':", s1.rfind('l'))

    # 9. Replacing
    print("Replace 'l' with 'x':", s1.replace('l', 'x'))

    # 10. Checking String Types
    test_str = "Hello123"
    print("Is alpha:", test_str.isalpha())
    print("Is digit:", test_str.isdigit())
    print("Is alnum:", test_str.isalnum())
    print("Is lowercase:", s1.islower())
    print("Is uppercase:", s1.isupper())

    # 11. Strip Whitespace
    spaced = "   Hello World   "
    print("Original with spaces:", repr(spaced))
    print("Strip:", repr(spaced.strip()))
    print("LStrip:", repr(spaced.lstrip()))
    print("RStrip:", repr(spaced.rstrip()))

    # 12. Splitting and Joining
    csv = "apple,banana,orange"
    fruits = csv.split(",")
    print("Split CSV:", fruits)
    joined = " | ".join(fruits)
    print("Joined with '|':", joined)

    # 13. Formatting
    name = "Nikku"
    age = 30
    print("Formatted (f-string):", f"My name is {name} and I am {age} years old.")
    print("Formatted (.format):", "{} is {} years old.".format(name, age))

    # 14. Escape Characters
    print("New Line:\nSecond Line")
    print("Tab\tSeparated")
    print("Backslash: \\")

    print("\n=== END OF DEMO ===")


# Run the program
string_operations()
