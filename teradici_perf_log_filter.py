import os
import re
import glob
from datetime import datetime

# Regex used to match relevant loglines (in this case, a specific IP address)
line_regex = re.compile("MGMT_PERF_MON")

# Output file, where the matched loglines will be copied to
output_filename = os.path.normpath("parsed_lines.log")
read_filenames = glob.glob("server*.log*")

# Overwrites the file, ensure we're starting out with a blank file
with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    for filename in read_filenames:
        with open(filename, "r") as in_file:
            # Loop over each log line
            for line in in_file:
                # If log line matches our regex, print to console, and output file
                if (line_regex.search(line)):
                    out_file.write(line)

with open(output_filename, "rw+") as sortme_file:
    lines = sortme_file.readlines()
    lines = sorted(lines)
    sortme_file.truncate(0)
    sortme_file.writelines(lines)
