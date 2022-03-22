# Archive
Information on the ia command-line tool can be found here: https://archive.org/services/docs/api/internetarchive/cli.html

We can gather a list of all the pages using:
```bash
ia search 'collection:pastpages' --itemlist > itemlist.txt
```
**collectionNames.py** generates a list of all the different collections contained and **countCollectionNames.py** gives a count of each

**removeDates.py** generates a new list **nodates.txt** that does not contain some of the pages with excess pictures

The format of **nytimes.py** and **russia.py** can be used to generate a new list for the specific collection wanted. That collection can then be downloaded using:
```bash
ia download --itemlist itemlist.txt
```
If we just want to download pictures or metadata, add 

```bash
--glob="*.jpg"
or
--glob="*.png"
or 
--glob="*meta.xml" 
``` 
Depending on what we are trying to download (there may be others).

**TakeSnapshot.py** just contains simple code on how to get a screenshot from a webpage using mobile emulation on Headless Selenium


