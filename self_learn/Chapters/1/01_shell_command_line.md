# Shell and Command Line Fundamentals

## Overview

The command line is the foundation of modern software development. While graphical interfaces are convenient, the shell provides unmatched power, automation capabilities, and universal access to system resources. Mastering the command line is essential for AI engineering, data science, and system administration.

---

## Understanding the Shell: Core Concepts

### What is a Shell?

A **shell** is a command-line interpreter that:
1. Accepts text commands from users
2. Interprets and executes those commands
3. Returns output and results
4. Provides a programming environment for automation

**Think of it as:** A conversation interface with your computer's operating system.

---

### Shell vs. Terminal vs. CLI vs. Console

These terms are often confused but have distinct meanings:

#### 1. **Shell** (The Brain)

The **program** that interprets commands.

```
┌─────────────────────────────────────┐
│         Shell Program               │
│  - Bash (Bourne Again Shell)        │
│  - Zsh (Z Shell)                    │
│  - Fish (Friendly Interactive Shell)│
│  - PowerShell (Windows)             │
└─────────────────────────────────────┘
```

**Examples:**
- **Bash**: Default on most Linux systems
- **Zsh**: Default on macOS since Catalina
- **PowerShell**: Windows native
- **Fish**: Modern, user-friendly alternative

**What shells do:**
- Parse command syntax
- Execute programs
- Manage environment variables
- Handle I/O redirection
- Support scripting

#### 2. **Terminal** (The Window)

The **application** that provides a text interface to the shell.

```
┌─────────────────────────────────────┐
│       Terminal Application          │
│  - GNOME Terminal (Linux)           │
│  - iTerm2 (macOS)                   │
│  - Windows Terminal (Windows)       │
│  - VS Code Integrated Terminal      │
└─────────────────────────────────────┘
```

**What terminals do:**
- Display text output
- Accept keyboard input
- Handle colors and formatting
- Support tabs and splits
- Customize appearance

#### 3. **CLI** (Command Line Interface)

The **interaction model** where users type text commands.

```
CLI vs GUI:

CLI:  user@computer:~$ ls -la
      → Text-based interaction
      → Commands and arguments
      → Scriptable and automatable

GUI:  [File Explorer Window]
      → Visual interaction
      → Click and drag
      → Harder to automate
```

#### 4. **Console** (Historical Term)

Originally a **physical terminal device** connected to a computer. Now often used interchangeably with "terminal," but historically referred to the main system terminal.

---

### The Relationship

```
User Types Command
       ↓
Terminal Application (displays text)
       ↓
Shell Program (interprets command)
       ↓
Operating System (executes)
       ↓
Output Returns
       ↓
Terminal Application (displays result)
       ↓
User Sees Output
```

**Example:**
1. You type `ls -la` in **iTerm2** (terminal)
2. **Bash** (shell) interprets the command
3. OS lists directory contents
4. **iTerm2** displays the output with colors

---

## Why the Command Line Matters

### 1. **Universality**

Every computer has a command-line interface:
- Servers (often no GUI)
- Cloud instances (SSH access only)
- Embedded systems
- Containers and virtual machines

**Reality:** Most production systems are Linux servers without GUIs.

### 2. **Automation**

Commands can be scripted and repeated:

```bash
# Manual (GUI): Click, click, click... for 1000 files
# Automated (CLI): One command
for file in *.txt; do
    convert "$file" "${file%.txt}.pdf"
done
```

**Automation = Time savings = Productivity**

### 3. **Remote Access**

SSH (Secure Shell) provides command-line access to remote machines:

```bash
ssh user@remote-gpu-server
# Now you're controlling a machine across the internet
nvidia-smi  # Check GPU status
python train_model.py  # Train AI model
```

### 4. **Precision and Control**

GUI tools often hide options. CLI exposes everything:

```bash
# Find all Python files modified in last 7 days, larger than 1MB
find . -name "*.py" -mtime -7 -size +1M -exec ls -lh {} \;
```

Try doing that with File Explorer clicks!

### 5. **Documentation and Reproducibility**

Commands are self-documenting:

```bash
# Setup script - anyone can reproduce your environment
conda create -n ml python=3.10
conda install pytorch torchvision torchaudio -c pytorch
pip install transformers accelerate
```

**Share this script = Share your entire setup**

---

## Shell Basics: Navigation and Files

### The File System Hierarchy

