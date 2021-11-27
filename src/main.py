import argparse, sys, os, json
from utils.constant import Constant
from utils.util import getOutputLine
from models.account import Account
from controllers.processing import Processing
from controllers.accounts import AccountProcess
from controllers.transactions import TransactionProcess


def _parse_args():
    parser = argparse.ArgumentParser(description="Nubank Authorizer")
    parser.add_argument(
        "-f", "--filepath", required=True, help="Path to the input file"
    )
    args = parser.parse_args()

    return args


def processFile(in_file: str):

    account_list = []
    trans_list = []

    account_proc = AccountProcess(account_list)
    trans_proc = TransactionProcess(trans_list)

    process = Processing(account_proc, trans_proc)

    lines = []
    with open(in_file) as f:
        lines = f.readlines()
    f.close()

    outfile_name = "authorizer_output.txt"
    out_file = open(outfile_name, "w")

    count = 0
    for line in lines:
        line_json = json.loads(line)
        accounts, violations = process.processLine(line_json)

        out_line = getOutputLine(accounts, violations)
        json.dump(out_line, out_file)
        out_file.write("\n")

    print(f"Saved to {outfile_name}!")
    out_file.close()


def main():

    print("Starting up ...")

    args = _parse_args()

    if not os.path.exists(args.filepath):
        print("File path not valid.")

    else:
        processFile(args.filepath)


if __name__ == "__main__":
    main()
