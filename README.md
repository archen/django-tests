# django-tests
Vagrant box to provide a known-functioning and consistent environment for Django contributors to test changes before committing to the repo.

## Strategy
Overall, the idea is to take the Ansible provisioning scripts used in the current Django test environment and convert all of the service installation steps to Docker containers which will still be provisioned by Ansible.

## Contributing
Make sure that you have VirtualBox, Vagrant, and Ansible installed on your machine. Clone the repository and run `vagrant up` from the root directory to test that your "build chain" is working properly.

After ensuring that your environment is prepared to build the vagrant box, create a new branch with the syntax:
```
`features/descriptive-name` for a feature
-or-
`bugfixes/descriptive-name` for a bug fix
```

Make sure that your commit messages reference the issue number for the issue that your branch should ultimately resolve. E.g.,
```
This commit fixes the dependent library problem for issue #6 
```
This will tie your commit to the issue in github for easier tracking.