Unix-like systems use a **tree structure** starting from root (`/`):

```
/                           (root - top of tree)
├── home/                   (user home directories)
│   └── username/           (your home directory)
│       ├── Documents/
│       ├── Downloads/
│       └── projects/
├── usr/                    (user programs)
│   ├── bin/                (executable programs)
│   └── lib/                (libraries)
├── etc/                    (configuration files)
├── var/                    (variable data - logs, caches)
└── tmp/                    (temporary files)
```

**Windows** uses drive letters: `C:\`, `D:\` but WSL maps them to `/mnt/c/`, `/mnt/d/`

---

### Essential Navigation Commands

#### 1. `pwd` - Print Working Directory

**What it does:** Shows your current location in the file system.

```bash
$ pwd
/home/username/projects/ml-research
```

**Why it matters:** You always need to know where you are.

---

#### 2. `ls` - List Directory Contents

**Basic usage:**

```bash
$ ls
file1.txt  file2.py  folder1/
```

**Common options:**

```bash
# Long format (detailed)
$ ls -l
-rw-r--r--  1 user  staff   1234 Nov  4 10:30 file1.txt
drwxr-xr-x  2 user  staff     64 Nov  4 10:31 folder1/

# Show hidden files (starting with .)
$ ls -a
.  ..  .gitignore  .env  file1.txt

# Combine options: long format + hidden + human-readable sizes
$ ls -lah
total 24K
drwxr-xr-x  3 user  staff   96 Nov  4 10:30 .
drwxr-xr-x 15 user  staff  480 Nov  4 09:00 ..
-rw-r--r--  1 user  staff  1.2K Nov  4 10:30 file1.txt
```

**Understanding `ls -l` output:**

```
-rw-r--r--  1 user  staff  1234 Nov  4 10:30 file1.txt
│││││││││   │  │     │      │     │         └─ filename
│││││││││   │  │     │      │     └─ timestamp
│││││││││   │  │     │      └─ size (bytes)
│││││││││   │  │     └─ group
│││││││││   │  └─ owner
│││││││││   └─ number of links
└────────── permissions (explained below)
```

**Permissions breakdown:**

```
-rw-r--r--
│└┬┘└┬┘└┬┘
│ │  │  └── others: r-- (read only)
│ │  └──── group:   r-- (read only)
│ └─────── owner:   rw- (read + write)
└──────── type:     -   (regular file)
                    d   (directory)
                    l   (symbolic link)
```

---

#### 3. `cd` - Change Directory

**Basic navigation:**

```bash
# Go to specific directory
$ cd /home/username/projects

# Go to home directory (shortcut)
$ cd ~
$ cd        # no argument also goes home

# Go up one level
$ cd ..

# Go up two levels
$ cd ../..

# Go to previous directory
$ cd -

# Navigate relative to current location
$ cd ./subfolder/another
```

**Special paths:**

```bash
.       # Current directory
..      # Parent directory
~       # Home directory
-       # Previous directory
/       # Root directory
```

**Pro tip:** Use tab completion!
```bash
$ cd Doc<TAB>     # Autocompletes to "Documents/"
$ cd ~/pro<TAB>   # Autocompletes to "~/projects/"
```

---

### File and Directory Operations

#### 1. `mkdir` - Make Directory

```bash
# Create single directory
$ mkdir my_project

# Create nested directories (parents as needed)
$ mkdir -p projects/ml/experiments/run_001

# Create multiple directories
$ mkdir dir1 dir2 dir3

# Create with specific permissions
$ mkdir -m 755 public_data
```

---

#### 2. `touch` - Create Empty File / Update Timestamp

```bash
# Create new empty file
$ touch script.py

# Create multiple files
$ touch file1.txt file2.txt file3.txt

# Update timestamp of existing file
$ touch existing_file.py

# Create with specific timestamp
$ touch -t 202411041200 dated_file.txt
```

**Practical use:** Quickly create placeholder files for testing.

---

#### 3. `cp` - Copy Files/Directories

```bash
# Copy file
$ cp source.txt destination.txt

# Copy file to directory
$ cp file.txt ~/backup/

# Copy directory (recursive)
$ cp -r folder1/ folder2/

# Copy with verbose output
$ cp -v file.txt backup.txt
'file.txt' -> 'backup.txt'

# Copy preserving attributes (permissions, timestamps)
$ cp -p original.txt copy.txt

