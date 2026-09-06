# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GrantTracker
import argparse

def main():
    parser = argparse.ArgumentParser(description="GrantTracker CLI")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a new grant")
    p_add.add_argument("--name", required=True, help="Grant name")
    p_add.add_argument("--deadline", help="Deadline (YYYY-MM-DD)")
    p_add.add_argument("--budget", type=float, help="Budget")

    p_list = sub.add_parser("list", help="List all grants")

    p_status = sub.add_parser("status", help="Show grant status")
    p_status.add_argument("grant_id", help="Grant ID")

    args = parser.parse_args()

    if args.command == "add":
        print(f"Grant '{args.name}' added (deadline: {args.deadline}, budget: {args.budget})")
    elif args.command == "list":
        print("All grants:")
    elif args.command == "status":
        print(f"Status of grant {args.grant_id}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
