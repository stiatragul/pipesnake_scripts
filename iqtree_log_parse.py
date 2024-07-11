# This script is used to parse out the time it takes for IQTREE2 to run gene trees. 
# Takes the information from log files and creates a CSV summary of the time taken for each gene tree.
# The output is written in the same directory as the log files with the name iqtree_log_summary.csv
import os
import csv
import argparse
import re

def convert_to_hm(seconds):
    seconds = float(seconds)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h:{minutes}m"

def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        filename = os.path.basename(log_file).replace('.log', '')
        total_iterations = None
        time_tree_search = None
        total_wall_clock_time = None
        model_finder_time = None
        best_fit_model = None
        threads = None
        samples = None
        length = None
        distinct_patterns = None
        gap_amb = None

        for line in file:
            if line.startswith('Total number of iterations:'):
                total_iterations = line.split(':')[-1].strip()
            elif line.startswith('Wall-clock time used for tree search:'):
                match = re.search(r'(\d+\.\d+) sec', line)
                if match:
                    time_tree_search = match.group(1)
            elif line.startswith('Total wall-clock time used:'):
                match = re.search(r'(\d+\.\d+) sec', line)
                if match:
                    total_wall_clock_time = match.group(1)
            elif line.startswith('Wall-clock time for ModelFinder:'):
                match = re.search(r'(\d+\.\d+) seconds', line)
                if match:
                    model_finder_time = match.group(1)
            elif line.startswith('Best-fit model:'):
                best_fit_model = line.split(':')[1].split('chosen according to BIC')[0].strip()
            elif line.startswith('Kernel:'):
                match = re.search(r'(\d+) threads', line)
                if match:
                    threads = match.group(1)
            elif line.startswith('Alignment has'):
                match = re.search(r'(\d+) sequences with (\d+) columns, (\d+) distinct patterns', line)
                if match:
                    samples = match.group(1)
                    length = match.group(2)
                    distinct_patterns = match.group(3)
            elif line.startswith('****  TOTAL'):
                match = re.search(r'(\d+\.\d+)%', line)
                if match:
                    gap_amb = match.group(1)

        time_tree_search_hm = convert_to_hm(time_tree_search) if time_tree_search else None
        total_wall_clock_time_hm = convert_to_hm(total_wall_clock_time) if total_wall_clock_time else None
        model_finder_time_hm = convert_to_hm(model_finder_time) if model_finder_time else None

        return [
            filename, 
            samples,
            length,
            gap_amb,
            distinct_patterns,
            time_tree_search_hm, 
            total_wall_clock_time_hm, 
            model_finder_time_hm, 
            best_fit_model,
            threads,
            time_tree_search, 
            total_wall_clock_time, 
            model_finder_time, 
            total_iterations
        ]

def main(directory):
    log_files = [f for f in os.listdir(directory) if f.endswith('.log')]
    output_file = os.path.join(directory, 'iqtree_log_summary.csv')

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'filename', 
            'samples',
            'length',
            'gap_amb',
            'distinct_patterns',
            'time_tree_search_hm', 
            'total_wall_clock_time_hm', 
            'model_finder_time_hm', 
            'best_fit_model',
            'threads',
            'time_tree_search_sec', 
            'total_wall_clock_time_sec', 
            'model_finder_time_sec', 
            'total_iterations' 
        ])

        for log_file in log_files:
            log_path = os.path.join(directory, log_file)
            row = parse_log_file(log_path)
            writer.writerow(row)

    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse log files and create a CSV summary.')
    parser.add_argument('directory', type=str, help='Directory containing the log files')
    args = parser.parse_args()

    main(args.directory)
