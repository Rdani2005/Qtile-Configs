# Qtile-Configs

This are my personal configs for Qtile window manager. For using this I recommend to download the <a href="https://wiki.archlinux.org/title/LightDM_(Espa%C3%B1ol)">Light DM</a> package for a login manager.

## Drivers

for using this, in my PC I installed the next drivers. This config is made in <a href="https://archlinux.org/">Arch Linux</a> and it was installed on a <a href="https://www.amazon.com/-/es/Latitude-E6440-i7-4600M-Windows-renovado/dp/B07GCRY8NC">Dell E6640</a> notebook.
Some of the drivers that I'm using is for my PC components. You should check out wich drivers are the right ones for your PC first.
### Video
<ul>
  <li><a href="https://wiki.archlinux.org/title/Intel_graphics_(Espa%C3%B1ol)">xf86-video-intel</a></li>
  <li><a href="https://wiki.archlinux.org/title/microcode">intel-ucode</a></li>
  <li><a href="https://wiki.archlinux.org/title/Vulkan">Vulkan-Intel</a></li>
  <li><a href="https://archlinux.org/packages/?name=vulkan-icd-loader">vulkan-icd-loader</a></li>
  <li><a href="https://archlinux.org/packages/extra/x86_64/mesa/">mesa</a></li>
  <li><a href="https://archlinux.org/packages/extra/x86_64/mesa-demos/">mesa-demos</a></li>
  <li><a href="https://wiki.archlinux.org/title/Intel_graphics_(Espa%C3%B1ol)">xorg-server</a></li>
  <li><a href="https://wiki.archlinux.org/title/Intel_graphics_(Espa%C3%B1ol)">xorg-xinit</a></li>
</ul>

## Programs for using
I decided to use the next programs
<ul>
  <li><a href="https://wiki.archlinux.org/title/PulseAudio">pulseaudio</a></li>
  <li><a href="https://archlinux.org/packages/extra/x86_64/pavucontrol/">pavucontrol</a></li>
  <li><a href="https://archlinux.org/packages/community/x86_64/pamixer/">pamixer</a></li>
  <li><a href="https://wiki.archlinux.org/title/Alacritty">alacritty</a></li>
  <li><a href="https://wiki.archlinux.org/title/feh">feh</a></li>
  <li><a href="https://archlinux.org/packages/core/x86_64/which/">which</a></li>
  <li><a href="https://wiki.archlinux.org/title/Rofi">rofi</a></li>
  <li><a href="https://wiki.archlinux.org/title/Visual_Studio_Code">code</a></li>
  <li><a href="https://wiki.archlinux.org/title/Firefox_(Espa%C3%B1ol)">firefox</a></li>
  <li><a href="https://archlinux.org/packages/community/any/arandr/">arandr</a></li>
  <li><a href="https://archlinux.org/groups/x86_64/base-devel/">base-devel</a></li>
  <li><a href="https://wiki.archlinux.org/title/git">git</a></li>
  <li><a href="https://archlinux.org/packages/extra/x86_64/geeqie/">geqiee</a></li>
  <li><a href="https://wiki.archlinux.org/title/VLC_media_player_(Espa%C3%B1ol)">vlc</a></li>
  <li><a href="https://archlinux.org/packages/community/x86_64/lxappearance/">lxappearance</a></li>
  <li><a href="https://wiki.archlinux.org/title/Thunar_(Espa%C3%B1ol)">Thunar</a></li>
</ul>

## How is it built?
Well, it is built in Python, so I created diferents python files. The first one is called "MyLayouts.py", where you can find the differents layouts that are available on my configs.
The second one is called "MyPersonalKey.py" where you can find the keymap that is used on Qtile. At the end of this explination, you will find a table that contains the keymaps.
The third one is called "MyWidgets.py", and here you can find the widgets that are used on the top bar of qtile.
Then, you will find a file called "autostart.sh" that contains a list of commands that are going to be execute when Qtile starts. 

## "Config.py" file
Right here, we call all all of our files and objects, so they can be used on Qtile

## Table Keys
<table>
  <tr>
    <td><b>Special Key</b></td>
    <td><b>+ Key</b></td>
    <td><b>Action</b></td>
  </tr>
  <tr>
    <td>Super</td>
    <td>Return</td>
    <td>Spawns an Alacritty terminal</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>B</td>
    <td>Opens a browser (in my case, firefox)</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>c</td>
    <td>Open a code editor (in my case, Visual Studio Code)</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>m</td>
    <td>Open a menu app (in my case, Rofi)</td>
  </tr>
  <tr>
    <td>Super + Shift</td>
    <td>w</td>
    <td>Kill the app that is running on the focused window</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>left arrow</td>
    <td>Move the focuse to the left</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>right arrow</td>
    <td>Move the focuse to the right</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>up arrow</td>
    <td>Move the focuse up</td>
  </tr>
  <tr>
    <td>Super</td>
    <td>down Arrow</td>
    <td>Move the focuse down</td>
  </tr>
  <tr>
    <td>Super + Shift</td>
    <td>left arrow</td>
    <td>Move the window to the left</td>
  </tr>
  <tr>
    <td>Super + Shift</td>
    <td>Right Arrow</td>
    <td>Move the window to the right</td>
  </tr>
  <tr>
    <td>Super + Shift</td>
    <td>Up Arrow</td>
    <td>Move the window up</td>
  </tr>
  <tr>
    <td>Super + Shift</td>
    <td>Down Arrow</td>
    <td>Move the window down</td>
  </tr>
  <tr>
    <td>Super + Control</td>
    <td>Left Arrow</td>
    <td>Grow the window to the left</td>
  </tr>
  <tr>
    <td>Super + Control</td>
    <td>Right Arrow</td>
    <td>Grow the window to the right</td>
  </tr>
  <tr>
    <td>Super + Control</td>
    <td>Up Arrow</td>
    <td>Grow the window up</td>
  </tr>
  <tr>
    <td>Super + Control</td>
    <td>Down Arrow</td>
    <td>Grow window down</td>
  </tr>
    <tr>
    <td>Super</td>
    <td>N</td>
    <td>Restart all the sizes of the windows</td>
  </tr>
    <tr>
    <td>Super</td>
    <td>Tab</td>
    <td>Change the Layout of Qtile</td>
  </tr>
  <tr>
   <td>Super + shift</td>
   <td>Q</td>
   <td>Shut Dowm Qtile</td>
  </tr>
  <tr>
   <td>Super + Shift</td>
   <td>R</td>
   <td>Restart Qtile</td>
  </tr>  
  <tr>
    <td>Super</td>
    <td>number between 1 and 8</td>
    <td>Change the group that we are working on</td>
  </tr>
</table>
