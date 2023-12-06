# AI README Generator

This is a command line application that generates README files for your projects based on the content of a specified git folder or repository. The application utilizes the OpenAI API to generate the README content.


## Features

- Reads code from a local git folder or repository
- Supports customization of file extensions to be included in the README generation
- Generates README files based on the code content using the OpenAI API
- Provides an interactive prompt for file extensions and folder path selection
- Displays API usage information, including API credits used and remaining


## Prerequisites

 - Python 3.x
 - OpenAI Python library (`pip install openai`)
 - [Documentation how to install OpenAI](https://pypi.org/project/openai/)



## Usage

- Clone the repository or download the source code.

```bash
  git clone https://github.com/hidayatabisena/ai-readme.git
  cd ai-readme
```
- Open a terminal or command prompt.
- Navigate to the directory where the `ai-readme.py` file is located.
- Run the command `python3 ai-readme.py` to start the application.
- Enter the file extensions you want to read in your project, separated by commas. Later the program will read your project code based on earlier file extensions.
- Confirm or input the path to your git folder or repository.
- Wait for the application to generate the README file.
- The generated README file will be saved as **README.md** in the current directory.

### Making the Program Executable
To make the program executable from anywhere on the system, you can create a shell script and add it to your system's PATH.

- Check your Python version with this command: `which python` and then copy the output e.g `/usr/local/bin/python3`
- Open a text editor and create a new file. Let's name it `ai-readme.sh`
- Add the following code to the `ai-readme.sh` file:

```bash
#!/bin/bash

timeout 30s /YOUR-PYTHON-PATH/python3 /YOUR-PATH-FOLDER/ai-readme.py "$@"
```
- Replace `/YOUR-PATH-FOLDER/ai-readme.py` with the actual path to your `ai-readme.py` file, and replace `/YOUR-PYTHON-PATH/python3` with your actual python3 path `(e.g /usr/local/bin/python3)`
- Save the file and close the text editor
- Open a terminal and navigate to the directory where you saved the `ai-readme.sh` file
- Make the script executable by running the following command:

```bash
chmod +x ai-readme.sh
```

- Move the script to a directory that is included in your system's PATH. For example, you can move it to `/usr/local/bin` by running:

```bash
sudo mv ai-readme.sh /usr/local/bin/ai-readme
```

Note: The `sudo` command may prompt you to enter your password.

Now, you should be able to run the script from any directory by simply typing `ai-readme` in the terminal.
## Examples

as a standalone python program:

```bash
$ python3 ai-readme.py
Enter the file extensions to read (comma-separated): .xcodeproj,.swift,.txt
The current folder path is '/path/to/your/git/folder'. Is this correct? (Y/N): Y
README.md file generated successfully.
API Credits Used: 2 / 10000
API Credits Remaining: 9998
```

as a executable script:

```bash
$ ai-readme
Enter the file extensions to read (comma-separated): .xcodeproj,.swift,.txt
The current folder path is '/path/to/your/git/folder'. Is this correct? (Y/N): Y
README.md file generated successfully.
API Credits Used: 2 / 10000
API Credits Remaining: 9998
```


## Limitations

- The OpenAI API has rate limits and quotas. Please ensure you have sufficient quota for the OpenAI API usage.
- The application currently supports reading Swift files by default. You can modify the code to include additional file extensions based on your needs.

```python
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
```


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) | [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) | [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
