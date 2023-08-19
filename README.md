# A guide for adding more Voice Engines to use with pyttsx3 (and potentially other tts libraries)

If you're using Windows (10 at least), then you have access to a suite of Microsoft voice engines that your OS can use for it's Narrator function. You also have free access to get more voice engines than the preinstalled ones your system comes with.

That's great, your computer can now speak to you using your preffered voice from a vast list of possibilities.
But if you're e developer, mabye you want to use these voice engines for something more particular than just the Narrator function.

In this text I'll be focusing on adding more voice engines to use with the python module pyttsx3 (Python3 Text To Speech module). Be aware, that no python knowldge is neccesary for actually configuring the voice engines. The environment only really comes into play when we test to see if our configuration was indeed successfull.

>The general problem that might arise with TTS libraries is that, no matter how many voice engines you have installed for your system, your TTS module might still only be able to access the default ones from your sistem. The default list, in most cases is:
>> Microsoft Hazel  - Female    - English   - United Kingdom;   
>> Microsoft David  - Male      - English   - United States;  
>> Microsoft Zira   - Female    - English   - United States;  
> 
>If this is the problem you're experiencing, the following should work as a solution for you, regardless of what TTS module / programming environment you've chosen to use.

# 1. In case you have not already installed your desired new voice engine, let's do that first
Navigate to your narrator settings window (Ctrl + Windows key + N), scroll down a bit and find the "<span style="color:blue">Add more voices</span>" button, and click on it

![Add More Voices Button](./Readme%20Screenshots/AddMoreVoices.png)

Scroll down to "Manage Voices", click on the "<span style="color:blue">Add Voices</span>" button, search for and select your desired voice packages, and finally click the "Add" button in the Voice packages  window.  
For this example, I'll be adding french language voice packages.

![Alt text](./Readme%20Screenshots/VoicePackages.png)

Please note that what you're searching for in the searchbar is the <i>language</i>, but in the case of french we found 3 <i>dialects</i> for our language. If you also look at my visible installed voice packages, you can see I have a lot of english dialetcs, including Indian, Canadian, Australian, etc.

The voice engine will "do" whatever you tell it to do, ultimately you can have an english-language voice engine read a french sentence, but do not expect good results unless you're matching languages.

After you click the Add button, wait for the new voice packages to be installed onto your system

![Voices Installing](./Readme%20Screenshots/VoicesInstalling.PNG)

After the installation is complete, you may try to use your new voices, however the results might not be what you expect:

![Not all voices present](./Readme%20Screenshots/NotAllVoices.png)

In my case, I seem to be only able to use the french dialect of my French language voice package, where's the Canadian and Swiss version?

# 2. Editing registry settings to access our voice packages

You can now close the narrator settings window if you haven't already, we're done with it.  
Now, we're left to work the registry editor, so let's open that:  
>Open a command prompt window (Windows key -> type "cmd" -> Enter key)
>Type <code>regedit</code> and press Enter
>
>![Regedit](./Readme%20Screenshots/cmd.png)

If you now navigate, either by using your mouse, or the navigation bar in your Registry Editor window to the following path: <code>Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens</code>, you will see that not only do we have our Canadian and Swiss dialects present, but we actually have, in this example a grand total of 7 voice models, not just 3 to match the number of dialects we selected.

What gives?

Well, before we continue, let me mention 3 paths in the Registry editor, and a simplification of their importance:

>Location 1 - <code>Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens</code> = Where your voice packages are registered by using the Narrator Setting as described above  
>
>Location 2 - <code>Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens</code> = Where your voice packages <b>SHOULD</b> be registered so their <b>DATA</b> can be accessed by pyttsx3 (and other tts modules)  
>
>Location 3 - <code>Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Speech_OneCore\Voices\Tokens</code> = Where your voice packages <b>SHOULD</b> be registered so their <b>ENGINE</b> can be accessed by pyttsx3 (and other tts modules)

For reference, let me show you all the french packages, immediately after step 1 finished installing them, in each of the above mentioned locations
1. ![Location 1](./Readme%20Screenshots/reg_speech_onecore.png)
2. ![Location 2](./Readme%20Screenshots/reg_speech.png)
3. ![Location 3](./Readme%20Screenshots/reg_speech_wow6432nodepng.PNG)

In this case, I have the correct voice packages registered at locations 1 and 3, <b>but i need them at locations 2 and 3</b>  
<i> Do also note, however that there's no guarantee you will have your packages registered at location 3, only at location 1 - see all those english packages I have present in the example pictures? When first configuring my tts environmeny, they'd only registered themselves at location 1</i>

<b><i>I will continue this guide as if you've only found your voices at location 1</i></b>

Go to "Location 1" in your registry editor, and right click + "Export" the voice package you want to fix. You can also right click and Export the whole "Tokens" folder and bulk-edit multiple reg paths in a single reg file, however since the modifications are the same regardless of how you do it, i'll focus on "fixing" the "Caroline" model for now.

![Caroline Export](./Readme%20Screenshots/CarolineExport.png)

Your exported .reg file should look like this if opened in a text editor (like Notepad++):

![Caroline Registry](./Readme%20Screenshots/CarolineReg.png)
(As noted in the screenshot, you will be missing lines 3 and 4 if you exported one single package instead of the entire folder)

As you can see, the registry editor contains information about both the voice "engine" itself, and a separate "Attributes folder" (visible in the registry editor for each voice if you click the arrow to the left of it to expand it and check sub-folders). I don't 
<br>
<br>
<br>
Now remember: we have this in "Location 1", we need it in "Location 2" and "Location 3".  
So, simply copy everything relevant to the voice package you want to fix and paste it - so you have it twice (in my picture, everything from line 5 until the end)

Now, for one version of the copied text, change the path from "Location 1" to "Location 2"  
(simply put "<code>(...)\Microsoft\Speech<s>_OneCore</s>\Voices\(...)</code>" becomes "<code>(...)\Microsoft\Speech\Voices\(...)</code>").  
Do this for both the "voice package" and it's "Attributes" sub-folder.  
(Do this for the "Tokens" folder path as well in case you exported the whole "Tokens" as a .reg file).

For the other version of the copied text, change the path from "Location 1" to "Location 3"  
(simply put "<code>(...)\SOFTWARE\Microsoft\Speech_OneCore\Voices\(...)</code>" becomes "<code>(...)\SOFTWARE\\<b>WOW6432Node\\</b>Microsoft\Speech_OneCore\Voices\(...)</code>").

Here's how your .reg file should look like after the modifications:

![Reg file after modifications](./Readme%20Screenshots//EditedRegFile.png)

After you've done this, save your .reg file and close it, then double click it (or right click -> Merge)

![Caroline Merge](./Readme%20Screenshots/CarolineMerge.png)

After which, click "Yes" on the next Alert MessageBox, and "OK" on the following one

![Alert Messagebox](./Readme%20Screenshots/RegistryDialog.PNG)

# 3. We're done - all that's left is to test and develop

You can now check your required Registry Editor Location paths (2 & 3) to ensure that your chosen voice package (Caroline) can be found there as well.

Now, your voice packages should work just fine with pyttsx3, or other tts libraries of your choice: Here's a simple TTS hello world program.

![Caroline joins Hortense](./Readme%20Screenshots//CarolineHortense.png)

(Do note that selecting your own voice can be done either by "knowing" the voice ID beforehand, or, as I've done it = get all voices available in a list, then iterate through it and parse through them by searching for a **case sensitive** string in the voice id string)

Obviously, you can't hear the result of "engine.say()" here, but those are just 10 lines of code, so feel free to test them out yourself.