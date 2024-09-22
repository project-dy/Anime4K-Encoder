import subprocess, os, sys,glob
from pymediainfo import MediaInfo
from pymkv import MKVFile
from utils import clear
# from simple_term_menu import TerminalMenu
from consts import *

#MODE SELECTION
def FHDMenu(shader_dir):
    # mode_menu = TerminalMenu(
    #     ["Mode A (High Quality, Medium Artifacts)",
    #     "Mode B (Medium Quality, Minor Artifacts)",
    #     "Mode C (Unnoticeable Quality Improvements)",
    #     "Mode A+A (Higher Quality, Might overshapen the image)",
    #     "Mode B+B (RECOMMENDED. High Quality, Minor Artifacts)",
    #     "Mode C+A (Low Quality, Minor Artifacts)"
    #     ],
    #     title="Please refer to the Anime4k Wiki for more info\nand try the shaders on mpv beforehand to know whats best for you\nChoose Shader Preset:"
    # )
    # mode_choice = mode_menu.show()
    print("Please refer to the Anime4k Wiki for more info\nand try the shaders on mpv beforehand to know whats best for you\nChoose Shader Preset:")
    print("1. Mode A (High Quality, Medium Artifacts)")
    print("2. Mode B (Medium Quality, Minor Artifacts)")
    print("3. Mode C (Unnoticeable Quality Improvements)")
    print("4. Mode A+A (Higher Quality, Might overshapen the image)")
    print("5. Mode B+B (RECOMMENDED. High Quality, Minor Artifacts)")
    print("6. Mode C+A (Low Quality, Minor Artifacts)")
    mode_choice = int(input("Enter your choice: "))-1

    # if mode_choice == None:
    if mode_choice == -1:
        print("Canceling")
        sys.exit(-1)

    #Apply Shaders
    if mode_choice == 0:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s
    elif mode_choice == 1:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_Soft_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s
    elif mode_choice == 2:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_Denoise_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s
    elif mode_choice == 3:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_M)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s
    elif mode_choice == 4:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_Soft_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_Soft_M)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s
    elif mode_choice == 5:
        s = os.path.join(shader_dir, Clamp_Highlights)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_Denoise_CNN_x2_VL)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x2)
        s = s + ":"
        s = s + os.path.join(shader_dir, AutoDownscalePre_x4)
        s = s + ":"
        s = s + os.path.join(shader_dir, Restore_CNN_M)
        s = s + ":"
        s = s + os.path.join(shader_dir, Upscale_CNN_x2_M)
        return s

#MACROS OR SOMETHING

def remove_audio_and_subs(fn):
    subprocess.call([
        "mkvmerge",
        "-o",
        "temp.mkv",
        #"--no-subtitles",
        #"--no-audio",
        fn
    ])

#IDK WHAT THIS DOES
def shader(fn, width, height, shader, ten_bit, outname):
    clear()
    files = []
    if os.path.isdir(fn):
        for file in glob.glob(os.path.join(fn, "*.mkv")):
            files.append(os.path.join(file))
    else:
        remove_audio_and_subs(fn)
        fn = "temp.mkv"
        clear()

#SELECT ENCODER 264/265
    # cg_menu = TerminalMenu(
    #     ["X264 (Medium Quality/Size ratio, Fast)",
    #     "X265 (High Quality/Size ratio, Slow)"
    #     ],
    #     title="Choose your video codec."
    # )
    # cg_choice = cg_menu.show()
    print("Choose your video codec.")
    print("1. X264 (Medium Quality/Size ratio, Fast)")
    print("2. X265 (High Quality/Size ratio, Slow)")
    cg_choice = int(input("Enter your choice: "))-1
    if cg_choice == 0:
        avc_shader(fn, width, height, shader, ten_bit, outname, files=files)
    elif cg_choice == 1:
        hevc_shader(fn, width, height, shader, ten_bit, outname, files=files)
    else:
        print("Cancel")
        sys.exit(-2)

#REMOVE TEMP OR SOMETHING
    if os.path.isdir(fn):
        os.remove("temp.mkv")
    else:
        os.remove(fn)

#Video settings 264

def avc_shader(fn, width, height, shader, ten_bit, outname, files=[]):
    clear()

#ALWAYS 10 BIT BC FOR SOME REASON IT DIDNT DETECTED 10 BIT ON THE ORIGINAL
    format = "yuv420p10le"

#detect width and height of video.
    if len(files) == 0:
        _m = MediaInfo.parse(fn)
    else:
        _m = MediaInfo.parse(files[0])
    track_width = -1
    for t in _m.tracks:
        if t.track_type == 'Video':
            track_width = t.width
            str_shaders = FHDMenu(shader)
    clear()

#Select Codec Presets
    encoder_preset = [
        "veryfast", "fast", "medium", "slow", "veryslow"
    ]
    # codec_preset = encoder_preset[TerminalMenu(encoder_preset, title="Choose your encoder preset:").show()]
    codec_preset = encoder_preset[int(input("Choose your encoder preset:\n0. veryfast\n1. fast\n2. medium\n3. slow\n4. veryslow\n"))]

    crf = input("Insert compression factor (CRF) 0-51\n0 = Lossless | 23 = Default | 51 = Highest compression\n")

