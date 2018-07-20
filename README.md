![jupyter](https://jupyter.org/assets/try/jupyter.png "Jupyter")

# Jupyter Talk

## [Link to slides](https://cdn.rawgit.com/shahzeb1/jupyter-talk/868c561e/Slides.slides.html) and [link to Notebook](https://nbviewer.jupyter.org/github/shahzeb1/jupyter-talk/blob/7c4c28aa59485bd41bd2684dffc7114d10dac335/Walkthrough.ipynb).

The following repo contains all the Notebooks and slides for a talk I gave about Jupyter Notebooks over at Lawrence Berkeley National Laboratory.

**GOAL**: Get a Jupyter Notebook environment up and running on CORI → how to get custom packages installed → how to integrate with tools like TensorBoard right within the Notebook → how to collaborate with your team using git

## Helpful tools:

1. Use [NBViewer](https://plot.ly/python/ipython-notebook-tutorial/) to view your Jupyter notebooks via Git.
2. Use [Plot.ly](https://plot.ly/python/ipython-notebook-tutorial/) for interactive graphs.
3. Use [Raw Git](http://rawgit.com/) to host .html files.

## Jupyter to Python conversion:

```
jupyter nbconvert --to script Test.ipynb
```

Make some minor changes to the `.py` file:

1. Get rid of the magic line
2. Add the following line before you import plt `matplotlib.use('agg')`
3. Instead of `plt.show()` use `plt.savefig('output/languages.png')`
4. Run with $ python3 <file>.py

## Make Slides with Jupyter:

```
jupyter nbconvert --to slides Slides.ipynb --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0"
```