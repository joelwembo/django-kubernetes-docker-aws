# django-kubernetes-docker-aws

Install and Set Up kubectl on Linux
Before you begin
You must use a kubectl version that is within one minor version difference of your cluster. For example, a v1.25 client can communicate with v1.24, v1.25, and v1.26 control planes. Using the latest compatible version of kubectl helps avoid unforeseen issues.

Install kubectl on Linux
The following methods exist for installing kubectl on Linux:

Install kubectl binary with curl on Linux
Install using native package management
Install using other package management
Install kubectl binary with curl on Linux
Download the latest release with the command:

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
Note:
To download a specific version, replace the $(curl -L -s https://dl.k8s.io/release/stable.txt) portion of the command with the specific version.

For example, to download version v1.25.0 on Linux, type:

curl -LO https://dl.k8s.io/release/v1.25.0/bin/linux/amd64/kubectl
Validate the binary (optional)

Download the kubectl checksum file:

curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
Validate the kubectl binary against the checksum file:

echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
If valid, the output is:

kubectl: OK
If the check fails, sha256 exits with nonzero status and prints output similar to:

kubectl: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
Note: Download the same version of the binary and checksum.
Install kubectl

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
Note:
If you do not have root access on the target system, you can still install kubectl to the ~/.local/bin directory:

chmod +x kubectl
mkdir -p ~/.local/bin
mv ./kubectl ~/.local/bin/kubectl
# and then append (or prepend) ~/.local/bin to $PATH
Test to ensure the version you installed is up-to-date:

kubectl version --client
Or use this for detailed view of version:

kubectl version --client --output=yaml    
Install using native package management
Debian-based distributions
Red Hat-based distributions
Update the apt package index and install packages needed to use the Kubernetes apt repository:

sudo apt-get update
sudo apt-get install -y ca-certificates curl
If you use Debian 9 (stretch) or earlier you would also need to install apt-transport-https:

sudo apt-get install -y apt-transport-https
Download the Google Cloud public signing key:

sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
Add the Kubernetes apt repository:

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
Update apt package index with the new repository and install kubectl:

sudo apt-get update
sudo apt-get install -y kubectl
Install using other package management
Snap
Homebrew
If you are on Ubuntu or another Linux distribution that supports the snap package manager, kubectl is available as a snap application.

snap install kubectl --classic
kubectl version --client
Verify kubectl configuration
In order for kubectl to find and access a Kubernetes cluster, it needs a kubeconfig file, which is created automatically when you create a cluster using kube-up.sh or successfully deploy a Minikube cluster. By default, kubectl configuration is located at ~/.kube/config.

Check that kubectl is properly configured by getting the cluster state:

kubectl cluster-info
If you see a URL response, kubectl is correctly configured to access your cluster.

If you see a message similar to the following, kubectl is not configured correctly or is not able to connect to a Kubernetes cluster.

The connection to the server <server-name:port> was refused - did you specify the right host or port?
For example, if you are intending to run a Kubernetes cluster on your laptop (locally), you will need a tool like Minikube to be installed first and then re-run the commands stated above.

If kubectl cluster-info returns the url response but you can't access your cluster, to check whether it is configured properly, use:

kubectl cluster-info dump
Optional kubectl configurations and plugins
Enable shell autocompletion
kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell, which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

Bash
Fish
Zsh
Introduction
The kubectl completion script for Bash can be generated with the command kubectl completion bash. Sourcing the completion script in your shell enables kubectl autocompletion.

However, the completion script depends on bash-completion, which means that you have to install this software first (you can test if you have bash-completion already installed by running type _init_completion).

Install bash-completion
bash-completion is provided by many package managers (see here). You can install it with apt-get install bash-completion or yum install bash-completion, etc.

The above commands create /usr/share/bash-completion/bash_completion, which is the main script of bash-completion. Depending on your package manager, you have to manually source this file in your ~/.bashrc file.

To find out, reload your shell and run type _init_completion. If the command succeeds, you're already set, otherwise add the following to your ~/.bashrc file:

source /usr/share/bash-completion/bash_completion
Reload your shell and verify that bash-completion is correctly installed by typing type _init_completion.

Enable kubectl autocompletion
Bash
You now need to ensure that the kubectl completion script gets sourced in all your shell sessions. There are two ways in which you can do this:

User
System

echo 'source <(kubectl completion bash)' >>~/.bashrc
If you have an alias for kubectl, you can extend shell completion to work with that alias:

echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
Note: bash-completion sources all completion scripts in /etc/bash_completion.d.
Both approaches are equivalent. After reloading your shell, kubectl autocompletion should be working. To enable bash autocompletion in current session of shell, run exec bash:

exec bash
Install kubectl convert plugin
A plugin for Kubernetes command-line tool kubectl, which allows you to convert manifests between different API versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release. For more info, visit migrate to non deprecated apis

Download the latest release with the command:

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert"
Validate the binary (optional)

Download the kubectl-convert checksum file:

curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert.sha256"
Validate the kubectl-convert binary against the checksum file:

echo "$(cat kubectl-convert.sha256) kubectl-convert" | sha256sum --check
If valid, the output is:

kubectl-convert: OK
If the check fails, sha256 exits with nonzero status and prints output similar to:

kubectl-convert: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
Note: Download the same version of the binary and checksum.
Install kubectl-convert

sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert
Verify plugin is successfully installed

kubectl convert --help
If you do not see an error, it means the plugin is successfully installed.
