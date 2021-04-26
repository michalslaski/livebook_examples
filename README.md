# Elixir Livebook examples

A collection of Livebook .livemd examples with training datasets.

## Salary prediction

### Python3 version

Training time: 2.860s

```
$ cd salary_prediction
$ python3 salary_prediction.py
```

### Jupyter Notebook

Training time: 12.639s

```
$ cd salary_prediction
$ jupyter notebook
```

### Google Colab

Training time: 23.478

```
$ cd salary_prediction
$ jupyter notebook  --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
```

Upload salaries.csv to your Google Drive and add this at the top of the notebook:

```
from google.colab import drive
drive.mount('/content/gdrive')
!cat ./gdrive/MyDrive/MachineLearning/salaries.csv
```

Then update the cell to read_csv from your actual path.
