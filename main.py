import argparse
import getpass
import sys

from cli.PasswordVerifier import PasswordVerifier


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify your passwords"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Subparser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new password")
    add_parser.add_argument("site", help="The name of the site")
    add_parser.add_argument("username", help="The username for the account")
    add_parser.add_argument("--password", help="The password for the account(not recommended, omit to enter securely)")

    # Subparser for the 'verify' command
    verify_parser = subparsers.add_parser("verify", help="Verify a password")
    verify_parser.add_argument("site", help="The name of the site")
    verify_parser.add_argument("username", help="The username for the account")
    verify_parser.add_argument("--password", help="The password to verify(not recommended, omit to enter securely)")

    # Subparser for the 'list' command
    subparsers.add_parser("list", help="List all stored accounts")

    # Subparser for the 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Delete an account")
    delete_parser.add_argument("site", help="The name of the site")
    delete_parser.add_argument("username", help="The username for the account")

    args = parser.parse_args()
    password_verifier = PasswordVerifier()

    if args.command == "add":
        password = args.password if args.password else getpass.getpass("Enter password: ")
        password_verifier.add_account(args.site, args.username, password)

    elif args.command == "verify":
        password = args.password if args.password else getpass.getpass("Enter password: ")
        password_verifier.verify_password(args.site, args.username, password)

    elif args.command == "list":
        password_verifier.list_accounts()

    elif args.command == "delete":
        password_verifier.delete_account(args.site, args.username)

    else:
        parser.print_help()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)