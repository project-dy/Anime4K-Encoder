![Logo of the project](demo.gif)

# Anime4K-Encoder
> Wrapper for [Anime4K](https://github.com/bloc97/Anime4K)

Makes it easy to encode a Anime using the MPV shaders with predefined encoding profiles!

## Key differences to Anime4K-PyWrapper

- Updated the shaders to work with the latest Anime4k shaders (4.0.1)
- Added x264 and x265 CPU support
- Removed NVENC
- Ability to choose CRF when encoding
- Auto burn in subs to eliminate a extra step [optional]
- Removed the second encoding option/mode, as I couldn't find a purpose apart from creating generation loss.
- Rearranged the code partially and added more comments to make it easier to modify.
- Butchered the code because I dont know how to code.

## Installing / Getting started

What you need:
- Linux (sorry its the fault of *mpv*)
- Python 3.X
- mpv > 0.32
- ffmpeg
- mkvnixtool (e.g mkvtoolnix on Ubuntu)
- mediainfo (e.g libmediainfo-dev mediainfo on Ubuntu)
- A dedicated GPU (no VM) [AMD/NVIDIA/Intel]

**Installing the necessary python libs**

```
pip3 install -r requirements.txt

```

### Initial Configuration

Download the latest shaders (GLSL (v4.0.1 Stable)) from [here](https://github.com/bloc97/Anime4K/releases).
Put them all into one folder for example called *shaders*

## Burning in subs

if there's a default sub track it will be burned in automatically, if you want to add softsubs you will have to add them later, to do so uncomment the following lines in shader.py:

[115] "--no-subtitles",
[116] "--no-audio",

This can also fix some audio problems that you may encounter during encoding, which may or may not slow down your encoding progress.

then follow the steps below normally

## Upscaling your first Anime!

Assuming your Anime Movie/Episode is called *input.mkv* and has a resolution of 1920x1080.
Now you want to upscale it to 4K (3840x2160).
Here are the commands you would run.

1. Encode the Video with the following command
```
python3 Anime4K.py -m shader --shader_dir "./shaders" --width 3840 --height 2160 -i input.mkv --output video_upscale.mkv

```
2. Follow the dialogues - they should be pretty self explanatory
4. Your file should now be in *video_upscale.mkv*
5. Done!

## If you didn't burned in the subs you need to add them this way.

1. Extract the audio and/or subtitles from the original file
```
python3 Anime4K.py -m audio -i input.mkv
python3 Anime4K.py -m subs -i input.mkv

```
2. Now we have the audio files and subtitles in the current folder.
3. Now lets add them into the final output

```
python3 Anime4K.py -m mux -i video_upscale.mkv -o video_upscaled_with_audio_and_subs.mkv

```
4. Done!

**Feel free to explore the other options of the program (or profiles) by typing**:

```
python3 Anime4K.py --help

```

## **[Optional]** Encoding ffmpeg progressbar
To get a overview of your current encoding of ffmpeg you may install the [ffmpeg-progressbar-cli](https://github.com/sidneys/ffmpeg-progressbar-cli)

```
npm install --global ffmpeg-progressbar-cli

```

*Don't worry the script will also work with normal ffmpeg.*

## Misc
This is a list of things that I've encountered but it may or may not be true for every user.

- The shader mode affects the encoding speed, from faster to slower C > B > A > C+A > B+B > A+A.
- The encoding preset doesnt noticeably affect the encoding speed (only tested from fastest to medium)
- I deprecated the NVENC since it butchers enormoulsy the quality of the video, even on high bitrates, and for that occasion just use x264.

## Benchmarks
Absolutely not a scientific test, done on a Ryzen 5 3600, GTX 1050ti

x264 | Fast | B+B = 0.9 Speed (12-14 fps)
x265 | Fast | B+B = 0.4 Speed (5-8 Fps)

Obviously the best way to use the shaders is in real time, its intended purpose. The purpose of this program is for those that can't run the HQ version of the shader (the one this one uses) in real time, or to use them for later (Phone, streaming server, etc)

## Features

* Encode Videos with Anime4K shaders easily
* Encode using x264 or x265
* Extract Audio and subtitles automatically
* Predefined profiles for Anime4K and ffmpeg

## TODO

- Batch Encoding.
- Adding extra shaders that are not included in the [Modes] by default (Darken, Thin, Etc)
- A way to get softsubs without having to mux the already upscaled video.
- Other things that you may find convenient

Keep in mind that I dont know how to code, its a miracle that this thing works. Many thanks to ThoughtfulDev for the original code.
If you want to add a feature it probably is easier to do it yourself since reading the code over and over again and trying to figure out what everything does without idea what a print() does can only get me so far.

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Links

- Related projects:
  - [**Huge thanks!**] Anime4K: https://github.com/bloc97/Anime4K
  - ThoughtfulDev: https://github.com/ThoughtfulDev/Anime4K
  - video2x: https://github.com/k4yt3x/video2x

- Thanks to:
  - ffmpeg-progressbar-cli: https://github.com/sidneys/ffmpeg-progressbar-cli
  - simple-term-menu: https://github.com/IngoHeimbach/simple-term-menu


## Licensing

The code in this project is licensed under GNU GENERAL PUBLIC LICENSE.
