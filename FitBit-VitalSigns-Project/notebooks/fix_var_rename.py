import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('6.0-survival-analysis-complete.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if 'Cox PH Visualization' in src and 'cox_hr' in src:
        new_source = []
        for line in cell['source']:
            # Fix the remaining 'len(hr)' -> 'len(cox_hr)'
            new_line = line.replace(
                "    y_pos = range(len(hr))\n",
                "    y_pos = range(len(cox_hr))\n"
            )
            new_source.append(new_line)
        cell['source'] = new_source
        print(f"Fixed cell {i} - y_pos now uses len(cox_hr)")
        for j, l in enumerate(new_source[13:20]):
            print(f"  {j+13}: {repr(l[:90])}")
        break

with open('6.0-survival-analysis-complete.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("Saved successfully.")
