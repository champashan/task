import itertools
import json
import sys

def generate_versions(template):
    parts = template.split(".")
    versions = []
    for indices in itertools.product(range(1, 10), repeat=parts.count("*")):
        version = []
        idx = 0
        for part in parts:
            if part == "*":
                version.append(str(indices[idx]))
                idx += 1
            else:
                version.append(part)
        versions.append(".".join(version))
    return versions

def read_and_generate_versions(config_path, target_version):
    with open(config_path, 'r') as file:
        config = json.load(file)

    versions = []
    for template in config.values():
        versions.extend(generate_versions(template))

    sorted_versions = sorted(set(versions), key=lambda v: list(map(int, v.split('.'))))
    print("Все версии:", sorted_versions)

    older_versions = [v for v in sorted_versions if list(map(int, v.split('.'))) < list(map(int, target_version.split('.')))]
    print("Версии старше:", older_versions)

if __name__ == "__main__":
    config_path = sys.argv[1]
    target_version = sys.argv[2]
    read_and_generate_versions(config_path, target_version)
