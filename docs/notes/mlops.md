# MLOps Checklist for Repo

- Branching strategy - single trunk, env as branches
- Code confidence checks before PR - black formatting, unit tests & coverage, linting, checkmarx like tools for security vulnarabilites, Sonarqube like tools integration?
- Prevent users from directly modifying main branches & be accessible only via PR
- Run training scripts if model artifact is deleted or monitor blob for file changes.
- CI/CD


# CLI vs Py SDK


### Azure CLI

#### Pros:
1. Using the Azure CLI can be straightforward for executing simple commands without needing to write a lot of code.
2. It can be quicker to set up for straightforward tasks and can be directly integrated into GitHub Actions workflows.
3. Provides direct access to Azure resources and commands, making it easier to manage and configure environments.
4. Great for scripting and quick automation tasks.

#### Cons:
1. As tasks become more complex, managing them through CLI commands can become cumbersome and harder to maintain.
2. Limited by the commands available in the CLI; more complex logic may require workarounds.
3. Errors can be harder to trace compared to more structured code.

### Python SDK

#### Pros:
1. Offers more flexibility for complex tasks and workflows, enabling you to write more sophisticated logic.
2. Code can be more easily organized, modular, and tested compared to a series of CLI commands.
3. Access to a wide range of Python libraries for data manipulation, model training, and more.
4. Easier to integrate with other Python-based MLOps tools and libraries.

#### Cons:
1. Requires familiarity with both Python and the SDK, which might be a barrier for some users.
2. More initial setup might be required, such as creating virtual environments or managing dependencies.
3. Python scripts can take longer to execute compared to simple CLI commands.

### Conclusion

- If you’re working on simpler tasks or need quick automation with minimal setup, the Azure CLI might be more appropriate.
- For complex MLOps workflows that require flexibility, maintainability, and integration with data processing or model training libraries, the Python SDK would likely be the better choice.
.