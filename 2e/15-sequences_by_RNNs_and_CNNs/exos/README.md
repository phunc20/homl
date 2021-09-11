## Dataset Source
- <https://github.com/ageron/handson-ml2/blob/master/datasets/jsb_chorales/README.md>
- <https://github.com/czhuang/JSB-Chorales-dataset/blob/master/README.md>

I have opted to copy the same directory structure as Mr. Geron. That is, I downloaded the
dataset and put it under `homl/2e/datasets/`


## Data Description
> - Each chorale is composed of 100 to 640 chords with a temporal resolution of 1/16th.
> - Each chord is composed of 4 integers (MIDI number, e.g. `60=C4, 61=C#4, 62=D4, 72=C5, etc.`), each indicating the index of a note on a piano, except for the value 0 which means "no note played".

```bash
~/.../2e/15-sequences_by_RNNs_and_CNNs/exos ❯❯❯ grep ",0," jsb_chorales/train/*.csv | head -10
jsb_chorales/train/chorale_034.csv:0,0,0,0
jsb_chorales/train/chorale_034.csv:0,0,0,0
jsb_chorales/train/chorale_034.csv:0,0,0,0
jsb_chorales/train/chorale_034.csv:0,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
jsb_chorales/train/chorale_034.csv:76,0,0,0
~/.../2e/15-sequences_by_RNNs_and_CNNs/exos ❯❯❯
```

