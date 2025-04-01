# Audio-Tools

This repo contains some auxiliary codes optimized by minimax, which can be used in text-to-audio training and inference process to improve performance. 

## Modifications

Codes are adapted from the following open-source libraries:
- [korean-romanizer](https://github.com/osori/korean-romanizer) - A Python library for Korean romanization
- [num2words](https://github.com/savoirfairelinux/num2words) - A library that converts numbers to words in multiple languages

We have modified the code to enhance its robustness. The improvements focus on error handling, edge cases, and overall stability to ensure reliable performance in various scenarios.

## Usage

Put the folder you want to use under your project, and import the library in your code.

```
# korean_romanizer
from path.to.korean_romanizer.romanizer import Romanizer
r = Romanizer("안녕하세요")
r.romanize() 

# num2words
from path.to.num2words import num2words
num2words(42)
```

Refer to the original library and the codes for more detailed usage.

## License

Check each subdirectory for LICENSE files, and root directory for NOTICE file.