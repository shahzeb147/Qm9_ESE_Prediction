"""
Qm9 dataset:
    - "mol_id" - Molecule ID (gdb9 index) mapping to the .sdf file
    - "A" - Rotational constant (unit: GHz)
    - "B" - Rotational constant (unit: GHz)
    - "C" - Rotational constant (unit: GHz)
    - "mu" - Dipole moment (unit: D)
    - "alpha" - Isotropic polarizability (unit: Bohr^3)
    - "homo" - Highest occupied molecular orbital energy (unit: Hartree)
    - "lumo" - Lowest unoccupied molecular orbital energy (unit: Hartree)
    - "gap" - Gap between HOMO and LUMO (unit: Hartree)
    - "r2" - Electronic spatial extent (unit: Bohr^2)
    - "zpve" - Zero point vibrational energy (unit: Hartree)
    - "u0" - Internal energy at 0K (unit: Hartree)
    - "u298" - Internal energy at 298.15K (unit: Hartree)
    - "h298" - Enthalpy at 298.15K (unit: Hartree)
    - "g298" - Free energy at 298.15K (unit: Hartree)
    - "cv" - Heat capavity at 298.15K (unit: cal/(mol*K))
    - "u0_atom" - Atomization energy at 0K (unit: kcal/mol)
    - "u298_atom" - Atomization energy at 298.15K (unit: kcal/mol)
    - "h298_atom" - Atomization enthalpy at 298.15K (unit: kcal/mol)
    - "g298_atom" - Atomization free energy at 298.15K (unit: kcal/mol)

information source: https://github.com/deepchem/deepchem/blob/master/deepchem/molnet/load_function/qm9_datasets.py
data source: https://figshare.com/collections/Quantum_chemistry_structures_and_properties_of_134_kilo_molecules/978904
More information :https://www.nature.com/articles/sdata201422#Tab3
"""


import os
import numpy as np

def extract_atom_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        atom_data = []
        num_atoms = int(lines[0].strip())
        for line in lines[2:2+num_atoms]:
            parts = line.strip().split()
            if len(parts) >= 4:  # Ensure there are at least 4 parts
                element = parts[0]
                x, y, z = map(float, parts[1:4])
                atom_data.append((element, np.array([x, y, z], dtype=np.float32)))
            else:
                print(f"Skipping malformed line in file {file_path}: {line.strip()}")
        return atom_data
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return []

def process_all_files_to_list(directory):
    all_molecules = []
    filenames = sorted(os.listdir(directory))
    for filename in filenames:
        if filename.endswith(".xyz"):
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")
            atom_data = extract_atom_data(file_path)
            if atom_data:
                all_molecules.append(atom_data)
    return all_molecules

# Directory containing the .xyz files
directory_path = '/Users/muhammadshahzebali/Desktop/research papers/datasets/qm9 data'

# Process all files and extract data into structured format
all_molecules = process_all_files_to_list(directory_path)

# Example: Print the number of molecules processed and the first molecule's data
print(f"Total molecules processed: {len(all_molecules)}")
print(all_molecules[1])
