Run the first program to create MFCCs then run the second program to train.

If you want to trim your dataset or want a 'other' word that picks up when none of the words wanted are said, use the RemoveUnwantedFiles.py script. It SHOULD NOT be in the dataset directory and will delete a lot of files in the dataset. Open it to modify according to your system (file paths and unwanted words).  

***RUN THE REMOVE FILE SCRIPT BEFORE RUNNING THE JUPYTER NOTEBOOKS***

To run these notebooks, first activate your Conda environment 

```
conda activate {nameofenv}
```
Then open notebook with:
```
jupyter notebook
```
Then navigate to the notebook files.
