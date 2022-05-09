# CTF Write-Ups
A collection of write-ups for CTF challenges I've solved.

- Cyber Defenders
- Hack the Box
- PicoCTF

If you find any errors or incorrect information in these pages, please let me know.  

---
## Python script:

The Python script converts all .md files in Obsidian to GitHub compatible Markdown.

Does this by adding the full file path to **pasted** images.

![](Pasted%20image%2020220509041143.png)

Combine it with [LightShot](https://app.prntscr.com/en/index.html) and you got yourself a super efficient Git compatible documentation workflow.

### Install:
1. Put the script in the root of the Obsidian file structure you want to make GitHub compatible.
	- It will convert all files in its root directory, plus all subdirectories.
2. Obsidian \[\[Wikilinks]] needs to be turned off.
	- Obsidian Settings -> Files and links -> Use \[\[Wikilinks]] -> `OFF`
3. In order to view and execute directly from Obsidian, 'Detect all file extensions' needs to be turned on.
	- Obsidian Settings -> Files and links -> Detect all file extensions -> `ON`
4. 'Default location for new attachments' needs to be 'in sub folder under current folder'.
	- Obsidian Settings -> Files and links -> Default location for new attachments -> In sub folder under current folder -> Subfolder name -> `attachments`.
	- Edit the `./attachments/` folder name in script to local path if necessary.

---