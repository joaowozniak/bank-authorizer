import argparse, os, json
from utils.util import getOutputLine
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


def processFile(
    in_file: str, out_file: str = "../outfile.txt", save_to_file: bool = True
):

    account_list = []
    trans_list = []

    account_proc = AccountProcess(account_list)
    trans_proc = TransactionProcess(trans_list)

    process = Processing(account_proc, trans_proc)

    lines = []
    with open(in_file) as f:
        lines = f.readlines()
    f.close()

    out = []

    for line in lines:
        line_json = json.loads(line)
        accounts, violations = process.processLine(line_json)
        out_line = getOutputLine(accounts, violations)
        out.append(out_line)

    if save_to_file:
        output_file = open(out_file, "w")

        for l in out:
            json.dump(l, output_file)
            output_file.write("\n")

        print(f"Saved to {out_file}!")
        output_file.close()

    return out


def main():

    print("Starting up ...")

    args = _parse_args()

    if not os.path.exists(args.filepath):
        print("File path not valid.")

    else:
        _ = processFile(args.filepath)


if __name__ == "__main__":
    main()
