class BankAccount:
    def __init__(self, balance=0, account_owner="", account_type=""):
        """
        Initializes the BankAccount with the specified attributes.

        Args:
            balance (float): The initial account balance (default is 0).
            account_owner (str): The name of the account owner (default is an empty string).
            account_type (str): The type of the account (e.g., savings, checking, etc., default is an empty string).
        """
        self.__balance = balance
        self.__account_owner = account_owner
        self.__account_type = account_type

    # Mutator methods
    def set_balance(self, new_balance):
        """
        Sets the value of the "__balance" attribute.

        Args:
            new_balance (float): The new account balance.
        """
        self.__balance = new_balance

    def set_account_owner(self, new_owner):
        """
        Sets the value of the "__account_owner" attribute.

        Args:
            new_owner (str): The new account owner's name.
        """
        self.__account_owner = new_owner

    def set_account_type(self, new_type):
        """
        Sets the value of the "__account_type" attribute.

        Args:
            new_type (str): The new account type.
        """
        self.__account_type = new_type

    # Accessor methods
    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
            float: The account balance.
        """
        return self.__balance

    def get_account_owner(self):
        """
        Returns the account owner's name.

        Returns:
            str: The account owner's name.
        """
        return self.__account_owner

    def get_account_type(self):
        """
        Returns the account type.

        Returns:
            str: The account type.
        """
        return self.__account_type

# Example usage
if __name__ == "__main__":
    my_account = BankAccount(balance=1000, account_owner="John Doe", account_type="Savings")
    print(f"Account owner: {my_account.get_account_owner()}")
    print(f"Account type: {my_account.get_account_type()}")
    print(f"Current balance: ${my_account.get_balance():.2f}")


    
   
    






