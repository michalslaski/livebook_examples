# Elixir Livebook examples

A collection of Livebook .livemd examples with training datasets.

## Salary prediction

### Elixir Livebook

Training time: 0.637s

#### Compiling EXLA

First time you run the Livebook notebook it will probably need to compile `exla`, which requires bazel to be installed.

##### EXLA on macOS Big Sur

On macOS Big Sur [this](https://docs.bazel.build/versions/master/install-os-x.html) worked:

```
% export BAZEL_VERSION=3.1.0
% curl -fLO "https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/$ bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh"
% chmod +x "bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh"
% ./bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh --user
```

##### EXLA on RaspberryPi 4

```
$ wget https://github.com/bazelbuild/bazel/releases/download/3.4.0/bazel-3.4.0-linux-arm64
$ chmod u+x bazel-3.4.0-linux-arm64
$ ./bazel-3.4.0-linux-arm64
$ cd ~/bin
$ ln -s /home/pi/dev/bazel/bazel-3.4.0-linux-arm64 bazel
```

#### Install Erlang and Elixir:

Next step is to run Livebook, which requires Erlang and Elixir to be installed.

```
% git clone https://github.com/asdf-vm/asdf.git ~/.asdf
% . $HOME/.asdf/asdf.sh
% asdf plugin add erlang https://github.com/asdf-vm/asdf-erlang.git
% export KERL_CONFIGURE_OPTIONS="--without-javac --enable-lock-counter --with-microstate-accounting=extra"
% asdf install erlang 24.0-rc3
% asdf global erlang 24.0-rc3
% asdf plugin-add elixir https://github.com/asdf-vm/asdf-elixir.git
% asdf install elixir 1.12.0-rc.1-otp-24
% asdf global elixir 1.12.0-rc.1-otp-24

% cat ~/.zshrc
export PATH="$PATH:$HOME/bin"

. $HOME/.asdf/asdf.sh
```

Compile Livebook and start it:

```
% git clone https://github.com/elixir-nx/livebook.git
% cd livebook
% mix deps.get --only prod
% MIX_ENV=prod mix phx.server
```

### Python3 version

Training time: 2.860s

```
% cd salary_prediction
% python3 salary_prediction.py
```

### Jupyter Notebook

Training time: 12.639s

```
% cd salary_prediction
% jupyter notebook
```

### Google Colab

Training time: 23.478s

```
% cd salary_prediction
% jupyter notebook  --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
```

Upload salaries.csv to your Google Drive and add this at the top of the notebook:

```
from google.colab import drive
drive.mount('/content/gdrive')
!cat ./gdrive/MyDrive/MachineLearning/salaries.csv
```

Then update the cell to read_csv from your actual path.