# Interactive (ask before overwriting)
$ cp -i file.txt existing.txt
overwrite existing.txt? (y/n)
```

---

#### 4. `mv` - Move/Rename Files

```bash
# Rename file
$ mv oldname.txt newname.txt

# Move file to directory
$ mv file.txt ~/Documents/

# Move multiple files
$ mv file1.txt file2.txt file3.txt ~/backup/

# Move directory
$ mv old_folder/ new_location/

# Rename directory
$ mv old_name/ new_name/
```

**Note:** `mv` is both move AND rename (same operation in Unix).

---

#### 5. `rm` - Remove Files/Directories

```bash
# Remove file
$ rm unwanted.txt

# Remove multiple files
$ rm file1.txt file2.txt file3.txt

# Remove directory and contents (recursive)
$ rm -r old_folder/

# Force removal (no confirmation)
$ rm -f stubborn_file.txt

# Interactive (ask before each deletion)
$ rm -i file.txt
remove file.txt? (y/n)

# Verbose (show what's being deleted)
$ rm -v *.log
removed 'error.log'
removed 'debug.log'
```

**⚠️ Warning:** `rm` is permanent! There's no "Recycle Bin" in the shell.

**Safe practices:**
```bash
# Always use -i for important files
$ rm -i important_file.txt

# Test with ls first
$ ls *.log         # See what would match
$ rm *.log         # Then delete

# Consider using trash instead
$ trash file.txt   # Moves to trash (if installed)
```

---

### Viewing and Searching Files

#### 1. `cat` - Concatenate and Display

```bash
# Display file contents
$ cat file.txt
Hello, world!
This is the file content.

# Display multiple files
$ cat file1.txt file2.txt

# Number lines
$ cat -n script.py
     1  import os
     2  import sys
     3  
     4  def main():
```

---

#### 2. `less` / `more` - Paginated Viewing

```bash
# View large file with scrolling
$ less large_file.txt

# Controls in less:
# Space     - Next page
# b         - Previous page
# /pattern  - Search forward
# ?pattern  - Search backward
# q         - Quit
```

---

#### 3. `head` / `tail` - View Start/End

```bash
# First 10 lines (default)
$ head file.txt

# First 20 lines
$ head -n 20 file.txt

# Last 10 lines
$ tail file.txt

# Last 20 lines
$ tail -n 20 file.txt

# Follow file in real-time (useful for logs)
$ tail -f application.log
```

---

#### 4. `grep` - Search Text

```bash
# Find lines containing "error"
$ grep error logfile.txt

# Case-insensitive search
$ grep -i ERROR logfile.txt

# Show line numbers
$ grep -n "import" script.py
5:import os
6:import sys
12:import numpy as np

# Recursive search in directory
$ grep -r "TODO" ./src/

# Invert match (lines NOT containing pattern)
$ grep -v "debug" logfile.txt

# Count matching lines
$ grep -c "error" logfile.txt
42
```

---

## Understanding Command Structure

### Anatomy of a Command

```bash
command -options arguments
```

**Example:**

```bash
ls -lah /home/user/Documents
│   │   └─ argument (what to operate on)
│   └─ options/flags (how to operate)
└─ command (what to do)
```

---

### Options and Flags

**Short form** (single dash, single character):
```bash
ls -l -a -h
```

**Combined short form:**
```bash
ls -lah      # Same as above
```

**Long form** (double dash, full word):
```bash
ls --all --human-readable -l
```

**Options with values:**
```bash
head -n 20 file.txt          # Short form
head --lines=20 file.txt     # Long form
```

---

### Arguments

**Single argument:**
```bash
cd /home/user
```

**Multiple arguments:**
```bash
cp file1.txt file2.txt file3.txt destination/
```

**Standard input (stdin):**
```bash
cat file.txt | grep "pattern"
#            └─ pipe: output of cat becomes input to grep
```

---

## Powerful Shell Features

### 1. Wildcards (Globbing)

**Match multiple files with patterns:**

```bash
# * matches any characters
$ ls *.txt              # All .txt files
$ ls file*              # Files starting with "file"
$ ls *2024*             # Files containing "2024"

# ? matches single character
$ ls file?.txt          # file1.txt, file2.txt, fileA.txt
$ ls report_202?.pdf    # report_2020.pdf through report_2029.pdf

