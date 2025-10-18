# Crop Management and Solutions

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1%2B-orange)](https://python.langchain.com/)

## Project Description

**Crop Management and Solutions** is an innovative web application designed to empower farmers and agricultural experts with AI-driven insights for crop health monitoring and management. The platform allows users to upload crop images, which are classified using a Convolutional Neural Network (CNN) model to detect issues like pests, diseases, or nutrient deficiencies. Once classified, the system leverages the Gemini API, integrated via LangChain and LangGraph, to generate real-time, actionable recommendations—such as treatment plans, preventive measures, or resource allocation strategies—tailored to the detected problem.

Hosted on Flask, the application provides a simple, intuitive interface for image uploads, result visualization, and solution delivery. Whether you're a smallholder farmer seeking quick advice or a large-scale operation optimizing yields, this tool bridges computer vision, natural language processing, and domain expertise to promote sustainable agriculture.

Key Features:
- **Image Classification**: CNN-based detection of crop anomalies with high accuracy.
- **AI-Powered Recommendations**: Gemini API generates context-aware solutions using LangChain for orchestration and LangGraph for multi-step reasoning workflows.
- **User-Friendly Web Interface**: Built with Flask for seamless deployment and scalability.
- **Extensible Architecture**: Easy to integrate additional models or APIs for broader crop coverage.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher ([Download here](https://www.python.org/downloads/)).
- Git ([Download here](https://git-scm.com/downloads)).
- A GitHub account for forking and contributing.
- (Optional) Docker for containerized deployment.

## Setup Instructions

### 1. Cloning the Repository
To get started, clone this repository to your local machine:
```
git clone https://github.com/yourusername/crop-management-solutions.git
cd crop-management-solutions
```

### 2. Creating a Python Virtual Environment (venv)
A virtual environment isolates project dependencies, preventing conflicts with other Python projects. Create one as follows:

#### On Unix/macOS/Linux:
```bash
# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

#### On Windows:
```bash
# Create the virtual environment
py -m venv venv

# Activate it
venv\Scripts\activate
```

**When to use venv?**
- Always at the start of a new project to manage dependencies cleanly.
- Before installing packages to avoid polluting your global Python installation.
- In team environments to ensure reproducible setups—everyone uses the same isolated space.

Once activated, your terminal prompt will change (e.g., `(venv)` prefix), indicating the environment is active. To deactivate later, simply run `deactivate`.

### 3. Installing Dependencies
With the venv active, install the required packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

This installs:
- Flask for the web server.
- TensorFlow/Keras or PyTorch for CNN model training/inference.
- LangChain and LangGraph for Gemini API integration.
- Other utilities like Pillow for image processing, requests for API calls, etc.

**When to install requirements?**
- After cloning or pulling updates that modify `requirements.txt`.
- When setting up on a new machine or environment.
- Post-venv creation to ensure packages are installed in the isolated space.

If you encounter issues (e.g., missing system libraries), refer to the package documentation (e.g., `pip install tensorflow` may require CUDA for GPU support).

### 4. Freezing Requirements
After installing or updating packages, "freeze" the current environment to generate or update `requirements.txt` for reproducibility:
```bash
pip freeze > requirements.txt
```

**When and how to freeze requirements?**
- **When**: After adding new packages (e.g., `pip install some-package`), before committing changes. This captures exact versions, ensuring others can replicate your setup without version mismatches.
- **How**: Run the command in your active venv. It outputs a list like `Flask==2.3.3` to the file. Review it manually to remove unnecessary dev dependencies if needed (e.g., testing tools).
- **Best Practice**: Commit `requirements.txt` to the repo, but never commit the `venv` folder (add it to `.gitignore`).

### 5. Environment Configuration
Create the env file:
```bash
cd models/
touch .env
```
Edit `.env` to add your Gemini API key (Given by group leader but normally obtained from [Google AI Studio](https://aistudio.google.com/)):
```
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development  # Set to 'production' for deployment
```

**Security Note**: Never commit `.env` to Git—it's already in `.gitignore`.

### 6. Running the Application
Start the Flask development server:
```bash
flask run
```
Or with auto-reload:
```bash
python app.py  # Assuming main file is app.py
```
Visit `http://127.0.0.1:5000` in your browser. Upload a crop image to test classification and solution generation.

For production deployment:
- Use Gunicorn/Waitress: `gunicorn -w 4 app:app`.
- Deploy to Heroku, Vercel, or AWS with environment variables set.

## Usage

1. **Upload Image**: Select a crop photo (e.g., leaf with blight) via the web form.
2. **Classification**: The CNN processes the image and outputs a diagnosis (e.g., "Tomato Late Blight").
3. **Generate Solutions**: LangGraph orchestrates a chain: Query Gemini via LangChain for step-by-step advice (e.g., "Apply fungicide X; monitor humidity").
4. **View Results**: Downloadable report with visuals and links to resources.

Example Workflow:
- Train/update CNN: Run `python train_cnn.py --data_path ./data`.
- Test API: `curl -X POST http://localhost:5000/classify -F "image=@crop.jpg"`.

## Git Workflow Guide

This project follows a standard GitHub workflow for collaboration. Below are detailed instructions on key Git commands, including when and how to use them. Always work in a feature branch to avoid disrupting the main codebase.

### Basic Local Workflow (add, commit, push)
These form the core of daily development.

- **git add**: Stages changes for commit. Use to prepare files for versioning.
  - **When**: After editing files (e.g., updating CNN model code or adding a new LangChain prompt).
  - **How**:
    ```bash
    # Stage a specific file
    git add app.py
    
    # Stage all changes (use cautiously)
    git add .
    
    # Stage interactively (review hunks)
    git add -p
    ```
  - **Tip**: Run `git status` first to see unstaged changes. Ignore temp files via `.gitignore`.

- **git commit**: Saves staged changes with a message. Creates a snapshot.
  - **When**: After completing a logical unit of work (e.g., "Implement Gemini integration via LangGraph").
  - **How**:
    ```bash
    # Basic commit
    git commit -m "Add CNN image preprocessing pipeline"
    
    # Verbose with editor for multi-line messages
    git commit
    ```
  - **Best Practice**: Use imperative mood (e.g., "Fix bug" not "Fixed bug"). Keep messages concise (<50 chars for summary).

- **git push**: Uploads local commits to the remote repository.
  - **When**: After committing local changes, to share with the team or back up progress. Push frequently but in small batches.
  - **How**:
    ```bash
    # Push to current branch (e.g., main)
    git push origin main
    
    # Push a new branch
    git push -u origin feature/new-model  # Sets upstream tracking
    ```
  - **Tip**: If pushing fails (e.g., remote changed), pull first (see below).

### Syncing with Remote (fetch, pull, merge)
These handle integrating remote changes.

- **git fetch**: Downloads remote changes without merging. Safe for reviewing.
  - **When**: Before starting work, to check for updates without altering your branch. Useful for inspecting others' commits.
  - **How**:
    ```bash
    git fetch origin  # Fetches from 'origin' remote
    git log --oneline --graph main..origin/main  # View differences
    ```
  - **Tip**: Run periodically; it's non-destructive.

- **git pull**: Fetches and merges remote changes into your branch. Shortcut for `fetch + merge`.
  - **When**: At the start of a session or before pushing, to stay in sync. Avoid during active work to prevent conflicts.
  - **How**:
    ```bash
    git pull origin main  # Pull from main branch
    ```
  - **If Conflicts Arise**: Edit conflicted files, stage (`git add`), then commit. Use `git mergetool` for GUI resolution.

- **git merge**: Integrates changes from one branch into another.
  - **When**: To combine feature branches into main (e.g., after review). Use for local integration before pushing.
  - **How**:
    ```bash
    # From main branch, merge a feature
    git checkout main
    git merge feature/cnn-update
    ```
  - **Tip**: Prefer `--no-ff` for explicit merge commits: `git merge --no-ff feature-branch`. Resolve conflicts manually.

### Branch Management (checkout)
- **git checkout**: Switches branches or restores files.
  - **When**: To start new work (create/switch to feature branch) or revert changes.
  - **How**:
    ```bash
    # Switch to existing branch
    git checkout main
    
    # Create and switch to new branch
    git checkout -b feature/gemini-integration
    
    # Restore a file to last commit
    git checkout -- app.py
    ```
  - **Modern Alternative**: Use `git switch` for branches (`git switch -c new-branch`).
  - **Tip**: Always branch off `main` for features: `git checkout -b fix/bug-description`.

### GitHub-Specific Actions (fork, pull request)
These are done via the GitHub website for collaboration.

- **Fork on GitHub**:
  - **When**: If contributing to someone else's repo (not your own). Creates your copy to work independently.
  - **How**:
    1. Go to the repo on GitHub.com.
    2. Click "Fork" in the top-right.
    3. Clone your fork: `git clone https://github.com/yourusername/crop-management-solutions.git`.
    4. Add upstream remote: `git remote add upstream https://github.com/originalowner/crop-management-solutions.git`.
  - **Sync Fork**: `git fetch upstream && git checkout main && git merge upstream/main && git push origin main`.

- **Pull Request (PR) on GitHub**:
  - **When**: To propose changes from your fork/branch to the original repo. Use for features, bug fixes, or docs updates—after local testing.
  - **How**:
    1. Push your branch: `git push origin feature/your-change`.
    2. On GitHub, click "Compare & pull request" from your branch.
    3. Add title (e.g., "Enhance LangGraph workflow for multi-crop support"), description (link issues, explain changes), and assign reviewers.
    4. Once merged, delete the branch.
  - **Best Practice**: Keep PRs small (<200 lines). Reference issues: "Closes #123". Use drafts for WIP.

### Full Example Workflow
1. Fork/clone repo.
2. `git checkout -b feature/new-cnn-model`.
3. Edit files, `git add .`, `git commit -m "Train CNN on expanded dataset"`.
4. `git push -u origin feature/new-cnn-model`.
5. Create PR on GitHub.
6. While waiting: `git fetch origin`, `git checkout main`, `git pull origin main` to stay updated.
7. If approved, merge via PR; locally: `git checkout main`, `git pull origin main`.

## Contributing

We welcome contributions! Follow the workflow above:
- Open issues for bugs/features.
- Submit PRs with tests (add to `tests/`).
- For major changes, discuss in an issue first.

Run tests: `pytest` (after installing dev deps: `pip install -r requirements-dev.txt`).

---