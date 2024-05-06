# nanogpt
NanoGPT from Andrej Karpathy's Video tutorial 
Watched the entire playlist, very informative and with a teacher like Andrej, accessible too. 

### A. Lessons and Observations from Micrograd 

1. Pytorch Documentation - the detail and depth of understanding of this library
2. Lego blocks type of building
3. Understanding the calculus - (n - 1) instead of n !!!
4. Step by Step - Explanation
5. Understanding of the library in depth and even questioning it (Repeated yes ....)
6. Dimensions, dimensions and broadcasting !!!
7. Subtle bugs - Generally because of broadcasting and not understanding the dimensions of the vectors
8. As he says - "lot of gymnastics around these multi-dimensional arrays, ton of trying to make these shapes work, layers shape"
9. He prototypes the layers in a jupyter notebook to check if it works and then transfers it to a working model
10. Dilated causal convoluted layers !!! A mouthful !!!

https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing

### B. Lessons from Tokenization

1. What I knew of a tokernizer before this tutorial - A way to check how much to pay based the number of tokens in the input and output text. And the tokens did not match the words, they broke across words.

This tutorial opens up a whole new world of how tokenizer influences the learning of the LLM. And yes it is hairy and gnarly to use Andrej's own words. 

1. Tokenizer for spaces in gpt2 vs latest - Earlier spaces were considered separate and spaces were not combined even if they were continuous, so number of tokens were higher. Later models do combine contiguous spaces.
2. It is the tokenizer that decides on the embeddings.
3. Treatment  of punctuation with words in gpt2 at encoder.py - for e.g. - dog., dog! etc.
4. The regex explanation yielded some new things for me - 
- \p{L} - Any kind of letter from a language - regex
    I tested with Devanagari script, Kannada script, it worked.
- \p{N} - any kind of numeric in any kind of script
    Tested with numbers in Kannanda and Hindi. 
5. For reasons that I don't fully understand !!! :) - 1:17 - GPT Tokenizer video
Guess there are always things to learn and understand, even if one is the same field.
6. Basic transformer attention model is the same, as is the tokenizer even with change in modalities to some extent (video, image), which is amazing when you think about it. However Sora has visual patches so this is different.
7. Testing of chatgpt using tokens along with Token irregularties - <|endoftext|> - Your  knowledge of these special tokends ends up being an attack surface potentially. 
8. He knows Korean ! :) An elegant way of displaying this.
9. Token economy - YAML is better than JSON 
10. The Best !!! [SoldGoldMagikarp](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation) - Last 10 min of the video

There are trigger words that make the gpt go haywire and behave strangely.
One such example - 
Single reddit user - Potential reason for the behavior, 
That token never appears in the training set for the LLM although present in the tokenizer data.
So token never gets activated, is never updated in the embedding table, never sampled, never used, never trained (completely untrained).
When this feeds into the transformer and it creates undefined behavior.

### Some learnings from the talk at Microsoft Build - "State of GPTs"

1. Revisit your prompting - ask if GPT-4 met the requirement - basically reflection
2. Spread your cognitive efforts per token
3. 1.4 Trillion tokens instead of just 300B tokens - More tokens => Better model
4. Chain of thought - ask it to go step by step
5. The best for most accurate results
Let’s work this out in a step by step way to be sure we have the right answer





