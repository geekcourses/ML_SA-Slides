# How to create a local copy of a remote repository hosted on GitHub

1. **Open Terminal**:
   Start by opening Command Prompt (CMD) or Git Bash on your computer. Navigate to the folder where you want to clone the repository using the `cd` command:
   ```bash
   cd path/to/your/folder
   ```

1. **Clone the Repository**:
   Use the following command to clone the remote (GitHub) repository. This command creates a local copy of the project on your machine:
   ```bash
   git clone https://github.com/Mitko208/RealFakeJobPostingPrediction.git
   ```

1. **Navigate to the Repository Directory**:
   Change into the directory that was just created:
   ```bash
   cd RealFakeJobPostingPrediction
   ```

1. **Fetch All Branches**:
   To ensure you have access to all branches available in the remote repository, use:
   ```bash
   git fetch --all
   ```

1. **List All Branches**:
   Check which branches are available, including those from the remote:
   ```bash
   git branch -a
   ```
   output:
   ```
   * master
   remotes/origin/Branch-1
   remotes/origin/HEAD -> origin/master
   remotes/origin/master
   remotes/origin/revert-1-master
   remotes/origin/test_branch
   remotes/origin/test_master
   ```

1. **Checkout a Remote Branch**:
   To switch to a specific branch (e.g., `test_branch`), use:
   ```bash
   git checkout test_branch
   ```

1. **List all branches again**:

    ```bash
    git branch -a
    ```

    Now you should have locally the code in 'test_branch' as well:
    ```
    master
    * test_branch
    remotes/origin/Branch-1
    remotes/origin/HEAD -> origin/master
    remotes/origin/master
    remotes/origin/revert-1-master
    remotes/origin/test_branch
    remotes/origin/test_master

    ```
