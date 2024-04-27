# Contributing to Stack Analyzer

Thank you for considering contributing to Stack Analyzer! This guide will help you get started with contributing to
our project. Whether it's a bug fix, a new analyzer, extending an existing functionality, even a typo fix, we appreciate all forms of contribution.

## Types of Contributions

We accept any type of contribution, including:

- Bug fixes
- Typos fixes
- New features / analyzers
- Documentation updates

## How to Contribute

To contribute to Stack Analyzer, follow these steps:

1. Clone the repository to your local machine.
2. Make your changes to the code or documentation.
3. Create a new branch for your changes using a descriptive name.
4. Commit your changes to the new branch.
5. Push your changes your newly created branch.
6. Submit a pull request (PR) to the base (main) branch.

Please make sure to include a clear and descriptive commit message for your changes. Also, make sure that your changes
are well tested and do not break any existing functionality.

## Guidelines

### General

When contributing to Stack Analyzer, please keep the following guidelines in mind:

1. Code should be well documented and follow the Python coding standards.
2. Pull requests should include a description of what the changes are, why they are needed, and how they address any
   issues or improve the project.
3. Pull requests should include a test plan and should have been tested locally before being submitted.
4. All code changes should be reviewed and approved by at least one other repository contributor before being merged.
5. Pull requests should not include any infrastructure changes that could cause potential downtime or other issues.

### Git Branches

Branch prefixes help to make it clear what the purpose of the PR branch is and make it easier for reviewers to
understand the changes being made. It's important to use consistent prefixes across all PR branches in the repository
to maintain a clear and organized codebase.

- `feature/`: Used for new features or functionality being added to the repository.
- `fix/`: Used for fixing a bug or issue in the Python code, tests or library functions.
- `refactor/`: Used for refactoring the codebase without changing its behavior.
- `docs/`: Used for changes to the documentation related to the codebase.
- `test/`: Used for changes related to testing the library functionality.

For example,

- `feature/add-authentication`: Adding a new authentication method to the API.
- `fix/fix-endpoint-response`: Fixing an issue with the response of a specific endpoint.
- `refactor/restructure-golang-packages`: Refactoring the Golang packages to make them easier to use.
- `docs/update-readme`: Updating the README file to include more information about the API and Golang code.
- `test/add-unit-tests`: Adding unit tests for the Golang code.

_**Note: Commits directly on main are not accepted.**_

### Git Commit Messages

- Use present tense ("Add analyzer..." not "Added analyzer..")
- Use imperative mood ("Update return type..." not "Updates return type...")
- Describe what you do and not how or why you do

The following are good examples for commit messages:

```txt
Change library's return type from JSON to XML
Upgrade Python version to the latest one
Replace the authentication method with a more secure one
```

### Updating the library

Once we some changes that we want to publish to PyPI (or test.PyPi), we can build a new library version as such:

```bash
python setup.py sdist bdist_wheel # build a new version
twine upload --repository testpypi dist/* # publish to test PyPI
```

## Getting Help

If you have any questions or need help contributing to Stack Analyzer, please reach out to the maintainers on our [Discord server](https://discord.com/invite/pqg5sxhx6Y) or by email.

Thank you for contributing to Stack Analyzer!
