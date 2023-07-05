#!/bin/bash

# Check if the table name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Error: Table name not provided."
    exit 1
fi

table_name=$1

# Check if the table already exists
if nft list tables | grep -q -w "$table_name"; then
    echo "Table '$table_name' already exists."
    exit 0
fi

# Create the table
nft create table $table_name

# Check the exit status of the previous command
if [ $? -eq 0 ]; then
    echo "Table '$table_name' created successfully."
else
    echo "Failed to create table '$table_name'."
fi
