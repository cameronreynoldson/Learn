# Binary `00100001`
##### :fire: Here we'll be going over some stuff about binary :fire:
* What is binary?
* Why do I need to know it?
* Where is it used?
* How can I apply it?


### What is binary?
Binary is a number representation, which  means we can represent all sorts of numbers in this form. For example:

`00000001` represents the number `1`

`01001011` represents the number `75`

Each digit in the binary representation of a number is called a _**bit**_. Each bit is either a `0` or a `1`. Simple, right? :boom:

While bits are important, we can't do much with them individually. That's why `bytes`, `kilobytes`, `megabytes`, `gigabytes`, etc. exist! Here's a conversion table:

| Name  | Conversion  |
|---|---|
| Byte  | 8 bits |
| Kilobyte (kb)|  1024 bytes  |
| Megabyte (mb) | 1024 kilobytes |
| Gigabyte (gb) | 1024 megabytes |


These are important because computers have circuits inside of them, which are either _on_ (represented by a `1` bit, also called an _on_ bit) or _off_ (represented by `0` bit, also called an _off_ bit). Thankfully, you don't need to know much about this for now :pray:.

Binary is called _**bi**nary_ because each digit is one of two numbers (`0` or `1`) and each number is represented by a combination of powers of `2`.

`Note: a power of 2 is just 2^(some number)`

Binary numbers, or binary *strings*, are read from right to left, _**not**_ left to right. To convert a number from binary to decimal (the number representation we're used to):
* Start at the right most bit
* Keep a counter starting at `0`, we'll call the counter `n`
* Start from the right side, if the bit is a 1, add ```2^n``` to your total, if it is a 0, don't add anything
* Add `1` to `n` and keep going for the rest of the bits

![](http://i.giphy.com/DPnR4JZESpkys.gif)


#### Similar to the decimal system
The decimal system is the number system that is most commonly used. 

For example, `1023` represents the number one thousand and twenty three. We'll see that there are some strong similarities between how we interpret binary and decimal. 

#### Example in decimal
The same way we calculate the binary number, we can calculate a decimal number except using digits `0-9` instead of `0-1` and powers of `10` instead of `2`. For `1023`, we have `10^0 * 3 + 10^1 * 2 + 10^2 * 0 + 10^3 * 1` which gives us one thousand and twenty three. Look familiar now? 

:fire: :fire: :fire:

#### Example in binary
Let's convert the number `00001011` from binary to decimal.

First, we start at the right most bit. Let's establish our counter and our total:
`total = 0`
`counter = 0`

Now, we see that the right most bit is a `1`, so we add `2^0` to our total and add `1` to our counter.

`total = 1`,
`counter = 1`

Next, we see that the second bit is also a `1`, so we add `2^1` to our total and add `1` to our counter.

`total = 3`,
`counter = 2`

Next, because we see that the third bit is a `0` and is not **on**, we don't add `2^counter` to our total; however, we still need to add `1` to our counter to keep track of the current bit that we are at.

`total = 3`,
`counter = 3`

Next, we see that the fourth bit is a `1`, so we add `2^3` to our total and add `1` to our counter.

`total = 11`,
`counter = 4`

Because there are no more `1`s in our binary string, we are done counting. The number is `11`. Good job! :clap:


#### Decimal to binary
You're probably like
> That's great and all, but what if I want to convert a decimal number, say 50, to binary?

No problem! Here are the steps:
* Find the largest power of `2` less than or equal to the number
* Subtract that power of `2` from the number and put a `1` in the place of that power of `2` in the binary string
* Keep doing this until your number is `0`

##### Example
Let's take the number `50`. First, we need to find the largest power of `2` less than or equal to `50`. This happens to be `32`.

`Popular powers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096 ...`

So now there will be a `1` in the `32` spot. Our current number is `100000`, which is `32` in binary.

`Note: we can add any amount of 0s to the front of our number and it will be the same. 0000001000 is the same as 1000.`

Next, we subtract `32` from `50` to get `18`. The largest power of `2` smaller than `18` is `16`, so we put a `1` in the `16` spot and subtract `16` from `18` to get `2`. Our current number is `110000`, which is `16 + 32 = 48`.

Lastly, we find the largest power of `2` less than or equal to `2`, which is just `2`, so we put a `1` in the `2` spot and subtract `2` from `2` to get `0`. Our current number is `110010`, which is `2^1 + 2^4 + 2^5 = 2 + 16 + 32 = 50`. Since we are at 0, we are done.

Congrats, you're now a binary wizard!

![](http://i.giphy.com/BYBPH2ob1Se3e.gif)

### Why do I need to know it?
Binary is important to know because it's the language of the computer. Everything that you will program will be converted down to binary before it runs, which means it's important to know the exact behavior of your program so that you don't run into any weird mistakes such as **integer overflow**.

### Where is it used?
Everywhere! It's the language of the computer. You will almost never have to use binary in your programs (depending on your task); however, it's incredibly important to understand because of what I mentioned above and some nifty tricks you can do by using bits to your advantage.

### How can I apply it?
Though we won't cover it now, here are a couple topics that require an understanding of binary if you're curious, though I don't recommend worrying about them for now:
* [Bitsets](https://en.wikipedia.org/wiki/Bit_array)
* [Avoid integer overflow](https://en.wikipedia.org/wiki/Integer_overflow)

![](http://i.giphy.com/3oEdv5XT0tYl7B77yM.gif)






