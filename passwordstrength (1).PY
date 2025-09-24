# ==============================
#  Password Strength Checker


def check_password(pw: str) -> str:
    # length check
    if len(pw) < 8:
        return "Weak: password must be at least 8 chars"

    # digit check
    if not any(c.isdigit() for c in pw):
        return "Weak: password must contain a digit"

    # uppercase check
    if not any(c.isupper() for c in pw):
        return "Weak: password must contain an upper char"

    # lowercase check
    if not any(c.islower() for c in pw):
        return "Weak: password must contain a lower char"

    # special character check
    specials = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    if not any(c in specials for c in pw):
        return "Medium: password must contain a special char"

    # if all conditions passed
    return "Strong: Your password is secure!"

def main():
    print("Welcome to the password strength checker")
    while True:
        pw = input("Enter your password (or type 'exit' to quit): ")
        if pw.lower() == "exit":
            print("Exiting...")
            break
        result = check_password(pw)
        print(result)

if __name__ == "__main__":
    main()
