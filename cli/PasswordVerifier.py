import json
import os
from typing import List, Optional
from colorama import Fore, Style
from tabulate import tabulate
from argon2 import PasswordHasher

AccountInfo = dict[str, str]
AccountStore = dict[str, AccountInfo]

def _hash_password(password: str) -> str:

    """
    Create a secure hash of the password

    Args:
        password (str): The password to hash.

    Returns:
        str: Hexadecimal digest of the password hash.
    """

    ph = PasswordHasher()
    return ph.hash(password)

class PasswordVerifier:

    def __init__(self, storage_file: Optional[str] = None) -> None:

        """
        Initializes the verifier with a storage file.

        Args:
            storage_file (Optional[str]): Path to the storage file. If not provided, a default location is used.
        """

        if storage_file is None:
            home_directory = os.path.expanduser("~")
            self.storage_directory = os.path.join(home_directory, ".password_verifier")

            if not os.path.exists(self.storage_directory):
                os.makedirs(self.storage_directory)
            
            self.storage_file = os.path.join(self.storage_directory, "passwords.json")
        
        else:
            self.storage_file = storage_file

        self.accounts: AccountStore = self._load_accounts()

    def _load_accounts(self) -> AccountStore:

        """
        Loads accounts from the storage file or returns an empty dictionary if file doesn't exist.

        Returns:
            AccountStore: Dictionary of accounts.
        """
        
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"{Fore.RED}Error: Storage file is corrupted.{Style.RESET_ALL}")
                return {}
        return {}
    
    def _save_accounts(self) -> None:

        """
        Saves the current accounts to the storage file.
        """
        
        with open(self.storage_file, 'w') as file:
            json.dump(self.accounts, file, indent=4)

    def add_account(self, site: str, username: str, password: str) -> None:

        """
        Adds a new account to the storage.

        Args:
            site (str): The name of the site.
            username (str): The username for the account.
            password (str): The password for the account.
        """
        
        if site in self.accounts:
            print(f"{Fore.YELLOW}Account already exists. Updating password...{Style.RESET_ALL}")

        key = f"{site}:{username}"
        
        self.accounts[key] = {
            "site": site,
            "username": username,
            "password": _hash_password(password)
        }

        self._save_accounts()
        print(f"{Fore.GREEN}Account for {site} ({username}) added successfully.{Style.RESET_ALL}")

    def verify_password(self, site: str, username: str, password: str) -> bool:
        """
        Verifies if the provided password matches the stored password for the given account.

        Args:
            site (str): The name of the site.
            username (str): The username for the account.
            password (str): The password to verify.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        
        key = f"{site}:{username}"
        
        if key not in self.accounts:
            print(f"{Fore.RED}Account not found.{Style.RESET_ALL}")
            return False
        
        stored_password_hash = self.accounts[key]["password"]
        
        if stored_password_hash == _hash_password(password):
            print(f"{Fore.GREEN}Password is correct! This is the correct password for {site}.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Incorrect password.{Style.RESET_ALL}")
            return False
        
    def list_accounts(self) -> None:

        """
        Lists all stored accounts.
        """
        
        if not self.accounts:
            print(f"{Fore.YELLOW}No accounts stored.{Style.RESET_ALL}")
            return
        
        table_data: List[List[str]] = []
        
        for key, account in self.accounts.items():
            table_data.append([account["site"], account["username"]])

        print(tabulate(table_data, headers=["Site", "Username"], tablefmt="grid"))

    def delete_account(self, site: str, username: str) -> None:
        """
        Deletes an account from the storage.

        Args:
            site (str): The name of the site.
            username (str): The username for the account.
        """
        
        key = f"{site}:{username}"
        
        if key not in self.accounts:
            print(f"{Fore.RED}Account not found.{Style.RESET_ALL}")
            return
        
        del self.accounts[key]
        self._save_accounts()
        print(f"{Fore.GREEN}Account for {site} ({username}) deleted successfully.{Style.RESET_ALL}")