# [] matches character set
$ ls file[123].txt      # file1.txt, file2.txt, file3.txt
$ ls [A-Z]*.py          # Python files starting with uppercase

# {} matches alternatives
$ ls {*.txt,*.md}       # All .txt and .md files
$ cp file.{txt,backup}  # Expands to: cp file.txt file.backup
```

**Practical examples:**

```bash
# Delete all log files
$ rm *.log

# Copy all Python files to backup
$ cp *.py ~/backup/

# List all files from 2024
$ ls *2024*

# Process all CSV and Excel files
$ process_data {*.csv,*.xlsx}
```

---

### 2. Pipes and Redirection

#### Pipes (`|`) - Chain Commands

**Concept:** Output of one command becomes input to the next.

```bash
# List files, then search for Python files
$ ls -la | grep ".py"

# Count lines in a file
$ cat file.txt | wc -l

# Sort and show unique lines
$ cat data.txt | sort | uniq

# Complex pipeline
$ ps aux | grep python | awk '{print $2}' | xargs kill
#  │       │             │                   └─ kill processes
#  │       │             └─ extract PIDs
#  │       └─ find Python processes
#  └─ list all processes
```

#### Redirection - Save Output

**Standard streams:**

```
stdin  (0) ← Input stream
stdout (1) ← Normal output
stderr (2) ← Error messages
```

**Redirect output:**

```bash
# Overwrite file with output
$ ls -la > files.txt

# Append to file
$ echo "New line" >> files.txt

# Redirect errors
$ command 2> errors.log

# Redirect both output and errors
$ command > output.log 2>&1
$ command &> combined.log        # Bash 4+ shorthand

# Discard output (send to /dev/null, the "black hole")
$ noisy_command > /dev/null 2>&1
```

**Redirect input:**

```bash
# Feed file contents as input
$ command < input.txt

# Here document (multi-line input)
$ cat << EOF > file.txt
Line 1
Line 2
Line 3
EOF
```

---

### 3. Command Substitution

**Use command output as argument:**

```bash
# Backticks (old style)
$ echo "Today is `date`"

# $() syntax (preferred)
$ echo "Today is $(date)"

# Practical examples
$ cd $(find . -name "my_project" -type d)
$ files=$(ls *.txt)
$ kill $(pgrep firefox)
```

---

### 4. Environment Variables

**Variables that configure shell behavior:**

```bash
# View all variables
$ env

# View specific variable
$ echo $HOME
/home/username

$ echo $PATH
/usr/local/bin:/usr/bin:/bin

# Set variable (current session only)
$ export MY_VAR="hello"
$ echo $MY_VAR
hello

# Set permanently (add to ~/.bashrc or ~/.zshrc)
$ echo 'export MY_VAR="hello"' >> ~/.bashrc
```

**Important variables:**

```bash
$HOME       # Your home directory
$PATH       # Directories to search for commands
$USER       # Your username
$SHELL      # Current shell program
$PWD        # Current directory
$OLDPWD     # Previous directory
```

---

## Essential Commands Reference

### File Information

```bash
# File type and info
$ file script.py
script.py: Python script, ASCII text executable

# Disk usage of file/directory
$ du -sh folder/
4.2G    folder/

# Count lines, words, characters
$ wc file.txt
  42  256 1984 file.txt
#lines words bytes

# Find files
$ find . -name "*.py"           # By name
$ find . -type f -size +1M      # Larger than 1MB
$ find . -mtime -7               # Modified last 7 days
```

---

### Process Management

```bash
# List running processes
$ ps aux

# Find process by name
$ pgrep python
$ pgrep -a python    # Show full command

# Interactive process viewer
$ top
$ htop               # Better alternative (if installed)

# Kill process
$ kill 1234          # By PID
$ killall python     # By name
$ pkill -f "script"  # By pattern
```

---

### System Information

```bash
# Disk space
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   42G   53G  45% /

# Memory usage
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       8.2Gi       1.4Gi       428Mi       5.9Gi       6.8Gi

# System uptime
$ uptime
10:30:42 up 5 days, 3:42, 2 users, load average: 0.52, 0.48, 0.45

# Current user
$ whoami
username

# System info
$ uname -a
Linux hostname 5.15.0-52-generic x86_64
```

---

### Network

```bash
# Test connectivity
$ ping google.com

# Download files
$ wget https://example.com/file.zip
$ curl -O https://example.com/file.zip

