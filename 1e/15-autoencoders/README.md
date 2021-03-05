### Motivation
The **_hailstone sequence_** from the author tries to give us an explanation/motivation as to why
autoencoders work. Putting in other words, it may be easy for computers to memorize very long
sequence, so we increase the difficulty to force it to feel the need to find patterns, just like
the hailstone sequence for us.

autoencoder should probably be translated in Chinese as 自己encoder, i.e. reflecting the fact that
its input and output should be highly similar if not identical.

### PCA and Undercomplete Linear Autoencoder
**(?1)** Prove
- either numerically
- or mathematically
that
> if the autoencoder uses only linear activations (i.e. **no activations**) and the cost function is the MSE, then it ends up performing Principal Component Analysis.

### Tying Weights
**(?2)** Omitting the input layer, do you know why the coding layer is the $\frac{N}{2}$-th layer if there are $N$ layers including the output layer? And why there is a transpose in $W_{N-L+1} = {W_{L}}^{T}$?<br>
**(R2)**
- We know the number of hidden layers is _odd_ because they have to be symmetric with respect to the coding layer.
Adding in the output layer, we see that $N$ is even. It follows naturally that the coding layer should be
the $\frac{N}{2}$-th layer.
- There exist $N$ weight (matrices) as well, labeled from $1$ to $N\,.$ Consider an $L$ such that
$1 \le L \le \frac{N}{2}$. This matrix maps the $L-1$-th layer to the $L$-th layer; in other words, it
maps $n_{L-1}$ neurons to $n_{L}$ neurons. Due to the symmetric nature, the matrix $W_{N-L+1}$ maps
$n_{L}$ neurons to $n_{L-1}$ neurons, and we see why transposing the matrix comes as a natural idea.

