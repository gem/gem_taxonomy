#!/bin/bash


if [ $# -ne 1 ]; then
    cat <<EOF

CONFIG:
    edit .git/config file and add the following rows:

[diff "xlsx"]
        binary = true
        textconv = ./bin/xlsx2text.sh

    than add the file $HOME/.config/git/attributes or append the
    following line to the already existing one:

*.xlsx diff=xlsx

SYNOPSIS
    $0 EXCEL_FILENAME

EOF
    exit 1
fi

python3 -c "
import sys
import pandas as pd
from io import StringIO

sheets_dict = pd.read_excel(sys.argv[1], sheet_name=None)
ExcelSheet = pd.DataFrame()
for name, sheet in sheets_dict.items():
    print('SHEET NAME: %s' % name)
    output = StringIO()
    sheet.to_csv (output, ',', index = None, header=True)

    output.seek(0)
    print(output.read())" $1
