def celsius_converter(f_temp: float | str) -> float:
        return round((float(f_temp) - 32) * 5.0 / 9.0, 2)

def parse_and_clean(line: str):
    if "|" not in line:
        return None

    data = [item.strip() for item in line.split("|")]

    if len(data) != 5 or data[4] != "ACTIVE" or data[2] in ["ERROR", "N/A", ""]:
        return None

    return data

input_file = "environmental_raw.txt"
output_file = "outputs.csv" 
skipped = 0

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    
    for line in infile:
        
        if not line.strip():
            skipped += 1
            continue
            
        clean = parse_and_clean(line) 
        
        if clean is not None:
            
            converted_temp = celsius_converter(clean[2])
            clean[2] = str(converted_temp)
            outfile.write(",".join(clean) + "\n")

        else: 
            skipped += 1

print("Skipped lines:", skipped)