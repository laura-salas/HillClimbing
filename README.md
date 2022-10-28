# HillClimbing
A simple plot visualization of the hill climbing algorithm.

## Example
Take the formula: 
```
cos(0.25(x^2)) - cos(x)
```
Will produce the following pyplot output when the script is run: <br/>
![graph-gif](https://github.com/laura-salas/HillClimbing/blob/bc7c9d6728e6769ae87b9788aec7bfe5c7c6c275/313219776_8383927455011663_5154466482966879082_n_AdobeExpress.gif)

Note that, just like with the real hill climbing algorithm, every time the algo is run, a random `x` is chosen as a starting point. The algorithm runs until a **local maxima** is reached (which might or might not be the global maxima)
## Parameters: 
`hill_function`, the formula to draw the hill graph 
`NUMBER_OF_POINTS`, how many plot points should be drawn on the graph
`epsilon`, the _neighbourhood_ size, such that for a pivot _i_, and neighbourhood of size _n_, you'd have the points:
```
[i-n, i-n+1, i-n+2, ..., i, i+1, i+2, ..., i+n]
```
`verbose`, which allows additional outputs to the console. 

## Further reading:
[Hill climbing algorithm, Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
