# Nubank Authorizer

## Introduction

Bank Account and Transaction Authorizer: An application that authorizes transactions for a specific account following a set of predefined rules.

## Description

The program receives json lines as input in the stdin and provides a json line output for each of the inputs.

### Authorizer Operations

Assuming all monetary values are positive integers using a currency without cents and the transactions will arrive at the Authorizer in chronological order:

#### 1. Account creation

_Input:_ Creates the account with the attributes available-limit and active-card.
_Output:_ The created account's current state with all business logic violations. If in the operation processing does not happen any violation, the field violations returns an empty vector [].

_Business rules:_ Once created, the account can't be updated or recreated. If the application receives another operation of account creation, it returns the following violation: account-already-initialized.

#### 2. Transaction authorization in the account

_Input:_ Tries to authorize a transaction for a particular merchant, amount and time given the created account's state and last authorized transactions.
_Output:_ The account's current state with any business logic violations. If in the operation processing does not happen any violation, the field violations returns an empty vector [].

_Business rules:_

- No transaction should be accepted without a properly initialized account: account-not-initialized;
- No transaction should be accepted when the card is not active: card-not-active;
- The transaction amount should not exceed the available limit: insufficient-limit;
- There should not be more than 3 transactions on a 2-minute interval: high-frequency-small-interval;
- There should not be more than 1 similar transactions (same amount and merchant ) in a 2 minutes interval: doubled-transaction

## Run

Navigate to src directory and execute:

```
$ python main.py -f ["filename.txt"]
```

Filename.txt should contain the account and transactions information.

## Tests

Navigate to test directory and execute:

```
pytest tests.py
```
