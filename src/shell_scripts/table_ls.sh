#!/bin/bash
nft list tables | awk '/table / {print $2}'
