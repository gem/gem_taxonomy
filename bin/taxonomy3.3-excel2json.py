#!/usr/bin/env python3
import sys
import json
import pandas

MAX_ID_LEN = 7

DELTA = 100


def usage(argv, exit_code):
    print("""
USAGE:
    %s XSLX_FILE
    """ % argv[0])
    sys.exit(exit_code)


# indexes for Summary sheet
ATTRIBUTE_NAME_IDX = 0
ATTRIBUTE_TITL_IDX = 1
ATTRIBUTE_REFE_IDX = 2
ATTRIBUTE_ATOMSGROUP_TITL_IDX = 3


# indexes for attributes sheets
ATOMSGROUP_NAME_IDX = 0
ATOMSGROUP_TITL_IDX = 1
ATOM_NAME_IDX = 2
ATOM_TITL_IDX = 3
ATOM_DESC_IDX = 4
ATOM_DEPS_IDX = 5
ATOM_DEPS_EXA = 6
ATOM_PROG_IDX = 7
ATOM_TYPE_IDX = 8
ATOM_ARGS_IDX = 9
ATOM_PARAMS_IDX = 10

#
#  MAIN
#
if __name__ == '__main__':
    tax = {
        'Attribute': [],
        'AtomsGroup': [],
        'Atom': [],
        'Param': {},
        'AtomsDeps': [],
        'AtomType': None,
    }

    #
    #   Taxonomy v3.3
    #
    infile_name = sys.argv[1]

    #
    #  Gather sheet_names starting from 'summary' sheet
    #
    xlsx = pandas.read_excel(
        infile_name, dtype=str,
        header=None, na_filter=None, sheet_name=[0])

    # Check summary page
    rows = xlsx[0].values
    sheet_names = ['summary']
    ref_found = False
    taxmod_atom_type = {}
    taxmod_atom_deps = {}

    attribute_prog = 0
    for row in rows:
        if not ref_found:
            if row[ATTRIBUTE_REFE_IDX].lower() == 'reference':
                ref_found = True
            continue

        if row[ATTRIBUTE_ATOMSGROUP_TITL_IDX] == '':
            break

        if row[ATTRIBUTE_NAME_IDX] != '':
            attribute_name = row[ATTRIBUTE_NAME_IDX]
            attribute_titl = row[ATTRIBUTE_TITL_IDX]

            tax['Attribute'].append({
                "prog": str(int(float(attribute_prog))),
                "name": attribute_name,
                "title": attribute_titl,
                })

            sheet_names.append(attribute_name)

            attribute_prog += 100

    xlsx = pandas.read_excel(
        infile_name, dtype=str,
        header=None, na_filter=None, sheet_name=sheet_names)

    atomsgroup_name = ''
    atomsgroup_titl = ''
    atomsgroup_prog = -100
    atom_prog = 0
    for sheet_name in sheet_names[1:]:
        attribute_name = sheet_name
        sheet = xlsx[sheet_name]
        rows = sheet.values

        atomsgroup_prog = -100

        name_found = False
        for row in rows:
            if not name_found:
                if row[ATOM_TITL_IDX].lower() == 'atom title':
                    name_found = True
                continue
            if row[ATOM_TITL_IDX] == '':
                break

            atomsgroup_name = (atomsgroup_name
                               if row[ATOMSGROUP_NAME_IDX] == ''
                               else row[ATOMSGROUP_NAME_IDX])
            atomsgroup_titl = (atomsgroup_titl
                               if row[ATOMSGROUP_TITL_IDX] == ''
                               else row[ATOMSGROUP_TITL_IDX])
            if row[ATOMSGROUP_NAME_IDX] != '':
                atom_prog = 0
                atomsgroup_prog += 100
                tax['AtomsGroup'].append({
                    "prog": str(int(float(atomsgroup_prog))),
                    "name": atomsgroup_name,
                    "title": atomsgroup_titl,
                    "group": attribute_name
                })

            atom_name = row[ATOM_NAME_IDX]
            atom_titl = row[ATOM_TITL_IDX]
            atom_desc = row[ATOM_DESC_IDX]
            atom_deps = row[ATOM_DEPS_IDX]
            atom_prog = row[ATOM_PROG_IDX]
            atom_type = row[ATOM_TYPE_IDX]
            atom_args = row[ATOM_ARGS_IDX]
            atom_parms = row[ATOM_PARAMS_IDX]

            if ':' in atom_name:
                param_atom = atom_name.split(':')[0]
                param_name = ':'.join(atom_name.split(':')[1:])
                param_titl = atom_titl
                param_desc = atom_desc
                param_prog = atom_prog

                if param_atom not in tax['Param']:
                    tax['Param'][param_atom] = []
                tax['Param'][param_atom].append(
                    {
                        'atom': param_atom,
                        'name': param_name,
                        'title': param_titl,
                        'desc': param_desc,
                        'prog': str(int(float(param_prog))),
                    }
                )
            else:
                tax['Atom'].append({
                    "prog": str(int(float(atom_prog))),
                    "name": atom_name,
                    "title": atom_titl,
                    "desc": atom_desc,
                    "group": atomsgroup_name,
                    "attr": attribute_name,
                    "type": atom_type,
                    "args": atom_args,
                    "params": atom_parms,
                })

            if atom_type:
                taxmod_atom_type[atom_name] = atom_type

            if atom_deps:
                taxmod_atom_deps[atom_name] = (
                    [x.strip() for x in atom_deps.split(',')])

    tax['AtomType'] = taxmod_atom_type
    tax['AtomsDeps'] = taxmod_atom_deps

    new_dict = {}
    for k in ['Attribute', 'AtomsGroup', 'Atom']:
        if 'name' in tax[k][0]:
            new_dict[k + 'Dict'] = {x['name']: x for x in tax[k]}
    tax.update(new_dict)

    with open('out/taxonomy3.3_standard.json', 'w') as f:
        json.dump(tax, f, indent=4)
