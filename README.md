# APCSP Story
Story Assignment for AP Computer Science Principles

To import a story:

1. Create a TSV file as so:
`id\tbackground\tchoice1\tchoice2\tresult1\tresult2`
2. Move the file to `/src/file.txt`
3. Change line 27 in `steps.py` to `i = import_steps('file.txt')`
4. Run `steps.py`