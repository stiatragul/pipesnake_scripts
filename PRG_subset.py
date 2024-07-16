import os
import argparse

def filter_fasta(input_file, output_file, keyword):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_sequence = False
        for line in infile:
            if line.startswith('>'):
                if keyword in line:
                    write_sequence = True
                    outfile.write(line)
                else:
                    write_sequence = False
            elif write_sequence:
                outfile.write(line)

def process_directory(input_dir, output_dir, keyword):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".fasta"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            filter_fasta(input_file, output_file, keyword)
            print(f"Processed {filename}")

def main():
    parser = argparse.ArgumentParser(description="Filter FASTA files for sequences containing a specific keyword in their headers.")
    parser.add_argument("input_dir", help="Directory containing input full FASTA files")
    parser.add_argument("output_dir", help="Directory to save the filtered FASTA files")
    parser.add_argument("--keyword", default="AHE", help="Keyword to filter sequences by (default: 'AHE')")
    
    args = parser.parse_args()
    
    process_directory(args.input_dir, args.output_dir, args.keyword)

if __name__ == "__main__":
    main()
