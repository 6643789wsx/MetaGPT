from metagpt.software_company import generate_repo, ProjectRepo
import argparse

def main(path):
    with open(path, 'r') as file:
        input_text = file.read()
    repo: ProjectRepo = generate_repo(input_text.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process design document")
    parser.add_argument('-p', type=str, required=True, help='Path to the design document')
    args = parser.parse_args()
    main(args.p)