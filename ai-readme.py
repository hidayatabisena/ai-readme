import os
import subprocess
from openai import OpenAI

client = OpenAI(
    api_key='YOUR_API_KEY',
)


def read_code(folder_path, file_extensions):
    code = ''
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    code += f.read()
    return code


def generate_readme(code):
    prompt = f"```swift\n{code}\n```"
    response = client.completions.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()


def main():
    file_extensions = input(
        "Enter the file extensions to read (comma-separated): ").split(',')

    folder_path = subprocess.run(
        ['pwd'], capture_output=True, text=True).stdout.strip()
    confirm_path = input(
        f"The current folder path is '{folder_path}'. Is this correct? (Y/N): ")

    if confirm_path.lower() == 'n':
        folder_path = input("Enter the specific folder path: ")

    code = read_code(folder_path, file_extensions)
    readme_content = generate_readme(code)

    with open('README.md', 'w') as f:
        f.write(readme_content)

    print('README.md file generated successfully.')

    # Check rate limit usage
    usage = client.usage.retrieve()
    print(
        f"API Credits Used: {usage['usage']['total']} / {usage['usage']['total']}")
    print(f"API Credits Remaining: {usage['usage']['remaining']}")


if __name__ == '__main__':
    main()
