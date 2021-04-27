


### Environment/Packages
The files `environment.yml` and `requirements.txt` are from `ageron`'s `handson-ml2` github repo for `miniconda` and `pip`, respectively.

**N.B.** For computers older than or equal to Thinkpad X200, the `environment.yml`'s tensorflow will not work because it is installed by `pip`. However, `conda`'s TensorFlow package has precompiled versions for the CPU
structure of Thinkpad X200, so instead of installing via `environment.yml`, one can manually install the required packages. For example,
```bash
conda create -n homl2e python=3.7
conda install -n homl2e tensorflow
conda install -n homl2e nbdime -c conda-forge
```
