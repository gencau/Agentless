import json
import glob

max_prompt_tokens = 0
max_file = None
max_instance = None

# Adjust the pattern to match your files
for filename in glob.glob("*.jsonl"):
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            # Safely access the nested prompt_tokens field
            try:
                prompt_tokens = data["file_traj"]["usage"]["prompt_tokens"]
                if prompt_tokens > max_prompt_tokens:
                    max_prompt_tokens = prompt_tokens
                    max_file = filename
                    max_instance = data.get("instance_id")
            except KeyError:
                continue

print(f"Highest prompt_tokens: {max_prompt_tokens}")
print(f"Found in file: {max_file}")
print(f"Instance ID: {max_instance}")