# Check network interfaces
$ ifconfig
$ ip addr

# Network statistics
$ netstat -tuln     # Listening ports
$ ss -tuln          # Modern alternative
```

---

### Compression and Archives

```bash
# Create tar archive
$ tar -cvf archive.tar folder/
$ tar -czvf archive.tar.gz folder/    # With gzip compression

# Extract tar archive
$ tar -xvf archive.tar
$ tar -xzvf archive.tar.gz

# Zip/Unzip
$ zip -r archive.zip folder/
$ unzip archive.zip
```

---

## Shell Scripting Basics

### Why Script?

**Automation:** Repeat tasks without manual intervention  
**Consistency:** Same process every time  
**Documentation:** Scripts serve as executable documentation

---

### Creating a Script

**1. Create file:**

```bash
$ touch script.sh
```

**2. Add shebang (tells OS which interpreter to use):**

```bash
#!/bin/bash
```

**3. Make executable:**

```bash
$ chmod +x script.sh
```

**4. Run it:**

```bash
$ ./script.sh
```

---

### Basic Script Example

```bash
#!/bin/bash
# Simple backup script

# Variables
SOURCE_DIR="$HOME/Documents"
BACKUP_DIR="$HOME/Backup"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$TIMESTAMP.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create archive
echo "Creating backup: $BACKUP_NAME"
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

# Check if successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
else
    echo "Backup failed!"
    exit 1
fi

# List recent backups
echo "Recent backups:"
ls -lht "$BACKUP_DIR" | head -n 5
```

---

### Script Components

#### Variables

```bash
# Assignment (no spaces around =)
NAME="value"
COUNT=42

# Using variables
echo $NAME
echo ${NAME}    # Preferred, clearer

# Command output as variable
FILES=$(ls *.txt)
CURRENT_DIR=$(pwd)
```

#### Conditionals

```bash
# If statement
if [ -f "file.txt" ]; then
    echo "File exists"
elif [ -d "folder" ]; then
    echo "Directory exists"
else
    echo "Neither exists"
fi

# File tests
[ -f file ]     # File exists
[ -d dir ]      # Directory exists
[ -r file ]     # Readable
[ -w file ]     # Writable
[ -x file ]     # Executable

# String tests
[ -z "$VAR" ]   # String is empty
[ -n "$VAR" ]   # String is not empty
[ "$A" = "$B" ] # Strings are equal

# Numeric tests
[ $A -eq $B ]   # Equal
[ $A -ne $B ]   # Not equal
[ $A -lt $B ]   # Less than
[ $A -gt $B ]   # Greater than
```

#### Loops

```bash
# For loop
for file in *.txt; do
    echo "Processing $file"
    wc -l "$file"
done

# While loop
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done

# Loop over command output
for pid in $(pgrep python); do
    echo "Python process: $pid"
done
```

#### Functions

```bash
# Define function
backup_file() {
    local file=$1
    local backup="${file}.backup"
    cp "$file" "$backup"
    echo "Backed up: $file -> $backup"
}

# Call function
backup_file "important.txt"
```

---

## Platform-Specific Notes

### Linux

**Shell:** Usually Bash (Bourne Again Shell)  
**Package manager:** apt (Debian/Ubuntu), yum (RedHat/CentOS), pacman (Arch)  
**Filesystem:** Case-sensitive  

```bash
# Install software (Ubuntu/Debian)
$ sudo apt update
$ sudo apt install package-name

# System logs
$ journalctl -f
```

---

### macOS

**Shell:** Zsh (Z Shell) since Catalina, previously Bash  
**Package manager:** Homebrew (community)  
**Filesystem:** Case-insensitive by default (but case-preserving)

```bash
# Install Homebrew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install software
$ brew install package-name

# macOS specific
$ open file.txt        # Open with default app
$ pbcopy < file.txt    # Copy to clipboard
$ pbpaste > file.txt   # Paste from clipboard
```

---

### Windows

**Options:**
1. **WSL2 (Windows Subsystem for Linux)** - Recommended
   - Full Linux environment
   - True Bash/Zsh support
   - Best compatibility with Linux tools

2. **PowerShell** - Windows native
   - Different syntax from Bash
   - Windows-integrated
   - Cross-platform (PowerShell Core)

3. **Git Bash** - Bash emulation
   - Minimal Linux tools
   - Good for Git operations

**WSL2 Setup:**

```bash
# In PowerShell (as Administrator)
wsl --install

