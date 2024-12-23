# Pomodoro Timer CLI


## 🤔 Why?
is well known that a well structured working schedule will give us better results. The idea of this cli tool is to be simple, just three flags to control all your workflow. besides, it shows you motivational quotes to so you feel 💯%.

## 📦 Installation

```bash
# Install dependencies
python3 -m pip install playsound
python3 -m pip install pyfiglet
```

```bash
# Clone the repository
git clone https://github.com/maximofrias522/Pomodoro-CLI.git

# Navigate into the project directory
cd Pomodoro-CLI

# copy the audio file to your preferene path 
cp ~/Pomodoro-CLI/digital_watch_alarm.mp3 /your/preference/path

# Make sure to modify this line in the pomo.py file - 107- playsound("./digital_watch_alarm.mp3") # change this path to yours

# Make the code executable
chmod +x pomo.py

# Change filename and move to corresponding path
cp ~/Pomodoro-CLI/pomo.py /usr/local/bin/pomo

# Execute a test
pomo

```
---

## ⚙️ Usage
```bash
# Example usage command
pomo -w 5 -r 2 -s 4
# In this case, you will set 5 minutes of work, 2 minutes of rest and 4 sessions

# For more details
pomo -h

```
---

## 🛠️ Development
Feel free to modify this code and make your own versions for your own necessities.

---

## 📝 License
This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
For any inquiries, feel free to reach out:
- Email: [frsmaximo522@gmail.com](frsmaximo522@gmail.com)
- GitHub: [@maximofrias522](https://github.com/maximofrias522)

---



