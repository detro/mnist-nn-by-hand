# MNBH - MNIST Neural-Network By Hand

Learning exercise: training a Neural Network by hand. Will use, of course, the most classical of datasets:
the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset.

Once I have a first trained model, I want to apply a few ideas:

* [ ] Apply image transformations to enhance training, and improve scoring
  * For example, rotation +/- 45 degrees
* [ ] Train and test with [QMNIST](https://github.com/facebookresearch/qmnist)
* [ ] Train and test with [EMNIST](https://www.nist.gov/itl/products-and-services/emnist-dataset)
* [ ] Train and test with [Fashion MNIST](https://www.wikiwand.com/en/articles/Fashion_MNIST)

## Setup

This repository is based on https://asdf-vm.com/ and https://taskfile.dev/.
You will have to install `asdf` or provide the dependencies listed in [`.tool-versions`](./.tool-versions).

If `asdf` is already installed in your system, please do the following:

```shell
# Add all necessary plugins to `asdf`
$ asdf plugin add task
$ asdf plugin add python
$ asdf plugin add poetry
# Install tools via `asdf`
$ asdf install
# Initialize codebase
$ task init
```

Now you can use the `task`: tap `TAB` twice to get a list of available commands.

## Usage

### `render_example`

```shell
# Render a random example digit from MNIST
$ task render_example
# Render a specific example digit from MNIST
$ task render_example -- --id 1234
# Help
$ task render_example -- --help
```

<details>
<summary>Output for training image `12345`</summary>
  
```shell
$ task render_example -- --id 12345
* Data Set: mnist (training) (size: 60000)
* Image ID: 12345
* Image Label: 3
┌────────────────────────────┐
│                            │
│                            │
│                            │
│                            │
│                            │
│              ▒█████▒       │
│           ░▓████████       │
│         ░▓██████████▒      │
│         ▓██████▓▓████      │
│        ░██████▓  ░▓██░     │
│        ░█████▓    ▒██░     │
│         ▒██▒      ▒██      │
│                  ░███      │
│                 ▒███▓      │
│              ░▒████▒       │
│             ░█████░        │
│             ▓████▒         │
│              ████▓         │
│       ▒       ▒███░        │
│     ░██       ░███         │
│     ▒█▓      ░███▓         │
│     ▓█░    ░▒████░         │
│     ███▓▓▓▓████▓▒          │
│     ▒█████████▒            │
│     ░▓██████▓              │
│                            │
│                            │
│                            │
└────────────────────────────┘
```
</details>

## Datasets

### Installation

```shell
$ task dataset.download
```

### Citations

* Yann LeCun, Courant Institute, NYU Corinna Cortes, Google Labs, New York Christopher J.C. Burges, Microsoft Research, Redmond.
  MNIST: The MNIST Dataset of handwritten digits
  * Retrieved from: https://github.com/fgnt/mnist (because official website seems empty now)
  * Official website: http://yann.lecun.com/

* Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017).
  EMNIST: an extension of MNIST to handwritten letters.
  * Retrieved from: http://arxiv.org/abs/1702.05373.
  * Official website: https://www.nist.gov/itl/products-and-services/emnist-dataset