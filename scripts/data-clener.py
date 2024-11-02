import os

def clean_path_file(input_file, output_file):
    paths = set()
    with open(input_file, 'r') as infile:
        for line in infile:
            # Strip space and comment
            path = line.strip()
            if path and not path.startswith("#"):
                paths.add(path)

    # Write cleaned to a file
    with open(output_file, 'w') as outfile:
        for path in sorted(paths):
            outfile.write(path + '\n')


input_file = 'wordlists/directory-list-2.3-medium.txt'
output_file = 'wordlists/cleaned_directory-list-2.3-medium.txt.txt'
clean_path_file(input_file, output_file)
