# Prosograph2

Prosograph2 is an extension on [Prosograph](https://github.com/alpoktem/Prosograph) for viewing bilingual speech corpora. Aligned samples are displayed side by side to accommodate e.g. prosodic comparison. The tool also reads prosodically annotated speech data from Proscript format files.

<p align="center"><img src="https://raw.githubusercontent.com/alpoktem/Prosograph/master/img/prosograph2_dump.png"></p>

## Run

Prosograph is written in [Python mode of Processing](http://py.processing.org/). Once you downloaded and installed Processing, put it in Python mode and then open the main script `Prosograph.pyde` to run.

## Dependencies

[`minim`](http://code.compartmental.net/tools/minim/) library needs to be installed for playback. You can do this directly from Processing.

## Data

Prosograph reads Proscript files. Sample dataset is provided in `data` directory. 

Data specific configurations are set in `dataconfig_<dataset>.py`. Inside this script you need to define `DATASET` as the path to your proscript file or the directory containing your proscript files. You also need to specify the keys used in your proscript files. The configuration file needs to be imported in main `.pyde` file on line:

```
import dataconfig_heroes as dataconfig   #Specify here which dataconfig you want to use
```

To view sample datasets, make sure you change `DATASET` to the exact directory where the dataset resides.

## Visual configurations

Visual configurations are set in `config.py`.

## Operation

Prosograph is operated with the following hotkeys:

* `N` - Skip ahead samples
* `B` - Skip back samples
* `P` - Play/pause
* `R` - Refresh view
* `S` - Save current view as image to disk
* `C` - Change colour palette
* `X`,`Q` - Exit

For playback, audio file needs to be in the same directory and with same name as the proscript file. To play, a section needs to be selected first using left-clicking on wordboxes. 

## Proscript format corpora

Sample data in this repository is taken from [Heroes corpus](http://hdl.handle.net/10230/35572)

To create your own proscript files, please refer to [Proscript python library](https://github.com/alpoktem/proscript).

## Citing

If you use this software, please give attribution. If you want to cite it in your work, you can use the following bibliography entries.

	@article{lre:prosograph,
		author = {Alp Oktem and Mireia Farrus and Antonio Bonafonte},
		title = {Corpora Compilation for Prosody-informed Speech Processing},
		journal = {Language Resources & Evaluation},
		status= {accepted}
	}

	@inproceedings{interspeech2017:prosograph,
		author = {Alp Oktem and Mireia Farrus and Leo Wanner},
		title = {Prosograph: a tool for prosody visualisation of large speech corpora},
		booktitle = {Proceedings of the 18th Annual Conference of the International Speech Communication Association (INTERSPEECH)},
		year = {2017},
		address = {Stockholm, Sweden}
	}
