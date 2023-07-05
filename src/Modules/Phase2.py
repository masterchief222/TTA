import subprocess


def table_ls():
    tables = get_table_list()
    if tables:
        print("List of tables:")
        for table in tables:
            print(table)
    else:
        print("No tables found.")


def get_table_list():
    try:
        output = subprocess.run(
            ["nft", "list", "tables"], capture_output=True, text=True)
        lines = output.stdout.splitlines()
        tables = [line.split()[1]
                  for line in lines if line.startswith("table")]
        return tables
    except subprocess.CalledProcessError as e:
        print(f"Failed to retrieve the list of tables: {e}")
        return []


def chain_ls():
    try:
        output = subprocess.check_output(
            ["nft", "list", "chains"], universal_newlines=True)
        print("List of chains:")
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Failed to list chains: {e}")


def create_table():
    table_name = input("Enter the table name: ")
    script_path = "shell_scripts/createTable.sh"

    try:
        # Execute the shell script with the table name as an argument
        result = subprocess.run(
            ["bash", script_path, table_name], capture_output=True, text=True)

        if result.returncode == 0:
            print("Table '{}' created successfully.".format(table_name))
        else:
            print("Failed to create table '{}'. Error: {}".format(
                table_name, result.stderr))
    except FileNotFoundError:
        print("Script '{}' not found.".format(script_path))
    except Exception as e:
        print("Error executing script: {}".format(str(e)))


def add_chain():
    tables = get_table_list()
    if not tables:
        print("No tables found.")
        return

    table_name = input("Enter the table name: ")
    if table_name not in tables:
        print(f"Table '{table_name}' not found.")
        return

    chain_name = input("Enter the chain name: ")

    try:
        subprocess.run(["sudo", "nft", "add", "chain", table_name, chain_name])
        print(
            f"Chain '{chain_name}' added successfully to table '{table_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add chain: {e}")


def Create_access_restricting():
    pass


def flush_nft():
    try:
        subprocess.run(["sudo", "nft", "flush", "ruleset"])
        print("nftables flushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to flush nftables: {e}")


def flush_table(table: str):
    try:
        subprocess.run(["sudo", "nft", "flush", "table", "ip", table])
        print("nftables flushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to flush nftables: {e}")


# import subprocess


# def table_ls():
#     try:
#         output = subprocess.check_output(
#             ["sudo", "bash", "shell_scripts/table_ls.sh"], universal_newlines=True)
#         tables = output.strip().split('\n')
#         if tables:
#             print("List of tables:")
#             for table in tables:
#                 print(table)
#         else:
#             print("No tables found.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to retrieve the list of tables: {e}")


# def chain_ls():
#     try:
#         output = subprocess.check_output(
#             ["sudo", "bash", "shell_scripts/chain_ls.sh"], universal_newlines=True)
#         print("List of chains:")
#         print(output)
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to list chains: {e}")


# def create_table():
#     table_name = input("Enter the table name: ")
#     try:
#         subprocess.run(
#             ["sudo", "bash", "shell_scripts/create_table.sh", table_name], check=True)
#         print(f"Table '{table_name}' created successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to create table '{table_name}': {e}")


# def add_chain():
#     table_name = input("Enter the table name: ")
#     chain_name = input("Enter the chain name: ")
#     try:
#         subprocess.run(["sudo", "bash", "shell_scripts/add_chain.sh",
#                        table_name, chain_name], check=True)
#         print(
#             f"Chain '{chain_name}' added successfully to table '{table_name}'.")
#     except subprocess.CalledProcessError as e:
#         print(
#             f"Failed to add chain '{chain_name}' to table '{table_name}': {e}")


# def Create_access_restricting():
#     pass


# def flush_nft():
#     try:
#         subprocess.run(
#             ["sudo", "bash", "shell_scripts/flush_nft.sh"], check=True)
#         print("nftables flushed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to flush nftables: {e}")


# def flush_table(table):
#     try:
#         subprocess.run(
#             ["sudo", "bash", "shell_scripts/flush_table.sh", table], check=True)
#         print(f"Table '{table}' flushed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to flush table '{table}': {e}")