# Choose distribution
wsl --install -d Ubuntu

# Access WSL
wsl
```

**PowerShell vs Bash:**

| Task | Bash | PowerShell |
|------|------|------------|
| List files | `ls` | `Get-ChildItem` or `ls` |
| Change dir | `cd` | `Set-Location` or `cd` |
| Copy file | `cp` | `Copy-Item` |
| Current dir | `pwd` | `Get-Location` |
| Environment | `$HOME` | `$env:HOME` |

---

## Best Practices

### 1. **Use Tab Completion**

Don't type full paths - let the shell complete them:

```bash
$ cd /hom<TAB>           # → /home/
$ cd /home/use<TAB>      # → /home/username/
$ git chec<TAB>          # → git checkout
```

### 2. **Read the Manual**

Every command has documentation:

```bash
$ man ls                 # Full manual for ls
$ command --help         # Quick help
$ tldr command           # Simplified examples (if installed)
```

### 3. **Use History**

Don't retype commands:

```bash
# Arrow up/down - navigate history
# Ctrl+R - search history interactively

$ history                # Show command history
$ !42                    # Run command #42 from history
$ !!                     # Run last command
$ !$                     # Last argument of previous command
```

### 4. **Alias Common Commands**

Save typing with aliases (add to `~/.bashrc` or `~/.zshrc`):

```bash
alias ll='ls -lah'
alias gs='git status'
alias gc='git commit'
alias py='python3'
alias jl='jupyter lab'
```

### 5. **Be Careful with Destructive Commands**

```bash
# Always use -i (interactive) for rm, mv, cp on important files
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'

# Test patterns before deleting
$ ls *.log       # See what matches
$ rm *.log       # Then delete
```

### 6. **Quote Variables**

Always quote variables to handle spaces correctly:

```bash
# Bad
file=$1
rm $file         # Fails with "my file.txt"

# Good
file="$1"
rm "$file"       # Works with spaces
```

### 7. **Use Shellcheck**

Validate scripts before running:

```bash
$ shellcheck script.sh
```

---

## Getting Help

### Built-in Help

```bash
# Manual pages
$ man command

# Command help
$ command --help
$ command -h

# Which program will run?
$ which python
/usr/bin/python

# What is this command?
$ whatis ls
ls (1) - list directory contents
```

### Online Resources

- **ExplainShell**: https://explainshell.com - Paste commands, get explanations
- **TLDR Pages**: https://tldr.sh - Simplified examples
- **Command Line Fu**: https://www.commandlinefu.com - Community recipes
- **Stack Overflow**: Tag [bash], [shell], [command-line]

---

## Summary

### Core Concepts

✅ **Shell** = Command interpreter (Bash, Zsh, Fish)  
✅ **Terminal** = Application that displays the shell  
✅ **CLI** = Interaction model (text commands)  
✅ **Why CLI?** = Automation, remote access, precision, reproducibility  

### Essential Commands

**Navigation:**
- `pwd` - Where am I?
- `ls` - What's here?
- `cd` - Go somewhere else

**File Operations:**
- `mkdir` - Create directory
- `touch` - Create file
- `cp` - Copy
- `mv` - Move/rename
- `rm` - Delete

**Viewing:**
- `cat` - Display file
- `less` - Paginated viewing
- `head` / `tail` - Start/end of file
- `grep` - Search text

**System:**
- `ps` - Processes
- `df` - Disk space
- `free` - Memory
- `top` - System monitor

### Power Features

✅ **Wildcards** - `*.txt`, `file[123].py`, `{*.csv,*.xlsx}`  
✅ **Pipes** - `command1 | command2 | command3`  
✅ **Redirection** - `command > output.txt 2>&1`  
✅ **Variables** - `$HOME`, `$PATH`, `$(command)`  
✅ **Scripting** - Automate repetitive tasks  

### Next Steps

1. Practice basic commands daily
2. Learn keyboard shortcuts (Ctrl+R, Ctrl+A, Ctrl+E)
3. Customize your shell (`.bashrc`, `.zshrc`)
4. Write simple automation scripts
5. Explore advanced tools (awk, sed, find)

**Remember:** The command line is a skill that compounds. Every command you learn makes the next one easier. Start simple, practice regularly, and soon it becomes second nature.
