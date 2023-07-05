import subprocess
from Modules.Display import show
from Modules.Phase2 import *
import Modules.Phase1
import sys


def display_phase_two_menu():
    main_menu = {
        "create table": create_table,
        "add chain": add_chain,
        "list of chains": chain_ls,
        "list of tables": table_ls,
        "Create access-restricting roles": Create_access_restricting,
        "flush nftabel": flush_nft,
        "back": "Exit"
    }
    show(main_menu, "Phase 1 menu")
