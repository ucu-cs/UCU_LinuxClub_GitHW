# UCU_LinuxClub_GitHW
> This repo is created as a homework practice for [LinuxClub@UCU](https://github.com/ucu-cs/UCU_Linux_Club) and is designed to demonstrate the git basics.

## Requirements:
This task requries cowsay package to be installed:
* __cowsay__

```pip install -u cowsay```

## HomeWork:
1. Create your own branch and add .gitignore file. It has to include .idea directory and all your other files which are not supposed to be present at remote repo. (E.g. files with credentials)
2. Merge your branch with main.
3. Create another branch to implement the random the algorithm to choose cowsay character. You can use random.choice for it. Hint: you have to modify get_character function.
4. Create a pull request to merge your branch with main. Merge it on *GitHub* or using *GitHub CLI*
5. Switch to branch ```wardady_read_random_quote```. Rebase this branch, so it uses your latest added feature from main branch - choice of the character for cowsay. It is expected that during rebase some conflicts occur. You have to resolve them by yourself.
6. PR&merge your branch with main once done!