#PRINT INFO
    print("File: " + fn)
    print("Using the following shaders:")
    print(str_shaders)
    print("Encoding with preset: " +  codec_preset + " crf=" + crf)
    import time
    time.sleep(3)
    #clear()

#ENCODE
    if len(files) == 0:
        subprocess.call([
            "mpv",
            #"--vf=format=" + format,
            fn,
            "--profile=gpu-hq",
            "--scale=ewa_lanczossharp",
            "--cscale=ewa_lanczossharp",
            "--video-sync=display-resample",
            "--interpolation",
            "--tscale=oversample",
            '--vf=gpu=w=' + str(width) + ':h=' + str(height),
            "--glsl-shaders=" + str_shaders,
            "--oac=libopus",
            "--oacopts=b=192k",
            "--ovc=libx264",
            '--ovcopts=preset=' + codec_preset + ',level=6.1,crf=' + str(crf) + ',aq-mode=3,psy-rd=1.0,bf=6',
            '--vf-pre=sub',
            '--o=' + outname
        ])
    else:
        i = 0
        for f in files:
            remove_audio_and_subs(f)
            clear()
            name = f.split("/")
            name = name[len(name) - 1]
            subprocess.call([
                "mpv",
                #"--vf=format=" + format,
                "temp.mkv",
                "--profile=gpu-hq",
                "--scale=ewa_lanczossharp",
                "--cscale=ewa_lanczossharp",
                "--video-sync=display-resample",
                "--interpolation",
                "--tscale=oversample",
                '--vf=gpu=w=' + str(width) + ':h=' + str(height),
                "--glsl-shaders=" + str_shaders,
                "--oac=libopus",
                "--oacopts=b=192k",
                "--ovc=libx264",
                '--ovcopts=preset=' + codec_preset + ',level=6.1,crf=' + str(crf) + ',aq-mode=3,psy-rd=1.0,bf=8',
                '--vf-pre=sub',
                '--o=' + os.path.join(outname, name)
            ])
            i = i + 1



#Video settings 265

def hevc_shader(fn, width, height, shader, ten_bit, outname, files=[]):
    clear()
#ALWAYS 10BIT BEACUSE IT DOESNT DETECT 10 BIT

    format = "yuv420p10le"


#detect width and height of video.
    if len(files) == 0:
        _m = MediaInfo.parse(fn)
    else:
        _m = MediaInfo.parse(files[0])
    track_width = -1
    for t in _m.tracks:
        if t.track_type == 'Video':
            track_width = t.width
            str_shaders = FHDMenu(shader)
    clear()

#Select Codec Presets
    encoder_preset = [
        "veryfast", "fast", "medium", "slow", "veryslow"
    ]
    # codec_preset = encoder_preset[TerminalMenu(encoder_preset, title="Choose your encoder preset:").show()]
    codec_preset = encoder_preset[int(input("Choose your encoder preset:\n0. veryfast\n1. fast\n2. medium\n3. slow\n4. veryslow\n"))]
    crf = input("Insert compression factor (CRF) 0-51\n0 = Lossless | 28 = Default | 51 = Highest compression\n")

#PRINT INFO
    print("File: " + fn)
    print("Using the following shaders:")
    print(str_shaders)
    print("Encoding with preset: " +  codec_preset + " crf=" + crf)
    import time
    time.sleep(3)
    #clear()

#ENCODE
    if len(files) == 0:
        subprocess.call([
            "mpv",
            #"--vf=format=" + format,
            fn,
            "--profile=gpu-hq",
            "--scale=ewa_lanczossharp",
            "--cscale=ewa_lanczossharp",
            "--video-sync=display-resample",
            "--interpolation",
            "--tscale=oversample",
            '--vf=gpu=w=' + str(width) + ':h=' + str(height),
            "--glsl-shaders=" + str_shaders,
            "--oac=libopus",
            "--oacopts=b=192k",
            "--ovc=libx265",
            '--ovcopts=preset=' + codec_preset + ',level=6.1,crf=' + str(crf) + ',aq-mode=3,psy-rd=1.0,bf=6',
            '--vf-pre=sub',
            '--o=' + outname
        ])
    else:
        i = 0
        for f in files:
            remove_audio_and_subs(f)
            clear()
            name = f.split("/")
            name = name[len(name) - 1]
            subprocess.call([
                "mpv",
                #"--vf=format=" + format,
                "temp.mkv",
                "--profile=gpu-hq",
                "--scale=ewa_lanczossharp",
                "--cscale=ewa_lanczossharp",
                "--video-sync=display-resample",
                "--interpolation",
                "--tscale=oversample",
                '--vf=gpu=w=' + str(width) + ':h=' + str(height),
                "--glsl-shaders=" + str_shaders,
                "--oac=libopus",
                "--oacopts=b=192k",
                "--ovc=libx265",
                '--ovcopts=preset=' + codec_preset + ',level=6.1,crf=' + str(crf) + ',aq-mode=3,psy-rd=1.0,bf=8',
                '--vf-pre=sub',
                '--o=' + os.path.join(outname, name)
            ])
            i = i + 1
